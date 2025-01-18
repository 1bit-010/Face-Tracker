import cv2

def face_tracker(video_source=0):
    """
    Tracks faces in real-time using OpenCV and displays them in a live video feed.
    
    Args:
        video_source (int or str): Camera index (e.g., 0 for the default webcam) or video file path.
    """
    # Load the Haar Cascade XML file for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # type: ignore
    
    # Open the video source (webcam or video file)
    video_capture = cv2.VideoCapture(video_source)
    
    if not video_capture.isOpened():
        print("Error: Unable to open video source.")
        return

    print("Press 'q' to exit the live video feed.")
    
    while True:
        # Read frames from the video feed
        ret, frame = video_capture.read()
        
        if not ret:
            print("Error: Unable to read frame.")
            break
        
        # Convert the frame to grayscale (Haar Cascade works on grayscale images)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,  # Scale factor for image resizing
            minNeighbors=5,   # Minimum neighbors to retain a detection
            minSize=(30, 30)  # Minimum size of detected faces
        )
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Display the frame with detected faces
        cv2.imshow('Face Tracker', frame)
        
        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture and close OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

# Run the face tracker
if __name__ == "__main__":
    face_tracker()
