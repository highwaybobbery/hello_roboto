#!/usr/bin/env python
import ADC0832
import time

def init():
	ADC0832.setup()

def loop():
	while True:
		raw_res = ADC0832.getResult()
		res = raw_res - 80
		if res < 0:
			res = 0
		if res > 100:
			res = 100
		print 'raw_res = %d res = %d' % (raw_res, res)
		time.sleep(0.2)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
