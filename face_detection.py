'''
import cv2

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture video from the laptop's camera
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Face Detection', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
'''
import cv2

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture video from the laptop's camera
video_capture = cv2.VideoCapture(0)

# Process every nth frame
frame_skip = 2
frame_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    if not ret:
        break
    
    frame_count += 1
    
    # Only process every nth frame
    if frame_count % frame_skip == 0:
        # Resize the frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        
        # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
        gray_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw rectangles around the detected faces on the original frame
        for (x, y, w, h) in faces:
            # Scale coordinates back to original frame size
            x *= 2
            y *= 2
            w *= 2
            h *= 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Face Detection', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
