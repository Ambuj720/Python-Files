from db import ParkingSpace
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

app.secret_key = "ajksdaksj"

def opendb():
    engine=create_engine("sqlite:///Carpark.sqlite",echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/startparking')
def about():
    return render_template('startparking.html')

@app.route('/uploadImg')
def contact_us():
    return render_template('uploadImg.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)