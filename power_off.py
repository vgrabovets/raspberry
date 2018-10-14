import time
from subprocess import call

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(17, True)

while True:
    input_state = GPIO.input(18)

    if input_state == False:
	call('sudo shutdown -h now', shell=True)
