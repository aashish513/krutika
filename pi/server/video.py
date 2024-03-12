import cv2
import threading




class VideoStream:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.lock = threading.Lock()

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        with self.lock:
            ret, frame = self.cap.read()
            if not ret:
                return None
            #frame = cv2.flip(frame, 1)
            ret, buffer = cv2.imencode('.jpg', frame)
            return buffer.tobytes()

def generate_frames(video_stream):
    while True:
        frame = video_stream.get_frame()
        if frame is None:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')