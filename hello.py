from flask import Flask, render_template
import RPi. GPIO as GPIO
import datetime
from time import sleep
import time
import serial
#import pymysql

ser = serial.Serial('/dev/ttyACM0', 115200)

#servo moter sensor
#servo moter 90 reset
#angle = 90
#duty = float(angle) / 10.0 + 2.5
#p.ChangeDutyCycle(duty)
#time.sleep(1)
#sound left, right
soundL = 0
soundR = 0

app = Flask(__name__)
@app.route("/")
@app.route("/main")
def hello():
    '''
    try:
        dataVal = ser.read(ser.inWaiting())
        print dataVal 
        value = dataVal.split(' ')         
        lightString = value[0]
        shockString = value[1]
        soundString = value[2]
        dustString = value[3]                         
        
    except (OSError, serial.serialutil.SerialException):
        lightString = '1'
        shockString = '2'
        soundString = '3'
        dustString = '4'
    '''
    
    time.sleep(6)
    dataVal = ser.readline()
    print (dataVal)
    value = dataVal.split(' ')         
    lightString = value[0]
    shockString = value[1]
    soundString = value[2]
    dustString = value[3]                         

    templateData = {
        'light':lightString,
        'shock':shockString,
        'sound':soundString,
        'dust':dustString
    }
    
    return render_template('main.html',**templateData)
    
    
    '''
    if ser.readable():
    dataVal = ser.readline()
    print dataVal 
                 
        value = dataVal.split(' ')         
        lightString = value[0]
        shockString = value[1]
        soundString = value[2]
        dustString = value[3]
    
    else :
        lightString = '1'
        shockString = '2'
        soundString = '3'
        dustString = '4'
    
    return render_template('main.html',
                           light=lightString,
                           shock=shockString,
                           sound=soundString,
                           dust=dustString)
    '''
#cctv
@app.route("/cctv.html")
def cctv():

    return render_template('cctv.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)