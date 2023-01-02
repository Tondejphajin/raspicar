import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class Servo():
    def __init__(self,pin=17):
        GPIO.setup(pin, GPIO.OUT)
        self.servo1 = GPIO.PWM(pin, 50)
        self.servo1.start(0)
        time.sleep(1)

    def turnLeft(self,duty=2.2,t=0):
        self.servo1.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.servo1.ChangeDutyCycle(0)
        time.sleep(t)

    def turnRight(self,duty=5,t=0):
        self.servo1.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.servo1.ChangeDutyCycle(0)
        time.sleep(t)

    def reset(self):
        self.servo1.ChangeDutyCycle(3.6)
        time.sleep(0.5)
        self.servo1.ChangeDutyCycle(0)

    def cleanup(self):
        self.servo1.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    servo = Servo()
    servo.reset()
    servo.turnLeft()
    servo.reset()
    servo.turnRight()
    servo.reset()
    servo.cleanup()
    print("done")