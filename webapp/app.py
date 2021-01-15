from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import serial

# QR code generation
import pyqrcode 
import png 
from pyqrcode import QRCode
from PIL import Image




app = Flask(__name__)

# inital port configuration
@app.before_first_request
def setuparduino():
	global ser
	ser = serial.Serial('COM19', 9600)


@app.route('/')
def home():
	now = datetime.now()
	d1 = now.strftime("%d-%m-%Y")
	t1 = now.strftime("%H:%M:%S")
	# exception handling for port not found
	try:
		ser_bytes = ser.readline()
		decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
	except:
		return redirect(url_for('portexception'))

	data=str([d1,t1,decoded_bytes])
	
	# Generate QR code
	url = pyqrcode.create(data)
	# Create and save the svg file naming "myqr.svg" 
	url.png("static/qrcode.png", scale = 8)


	return render_template('index.html',dt = d1, t1=t1, w1=decoded_bytes, qrpath = '/static/qrcode.png')

@app.route('/portexception')
def portexception():
	return render_template('portexception.html')