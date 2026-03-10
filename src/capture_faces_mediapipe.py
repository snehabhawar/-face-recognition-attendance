import cv2
import mediapipe as mp
import os

name = input("Enter your name: ")

dataset_path = f"../dataset/known_faces/{name}"
os.makedirs(dataset_path, exist_ok=True)

mp_face_detection = mp.solutions.face_detection

cap = cv2.VideoCapture(0)

count = 0
max_images = 800

with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.6) as face_detection:

    print("Starting capture...")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_detection.process(rgb)

        if results.detections:

            for detection in results.detections:

                bbox = detection.location_data.relative_bounding_box

                h, w, _ = frame.shape

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)

                x = max(0, x)
                y = max(0, y)

                face = frame[y:y+height, x:x+width]

                if face.size == 0:
                    continue

                gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                gray = cv2.resize(gray, (200,200))

                img_path = f"{dataset_path}/{count}.jpg"

                cv2.imwrite(img_path, gray)

                count += 1

                cv2.rectangle(frame,(x,y),(x+width,y+height),(0,255,0),2)

        cv2.imshow("Capturing Faces", frame)

        if count >= max_images:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

print(f"Captured {count} images for {name}")