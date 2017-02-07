from flask import *
import psutil
#App Config
app = Flask(__name__)

app.debug = True

#Routes
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/full')
def full():
	return render_template('main.html')
@app.route('/load')
def load():
#Docs: https://pypi.python.org/pypi/psutil
	cpu= psutil.cpu_percent()
	memory= psutil.virtual_memory()
	mem=memory.percent
	return "CPU: {} Memory: {}".format(cpu,mem)
#HTTP Error Messages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 

@app.errorhandler(403)
def unauthaurized_request(e):
    return render_template('403.html'), 403
#Run App
if __name__ == "__main__":
	app.run(host = '0.0.0.0')
