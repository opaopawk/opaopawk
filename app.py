import os
os.system('python ox.py')
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'curl '

if __name__ == '__main__':
    app.run()
