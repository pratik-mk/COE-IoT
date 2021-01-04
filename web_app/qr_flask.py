import serial
import time
import csv
from datetime import date

# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode

from PIL import Image
  


def weight():
    try:
        today = date.today()
        ser = serial.Serial('COM4', 38400)
        ser.flushInput()
    except:
        print("Port Not Found/Connected")

    while True:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
            with open("output.csv","a", newline='') as f:
                writer = csv.writer(f,delimiter=",")
                t1=time.strftime("%H : %M : %S")
                d1=today.strftime("%d/%m/%Y")
                writer.writerow([d1,t1,decoded_bytes])
                
                data=str([d1,t1,decoded_bytes])
                print(data)
                # Generate QR code 
                url = pyqrcode.create(data) 
      
                # Create and save the svg file naming "myqr.svg" 
                url.png("/static/myqr.png", scale = 8) 
        except:
            print("Keyboard Interrupt")
            decoded_bytes = None
            break
    return decoded_bytes
                
              
        