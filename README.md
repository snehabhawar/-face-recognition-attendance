AI Face Recognition Attendance System

A real-time attendance system built using Computer Vision and Deep Learning.
The system detects faces through a webcam, recognizes individuals using FaceNet embeddings via DeepFace, and automatically logs attendance in CSV and Excel formats.

Features

Real-time face detection using webcam

Deep learning face recognition (FaceNet / DeepFace)

Automatic attendance logging

Excel attendance export

Live attendance dashboard showing present students

Duplicate attendance prevention

Privacy-safe repository (face images excluded)

Demo

Example system output:

Students Present: 2

✔ Sneha
✔ Alex
Project Structure
face-recognition-attendance
│
├── src
│   ├── capture_faces_mediapipe.py
│   ├── train_model.py
│   ├── recognize.py
│   └── recognize_deepface.py
│
├── dataset
│   └── known_faces
│       └── README.md
│
├── attendance
│   └── README.md
│
├── screenshots
│
├── requirements.txt
├── README.md
└── .gitignore

Face images are not included for privacy reasons.

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/face-recognition-attendance.git
cd face-recognition-attendance

Install dependencies:

pip install -r requirements.txt
Usage
1. Capture Face Dataset
python src/capture_faces_mediapipe.py

This will capture face images using the webcam.

2. Train the Recognition Model
python src/train_model.py
3. Run the Attendance System
python src/recognize_deepface.py

The system will:

detect faces in real time

recognize known individuals

log attendance automatically

Attendance Output

Attendance logs are saved as:

attendance/attendance.csv
attendance/attendance.xlsx

Example:

Name	Date	Time
Sneha	2026-03-10	18:41
Alex	2026-03-10	18:43
Tech Stack

Python

OpenCV

MediaPipe

DeepFace (FaceNet)

TensorFlow

Pandas

Privacy

This repository does not include face images.
Users must capture their own dataset locally before running the system.

Future Improvements

Web dashboard for attendance monitoring

Multi-camera support

Cloud database integration

Mobile camera support

Author

Sneha Bhawar
Computer Science Student