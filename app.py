from flask import Flask, request, send_from_directory, render_template
from sqlalchemy.exc import IntegrityError
# from model import Session, Produto

app = Flask(__name__)

@app.route('/')
def hello_world():
  # session = Session()
  return render_template("app.html"), 200

if __name__ == '__main__':
  app.run(debug=True)


