# REAL-TIME OBJECT DETECTION USING YOLO-V10 (COMPUTER VISION)

## 📌 Project Description

This project implements real-time object detection using YOLO-V10 and computer vision techniques. The system detects and classifies multiple objects in images with high accuracy and speed. YOLO-V10 provides efficient object localization and recognition, making it suitable for real-world applications such as surveillance, traffic monitoring, and smart systems.

---

## ✨ Features

- Real-time object detection
- Multiple object recognition
- High accuracy and speed
- Bounding box visualization
- Confidence score display
- User-friendly interface

---

## 🛠 Technologies Used

### Programming Language
- Python

### Libraries
- YOLOv10
- OpenCV
- NumPy
- PyTorch

### Tools
- VS Code
- GitHub
- Git
### Supported Media
1.Images (JPG,JPEG,PNG)
2.Videos(MP4,AVI,MOV)

### Platform
windows/linux/macOS

---

## **Project Structure**
## Project Structure

```text
object-detection/
│
├── app.py                     # Main application file
├── requirements.txt           # Required Python packages
├── README.md                  # Project documentation
│
├── yolov10m.pt                # Pre-trained YOLOv10 model
│
├── assets/
│   ├── images/                # Sample input images
│   └── videos/                # Sample input videos
│
├── outputs/
│   ├── detected_images/       # Output images with detections
│   └── detected_videos/       # Output videos with detections
│
└── screenshots/
    └── demo.png               # Project screenshots
```
object-detection/
│
├── app.py
├── requirements.txt
├── README.md
├── yolov10m.pt
├── static/
├── outputs/
└── assets/
# Installtion
 ## Step 1: Clone the Repository
 git clone https://github.com/swamyelurieluri-boop/object-detection.git
cd object-detection
## Step 2: Activate the virtual Environment
### widows
venv\Scripts\activate
### Linux/macOS
source venv/bin/activate
## Step 3: Install Required Dependencies
pip install ultralytics
pip install opencv-python
pip install gradio
pip install numpy
pip install torch torchvision
## Step 4: Run the Application
python app.py
## Step 5: Open in Browser
http://127.0.0.1:7860
# Future Enhancements
Integrate live webcam-based object detection for real-time monitoring.
Deploy the application on cloud platforms for remote access and scalability.
Add object tracking functionality to monitor moving objects across video frames.
Implement custom dataset training for domain-specific object detection tasks.
Enhance the user interface with advanced visualization and analytics features.
Optimize the model for edge devices and mobile platforms.
Generate automated detection reports with object statistics and confidence scores.
Support real-time video streaming from IP cameras and surveillance systems.
Improve detection accuracy in low-light and complex environmental conditions.



