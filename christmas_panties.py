#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

colors = [
  {'r': 100, 'g': 100, 'b': 100 },
  {'r': 100, 'g': 0, 'b': 100 },
  {'r': 100, 'g': 100, 'b': 0 },
  {'r': 0, 'g': 100, 'b': 100 },
  {'r': 50, 'g': 0, 'b': 0 },
  {'r': 0, 'g': 50, 'b': 0 },
  {'r': 0, 'g': 0, 'b': 50 },
  {'r': 50, 'g': 50, 'b': 50 },

]
# colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
pins = {'pin_r':10, 'pin_g':11, 'pin_b':12}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
	GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
	GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

p_r = GPIO.PWM(pins['pin_r'], 2000)  # set Frequece to 2KHz
p_g = GPIO.PWM(pins['pin_g'], 2000)
p_b = GPIO.PWM(pins['pin_b'], 5000)

p_r.start(0)      # Initial duty Cycle = 0(leds off)
p_g.start(0)
p_b.start(0)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
	r_val = col['r']
	g_val = col['g']
	b_val = col['b']

	rgb_sum = float(r_val + g_val + b_val)
        multiplier = 1
        
	if rgb_sum == 0:
            # do nothing bc divide by 0 is fail
            # print("sum " + str(rgb_sum) + " is 0")
            multiplier = 1
	elif rgb_sum == 100:
            # do nothing bc it is already normal
            # print("sum " + str(rgb_sum) + " is 100")
            multiplier = 1
	else:
            # print("sum " + str(rgb_sum) + " is not 0 or 100")
            # example 200 * (100 / 200) = 100
            # example 50 * (100 / 50) = 100
            multiplier = 100 / rgb_sum
	
	adjusted_r_val = r_val * multiplier
	adjusted_g_val = g_val * multiplier
	adjusted_b_val = b_val * multiplier
	
	p_r.ChangeDutyCycle(adjusted_r_val)     # Change duty cycle
	p_g.ChangeDutyCycle(adjusted_g_val)
	p_b.ChangeDutyCycle(adjusted_b_val)
        print(
          "starting total: " + str(rgb_sum) + " multiplier: " + str(multiplier) + 
          " adjusting r: " + str(r_val) + " to: " + str(adjusted_r_val) +
          " adjusting g: " + str(g_val) + " to: " + str(adjusted_g_val) +
          " adjusting b: " + str(b_val) + " to: " + str(adjusted_b_val)
        )

try:
	while True:
		for col in colors:
			setColor(col)
			time.sleep(1.5)
except KeyboardInterrupt:
	p_r.stop()
	p_g.stop()
	p_b.stop()
	for i in pins:
		GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
	GPIO.cleanup()
