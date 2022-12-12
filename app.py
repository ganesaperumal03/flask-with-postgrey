from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost/ganesh'

db=SQLAlchemy(app)

class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(40))
  age=db.Column(db.String(40))
  contact=db.Column(db.String(40))
  mail=db.Column(db.String(40))
  department=db.Column(db.String(40))
  Reg_no=db.Column(db.String(40))
  CPGA=db.Column(db.String(40))


  def __init__(self,name,age,contact,mail,department,Reg_no,CPGA):
    self.name=name
    self.age=age
    self.contact=contact
    self.mail=mail
    self.department=department
    self.Reg_no=Reg_no
    self.CPGA=CPGA


@app.route('/')
def welcome():
    return redirect('/login')


@app.route('/home')
def home():
     return render_template("register.html")


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'ganesh':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route("/Register",methods=["POST","GET"])

def Register():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        contact = request.form.get('contact')
        mail = request.form.get('mail')
        department=request.form.get('department')
        Reg_no=request.form.get('Reg_no')
        CPGA=request.form.get('CPGA')
        student=Student(name,age,contact,mail,department,Reg_no,CPGA)
        db.session.add(student)
        db.session.commit()

        studentResult=db.session.query(Student).filter(Student.id==1)
        for result in studentResult:
            print(result.name)

        return render_template('result.html', data=name)
if __name__ =='__main__':
    app.run(debug=True)

