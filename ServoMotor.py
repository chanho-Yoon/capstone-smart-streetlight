import RPi. GPIO as GPIO
from time import sleep
import time

print "Servo Motor";

'''servo moter sensor'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(26,100)
p.start(5)
''' sound sensor '''
soundpin=0
GPIO.setup(soundpin, GPIO.IN)


'''servo moter 90 reset'''
angle = 90
duty = float(angle) / 10.0 + 2.5
p.ChangeDutyCycle(duty)
time.sleep(1)


try:

	while True:
		'''
		angle = raw_input("Enter Angle ( 0 to 180 ): ")
		duty = float(angle) / 10.0 + 2.5
		p.ChangeDutyCycle(duty)
		time.sleep(2)
		'''
		soundlevel = GPIO.input(soundpin)
		print "soundlevel : " , soundlevel
     		#print "soundlevel first!",soundlevel

     		sleep(0.2)
		if soundlevel == 1 :  
			
			angle = 40
                	duty = float(angle) / 10.0 + 2.5
                	p.ChangeDutyCycle(duty)
                	time.sleep(0.2)
			
			print "1111111111111 ---- " , soundlevel

		elif soundlevel == 0 :
			angle = 150
                        duty = float(angle) / 10.0 + 2.5
                        p.ChangeDutyCycle(duty)
			time.sleep(0.2)

			print "0000000000000 ---- " , soundlevel

except KeyboardInterrupt:
	print "GPIO.cleanp()"
	GPIO.cleanup()
