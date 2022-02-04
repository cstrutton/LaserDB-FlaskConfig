import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/restart')
def restart():
    ret = subprocess.run(['sudo', 'cat', '/etc/network/interfaces.d/eth0'], capture_output=True)
    return ret.stdout

@app.route('/who')
def who():
    ret = subprocess.run(['who'], capture_output=True)
    return ret.stdout


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
