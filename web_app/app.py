from flask import Flask, render_template, request, redirect
from datetime import datetime
import serial

# QR code generation
import pyqrcode 
import png 
from pyqrcode import QRCode
from PIL import Image




app = Flask(__name__)

@app.before_first_request
def setuparduino():
	global ser
	ser = serial.Serial('COM19', 9600)

@app.route('/')
def hello_world():
	now = datetime.now()
	d1 = now.strftime("%d-%m-%Y")
	t1 = now.strftime("%H:%M:%S")
	ser_bytes = ser.readline()
	decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
	data=str([d1,t1,decoded_bytes])
	
	# Generate QR code
	url = pyqrcode.create(data)
	# Create and save the svg file naming "myqr.svg" 
	url.png("static/qrcode.png", scale = 8)

	return render_template('index.html',dt = d1, t1=t1, w1=decoded_bytes)
