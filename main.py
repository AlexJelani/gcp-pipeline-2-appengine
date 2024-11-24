from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(): 
    return 'Welcome to Python Flask World v2.0 from ci/cd pipeline'

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8080)



