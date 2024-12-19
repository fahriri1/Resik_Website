from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/control', methods=['POST'])
def control():
    command = request.json.get('command')
    print(f"Received command: {command}")
    # Add logic to forward the command to the ESP-01
    response = requests.post("http://192.168.227.229:80/control", json={'command': command})
    return {'status': 'Command received', 'command': command}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)