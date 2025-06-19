import RPi.GPIO as GPIO

class ConveyorBelt:
    def __init__(self, pin=14):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.turn_off()

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def cleanup(self):
        self.turn_off()
        GPIO.cleanup(self.pin)
