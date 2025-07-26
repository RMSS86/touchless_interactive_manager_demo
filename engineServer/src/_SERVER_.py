from flask import Flask, Response
from _CONVERTER_ import _CONVERT_

app=Flask(__name__)

def gen(camera_):
    while True:
        jpeg_frame = camera_._get_frame_()#actaully _VIDEO_._get_frame_() method
        yield (b'--frame\r\n'
               b'Content-Type:image/jpeg\r\n\r\n' + jpeg_frame + b'\r\n\r\n')  #

@app.route('/video_feed')
def video_feed():
    return Response(gen(_CONVERT_()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/command_back',methods=['POST'])
def _comm_received():
    print('receied command from commDevice!')

@app.route('/signin',methods=['POST'])
def _ver_received():
    print('receied command from commDevice!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

