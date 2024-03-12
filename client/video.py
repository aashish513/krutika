import cv2

# URL of the Flask server's video feed endpoint
url = 'http://127.0.0.1:5000/video'

# OpenCV VideoCapture object to read frames from the video feed
cap = cv2.VideoCapture(url)

while True:
    # Read frame from the video feed
    ret, frame = cap.read()

    # If frame is successfully read
    if ret:
        # Display the frame
        cv2.imshow('Video Feed', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error reading frame from video feed")
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
