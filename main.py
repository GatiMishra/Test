from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, Jagadeesh!'

from app import route

if __name__ == '__main__':
  app.run()
