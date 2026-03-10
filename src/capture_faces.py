import cv2
import os

# Ask for name
name = input("Enter your name: ")

# Get project root directory (one level above src)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create dataset path
dataset_path = os.path.join(base_dir, "dataset", "known_faces", name)
os.makedirs(dataset_path, exist_ok=True)

print("Saving images to:", dataset_path)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

count = 0
max_images = 100

print("Starting face capture...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(40,40)
    )

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200,200))

        img_path = os.path.join(dataset_path, f"{count}.jpg")
        cv2.imwrite(img_path, face)

        count += 1

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Capturing Faces", frame)

    if count >= max_images:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Captured {count} images for {name}")