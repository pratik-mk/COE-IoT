from flask import Flask, render_template
from datetime import datetime
import qr_flask 


app = Flask(__name__)

@app.route('/')
def hello_world():
	now = datetime.now()
	d1 = now.strftime("%d-%m-%Y")
	t1 = now.strftime("%H:%M:%S")
	w1 = qr_flask.weight()
	return render_template('index.html',dt = d1, t1=t1, w1=w1)
