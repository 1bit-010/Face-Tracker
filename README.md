# Face Tracker

A real-time face tracking application built using **Python** and **OpenCV**. This program detects faces using the Haar Cascade Classifier and tracks them in a live video feed or a video file.

## Features

1. **Real-Time Face Tracking**:
   - Detects faces using Haar Cascade XML classifier.
   - Displays rectangles around detected faces in real-time.

2. **Customizable Video Source**:
   - Use your webcam or provide a video file for face tracking.

3. **User-Friendly Exit**:
   - Exit the video feed by pressing `q`.



## Prerequisites

1. **Python 3.x**
   - Ensure you have Python installed. Download it from [python.org](https://www.python.org/).

2. **Install Required Libraries**:
   - Install OpenCV:
     ```bash
     pip install opencv-python opencv-python-headless
     ```

3. **Haar Cascade XML File**:
   - OpenCV includes pre-trained Haar Cascade classifiers. This program uses the `haarcascade_frontalface_default.xml` file, which is included in OpenCV's default installation.



## Installation

1. Clone this repository or download the source code:
   ```bash
   git clone https://github.com/1bit-010/Face-Tracker.git


2. Navigate to the project directory:
   ```bash
   cd face-tracker




## Usage

1. **Run the Program**:
   - By default, the program uses the first available webcam (camera index `0`).
   - To track faces from a video file, modify the `video_source` argument in the `face_tracker()` function.

2. **Interact with the Feed**:
   - A window will open showing the video feed.
   - Detected faces will be highlighted with green rectangles.

3. **Exit**:
   - Press `q` to close the video feed.





## Customization

1. **Change Video Source**:
   - To use a video file, modify this line in the `face_tracker()` function:
     ```python
     video_source = "path/to/video.mp4"
     ```

2. **Adjust Detection Parameters**:
   - Modify the `scaleFactor`, `minNeighbors`, and `minSize` parameters of `detectMultiScale()` for more control over detection sensitivity:
     ```python
     faces = face_cascade.detectMultiScale(
         gray_frame,
         scaleFactor=1.1,  # Resize image at each scale step
         minNeighbors=5,   # Minimum neighbors to retain detection
         minSize=(30, 30)  # Minimum face size
     )
     ```


## Future Enhancements

1. **Deep Learning-Based Detection**:
   - Use OpenCV's DNN module for more robust face detection.

2. **Face Recognition**:
   - Incorporate models like dlib or FaceNet for face recognition.

3. **Save Detected Faces**:
   - Add functionality to capture and save detected faces as images.

4. **GUI Support**:
   - Create a graphical user interface using `tkinter` or `PyQt`.



Enjoy tracking faces in real-time! 😊

