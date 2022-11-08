import json
from flask import Flask, render_template
from flask_socketio import SocketIO, send

with open("./config.json","r") as configFile:
    config = json.load(configFile)

app = Flask(__name__)
app.config['SECRET'] = "secret123"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print("Received message: "+message)
    if message != "User connected!":
        send(message, broadcast= True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    socketio.run(app, host=config['hostIP'], port=config['port'])