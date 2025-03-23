import cv2

def detect_faces(video_input=0):
    # Load the Haar Cascade classifier for face detection
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # type: ignore
    
    # Open the video source (webcam or video file)
    video_stream = cv2.VideoCapture(video_input)
    
    if not video_stream.isOpened():
        print("Error: Unable to access video input.")
        return

    print("Press 'q' to exit the live video feed.")
    
    while True:
        # Capture frames from the video stream
        success, frame_data = video_stream.read()
        
        if not success:
            print("Error: Unable to retrieve frame.")
            break
        
        # Convert the frame to grayscale for processing
        grayscale_frame = cv2.cvtColor(frame_data, cv2.COLOR_BGR2GRAY)
        
        # Perform face detection
        detected_faces = face_detector.detectMultiScale(
            grayscale_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Draw rectangles around detected faces
        for (x_coord, y_coord, width, height) in detected_faces:
            cv2.rectangle(frame_data, (x_coord, y_coord), (x_coord + width, y_coord + height), (0, 255, 0), 2)
        
        # Display the processed frame
        cv2.imshow('Face Detection', frame_data)
        
        # Exit loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources and close  windows
    video_stream.release()
    cv2.destroyAllWindows()

# Execute the function
if __name__ == "__main__":
    detect_faces()
