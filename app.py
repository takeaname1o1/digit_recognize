from flask import Flask

# The Flask application object
app = Flask(__name__)

# Your routes and other application logic go here
@app.route('/')
def hello_world():
    return 'Hello, from your Digit Recognizer!'

# This part is for local development and won't be used by Gunicorn
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
