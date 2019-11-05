import spidev, time

spi = spidev.SpiDev()

spi.open(0,0)



def analog_read(channel):

	buff = spi.xfer2([1, (8 + channel) << 4, 0])

	adc_out = ((buff[1]&3) << 8) + buff[2]

	return adc_out


while True:

	reading = analog_read(2)

	print("Reading=%d" % (reading))

	time.sleep(1)

