import cv2
import mediapipe as mp

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.6) as face_detection:

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert to RGB (MediaPipe requires RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:

                bbox = detection.location_data.relative_bounding_box

                h, w, c = frame.shape

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)

                cv2.rectangle(frame,
                              (x, y),
                              (x + width, y + height),
                              (0,255,0),
                              2)

        cv2.imshow("MediaPipe Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()