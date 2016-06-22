from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import psutil
app = Flask(__name__)

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://aditya:Bangalore12E@localhost/flask'
class User(db.Model):
	uid = db.Column(db.Integer, primary_key= True)
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String(20), unique= True)

	def __init__(self,username, password):
		self.username = username
		self.password = password

@app.route('/')
def index():
	return render_template('403.html')
@app.route('/full')
def full():
	return render_template('main.html')
@app.route('/load')
def load():
	cpu= psutil.cpu_percent()
	memory= psutil.virtual_memory()
	mem=memory.percent
	return "CPU: {} Memory: {}".format(cpu,mem)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403
if __name__ == "__main__":
	app.run()