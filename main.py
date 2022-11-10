from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def Score():
   with open("/app/Score1.txt", "r") as f:
      content = f.read()
      return render_template("Score1.html", content=content)

@app.route('/a')
def hello_world():
        return 'Hello I am a Flaskk Application'


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
