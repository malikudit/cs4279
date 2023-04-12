
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import subprocess
import os
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    global hello
    if request.method == 'POST':
        video = request.files['video']
        video.save('static/' + video.filename)
        hello = 'static/' + video.filename
        return redirect(url_for('output', hello=hello))
    return render_template('index.html')

def run_process():
    process = subprocess.Popen(["build/src/DarkPlate", hello], stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT, text=True)
    skip_count = 0
    while True:
        out = process.stdout.readline()
        if out == '' and process.poll() is not None:
            break
        if out:
            if "-> frame" in out:
                socketio.emit('output', {'data': out.strip()})
                skip_count = 8
            elif skip_count == 0:
                socketio.emit('output', {'data': out.strip()})
                skip_count = 8
            else:
                skip_count -= 1



@app.route('/output')
def output():
    return render_template('output.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')
    thread = threading.Thread(target=run_process)
    thread.start()

if __name__ == '__main__':
    socketio.run(app)


