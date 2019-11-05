import serial
ser = serial.Serial('/dev/ttyACM0',9600);

cnt = 1;

while 1 :
	dustVal = ser.readline();
	print dustVal;
	'''print "cnt" , cnt;'''

	cnt = cnt+1;
