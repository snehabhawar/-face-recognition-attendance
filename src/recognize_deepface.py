import cv2
from deepface import DeepFace
import datetime
import csv
import os

dataset_path = "../dataset/known_faces"
attendance_file = "../attendance/attendance.csv"
excel_file = "../attendance/attendance.xlsx"

marked_names = set()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    try:
        results = DeepFace.find(
            img_path=frame,
            db_path=dataset_path,
            model_name="Facenet",
            enforce_detection=False
        )

        if len(results[0]) > 0:

            identity_path = results[0]['identity'][0]

            name = identity_path.split("\\")[-2]

        else:
            name = "Unknown"

    except:
        name = "Unknown"

    if name != "Unknown":

        if name not in marked_names:

            date_today = datetime.datetime.now().strftime("%Y-%m-%d")
            time_now = datetime.datetime.now().strftime("%H:%M:%S")

            with open(attendance_file,"a",newline="") as f:
                writer = csv.writer(f)
                writer.writerow([name,date_today,time_now])

            marked_names.add(name)

            print(f"{name} marked present")

    cv2.putText(
        frame,
        name,
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Students Present: {len(marked_names)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        3
    )

    y_offset = 120

    for student in marked_names:

        cv2.putText(
            frame,
            f"Present {student}",
            (20,y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,255),
            2
        )

        y_offset += 30

    cv2.imshow("Deep Learning Attendance System",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()