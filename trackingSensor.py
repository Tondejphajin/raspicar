import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class trackingSensor():
    def __init__(self, trackerPin):
        self.trackerPin = trackerPin
        GPIO.setup(self.trackerPin, GPIO.IN)

    def terminated(self):
        GPIO.cleanup()

if __name__ == '__main__':
    trackerA = trackingSensor(20)
    trackerB = trackingSensor(21)
    while True:
        print(GPIO.input(trackerA.trackerPin))
        print(GPIO.input(trackerB.trackerPin))
        sleep(0.2)