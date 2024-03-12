from flask import Flask, render_template, Response, request

#video
import video
import speak
app = Flask(__name__)



@app.route('/')
def index():
    return "this server is running"

#serve video
@app.route('/video')
def video_feed():
    return Response(video.generate_frames(video_stream), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/speak', methods=['POST', 'GET'])
def speak_now():
    return speak.speak(request)


if __name__ == '__main__':
    video_stream = video.VideoStream()
    app.run(debug=True, host= "127.0.0.1", port =5000)
