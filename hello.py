from flask import Flask, render_template
import datetime
from time import sleep
import time
import serial


port = '/dev/ttyACM0'
cmd = 'temp'
ser = serial.Serial('/dev/ttyACM0', 9600)

print(ser.name)

app = Flask(__name__)

@app.route("/")
@app.route("/test")
def hello():
    a = 1
    while a:
        if ser.in_waiting != 0 :
            dataVal = ser.readline()
            dataVal = dataVal[:-2].decode()
            value = dataVal.split(',')
            print (value)
            lightString = value[0]
            ampString = value[1]
            shockString = value[2]
            soundString = value[3]
            dustString = value[4]
            
            templateData = {
            'light':lightString,
            'amp' : ampString,
            'shock':shockString,
            'sound':soundString,
            'dust':dustString
            }


            a = 0
        else :
            time.sleep(1)

    return render_template('test.html',**templateData)
    time.sleep(5)
    ser.close()
@app.route("/cctv.html")

def cctv():
    
        return render_template('/cctv.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    
    
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
    
#cctv
@app.route("/cctv.html")
def cctv():

    return render_template('cctv.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    '''