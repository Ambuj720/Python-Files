from unicodedata import category
from database import Question
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

app.secret_key = "ajksdaksj"

def opendb():
    engine=create_engine("sqlite:///Database.sqlite",echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        qs=request.form.get('qs')
        op1=request.form.get('op1')
        op2=request.form.get('op2')
        op3=request.form.get('op3')
        op4=request.form.get('op4')
        cat=request.form.get('category')
        ans=request.form.get('ans')
        if not qs and len(qs)<10:
                flash('Question is required and at least 10 characters long', 'danger')
                return redirect('/')
        elif not op1 or len (op1) < 3:
                flash('Option','')
                return redirect('/')
                return render_template('index.html')
        elif not op2 or len (op2) < 3:
                flash('Option','')
                return redirect('/')
                return render_template('index.html')
        elif not op3 or len (op3) < 3:
                flash('Option','')
                return redirect('/')
                return render_template('index.html')
        elif not op4 or len (op4) < 3:
                flash('Option','')
                return redirect('/')

        else:
            db = opendb()
            q = Question(title=qs, op1=op1, op2=op2, op3=op3, op4=op4, ans=ans, category=cat)
            db.add(q)
            db.commit()
            db.close()
            flash('Question added successfully', 'success')
            return redirect('/')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact_us():
    return render_template('contact.html')
 

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

