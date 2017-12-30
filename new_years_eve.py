#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import music_scale

BuzzerPin = 10    # pin10

SPEED = 1

# Song is a list of tones with name and 1/duration. 16 means 1/16
SONG =	[
	["a4",4],
	["e5",16],["eb5",16],
	["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
	["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
	["b4",8],["p",16],["e4",16],["ab4",16],["b4",16],
	["c5",8],["p",16],["e4",16],["e5",16],["eb5",16],
	["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
	["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
	["b4",8],["p",16],["e4",16],["c5",16],["b4",16],["a4",4]
	]

def setup():
	GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
	GPIO.setup(BuzzerPin, GPIO.OUT)

def play_note=(player, frequency, duration):
	if frequency == 'p': # p => pause
		time.sleep(duration)
	else:
		player.ChangeFrequency(frequency)
		player.start(duration)
		time.sleep(duration)
		p.stop()

def run():
	music = map(frequency_and_duration(SONG))
	first_note_played = false
	player = false

	for note in SONG:
		if first_note_played
			play_note(player, note['frequency'], note['duration'])
		else
			player = GPIO.PWM(BuzzerPin, note['frequency'])
			player.start(note['duration'])


def frequency_and_duration(note_and_duration):
	return {
		'frequency': music_scale.note_to_frequency(note_and_duration[0])
		'duration': duration(note_and_duration[1])
	}

def duration(denominator):
	return (1./(denominator*0.25*SPEED))

def destroy():
	GPIO.output(BuzzerPin, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		run()
        GPIO.cleanup()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
