from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
import psycopg2

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:grespost@localhost:5432/daproj"
db = SQLAlchemy(app)

class Details(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.string(50))
    emailid = db.Column(db.string(100),unique = True,nullable = False)
    password = db.Column(db.string(100),nullable = False)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/home',methods = ['GET','POST'])
# @login_required
def home():
    return render_template('home.html')

@app.route('/about',methods = ['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/sales',methods = ['GET','POST'])
def sales():
    return render_template('sales.html')

@app.route('/Visuals',methods = ['GET','POST'])
def Visuals():
    return "Here come's the Visuals"

@app.route('/Analysis',methods = ['GET','POST'])
def Analysis():
    return "Here come's the Analysis"

@app.route('/ARM',methods = ['GET','POST'])
def ARM():
    return render_template('apriori_analysis.html')

@app.route('/customer',methods = ['GET','POST'])
def customer():
    return render_template('customer.html')

@app.route('/customer_segment',methods = ['GET','POST'])
def customer_segmentation():
    return render_template('segmentation.html')




if __name__ == "__main__":
    app.run(debug=True)