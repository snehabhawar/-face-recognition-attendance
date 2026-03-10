import cv2
import os
import numpy as np

# Path to dataset
dataset_path = "../dataset/known_faces"

faces = []
labels = []
label_map = {}
current_label = 0

# Read dataset folders
for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_folder):
        continue

    label_map[current_label] = person_name

    for image_name in os.listdir(person_folder):

        img_path = os.path.join(person_folder, image_name)

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        faces.append(img)
        labels.append(current_label)

    current_label += 1


faces = np.array(faces)
labels = np.array(labels)

print("Training on", len(faces), "images")

# Create LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, labels)

# Save trained model
recognizer.save("../dataset/face_model.yml")

# Save label mapping
np.save("../dataset/labels.npy", label_map)

print("Model trained successfully!")