#!/usr/bin/env python3
try:
    from flask import Flask
except:
    import os
    os.system("pip install flask")


from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
