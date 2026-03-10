#  AI Face Recognition Attendance System

A **real-time attendance system** built using **Computer Vision and Deep Learning**.
The system detects faces through a webcam, recognizes individuals using **FaceNet embeddings via DeepFace**, and automatically logs attendance in **CSV and Excel formats**.

---

##  Features

* 🎥 Real-time face detection using webcam
* 🧠 Deep learning face recognition (FaceNet / DeepFace)
* 📝 Automatic attendance logging
* 📊 Excel attendance export
* 📋 Live attendance dashboard showing present students
* 🔁 Duplicate attendance prevention
* 🔒 Privacy-safe repository (face images excluded)

---

##  Demo

Example system output:
<img width="481" height="383" alt="image" src="https://github.com/user-attachments/assets/385de558-3565-41b9-a853-1d0315fa1ae5" />


```
Students Present: 1

✔ Sneha
✔ Alex
---

##  Project Structure

```
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
```

 Face images are **not included** in the repository for privacy reasons.

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/face-recognition-attendance.git
cd face-recognition-attendance
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Usage

###  Capture Face Dataset

```bash
python src/capture_faces_mediapipe.py
```

This captures face images using your webcam.

---

###  Train the Recognition Model

```bash
python src/train_model.py
```

---

###  Run the Attendance System

```bash
python src/recognize_deepface.py
```

The system will:

* Detect faces in real time
* Recognize known individuals
* Log attendance automatically

---

##  Attendance Output

Attendance logs are generated in:

```
attendance/attendance.csv
attendance/attendance.xlsx
```

Example:

| Name  | Date       | Time  |
| ----- | ---------- | ----- |
| Sneha | 2026-03-10 | 18:41 |
| Alex  | 2026-03-10 | 18:43 |

---

##  Tech Stack

* Python
* OpenCV
* MediaPipe
* DeepFace (FaceNet)
* TensorFlow
* Pandas

---

##  Privacy

This repository **does not include face images**.

Users must capture their own dataset locally before running the system.

---

##  Future Improvements

*  Web dashboard for attendance monitoring
*  Multi-camera support
*  Cloud database integration
*  Mobile camera support

---

##  Author

**Sneha Bhawar**

