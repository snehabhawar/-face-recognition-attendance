import cv2
import mediapipe as mp
import numpy as np
import datetime
import csv
import os
import pandas as pd

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("../dataset/face_model.yml")

labels = np.load("../dataset/labels.npy", allow_pickle=True).item()

attendance_file = "../attendance/attendance.csv"
excel_file = "../attendance/attendance.xlsx"


def load_marked_names(file):
    marked = set()

    if os.path.exists(file):
        with open(file, "r") as f:
            reader = csv.reader(f)
            next(reader, None)

            for row in reader:
                if len(row) > 0:
                    marked.add(row[0])

    return marked


marked_names = load_marked_names(attendance_file)

last_seen = {}
cooldown = 5

mp_face_detection = mp.solutions.face_detection

cap = cv2.VideoCapture(0)

recent_predictions = []
prediction_threshold = 5

with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.6) as face_detection:

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_detection.process(rgb)

        name = "Unknown"
        confidence_percent = 0

        if results.detections:

            detection = results.detections[0]

            bbox = detection.location_data.relative_bounding_box

            h, w, _ = frame.shape

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            width = int(bbox.width * w)
            height = int(bbox.height * h)

            x = max(0, x)
            y = max(0, y)

            face = frame[y:y+height, x:x+width]

            if face.size != 0:

                gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                gray_face = cv2.equalizeHist(gray_face)
                gray_face = cv2.resize(gray_face, (200,200))

                label, confidence = recognizer.predict(gray_face)

                confidence_percent = max(0, 100 - int(confidence))

                predicted_name = "Unknown"

                if confidence_percent > 50:
                    predicted_name = labels[label]

                recent_predictions.append(predicted_name)

                if len(recent_predictions) > prediction_threshold:
                    recent_predictions.pop(0)

                if recent_predictions.count(predicted_name) >= 3:
                    name = predicted_name

                current_time = datetime.datetime.now().timestamp()

                if name != "Unknown":

                    if name not in last_seen or current_time - last_seen[name] > cooldown:

                        last_seen[name] = current_time

                        if name not in marked_names:

                            date_today = datetime.datetime.now().strftime("%Y-%m-%d")
                            time_now = datetime.datetime.now().strftime("%H:%M:%S")

                            with open(attendance_file, "a", newline="") as f:
                                writer = csv.writer(f)
                                writer.writerow([name, date_today, time_now])

                            marked_names.add(name)

                            # update Excel
                            df = pd.read_csv(attendance_file)
                            df.to_excel(excel_file, index=False)

                            print(f"{name} marked present")

                cv2.rectangle(frame,(x,y),(x+width,y+height),(0,255,0),2)

        # Display recognition result
        cv2.putText(
            frame,
            f"{name} ({confidence_percent}%)",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        # Student counter
        cv2.putText(
            frame,
            f"Students Present: {len(marked_names)}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            3
        )

        # Dashboard panel
        y_offset = 120

        for student in marked_names:

            cv2.putText(
                frame,
                f" {student}",
                (20, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2
            )

            y_offset += 30

        cv2.imshow("Face Recognition Attendance Dashboard", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()