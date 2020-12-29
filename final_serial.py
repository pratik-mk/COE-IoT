import serial
import time
import csv
from datetime import date

today = date.today()
 
ser = serial.Serial('COM4', 38400)
ser.flushInput()

          #  writer.writerow([time.strftime("%H : %M : %S"),decoded_bytes])
           # writer.writerow([today.strftime("%d/%m/%Y"),decoded_bytes])
 
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
            
          
    except:
        print("Keyboard Interrupt")
        break
