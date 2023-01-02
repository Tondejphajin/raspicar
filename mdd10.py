import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
from servo import Servo

class Motor():
    def __init__(self,AN1=12,AN2=13,DIG1=24,DIG2=26):
        self.AN1 = AN1
        self.AN2 = AN2
        self.DIG1 = DIG1
        self.DIG2 = DIG2
        GPIO.setup(AN1, GPIO.OUT)
        GPIO.setup(AN2, GPIO.OUT)
        GPIO.setup(DIG1, GPIO.OUT)
        GPIO.setup(DIG2, GPIO.OUT)
        self.p1 = GPIO.PWM(self.AN1, 100)
        self.p1.start(0)
        self.p2 = GPIO.PWM(self.AN2,100)
        self.p2.start(0)
        self.servo = Servo()

    def forward_left(self,speed=50,t=0):
        GPIO.output(self.DIG1, GPIO.LOW)
        GPIO.output(self.DIG2, GPIO.LOW)
        self.p1.start(speed)
        self.p2.start(speed)
        self.servo.turnLeft()
        sleep(t)

    def backward_left(self,speed=50,t=0):
        GPIO.output(self.DIG1, GPIO.HIGH)
        GPIO.output(self.DIG2, GPIO.HIGH)
        self.p1.start(speed)
        self.p2.start(speed)
        self.servo.turnLeft()
        sleep(t)

    def stop(self,t=0):
        GPIO.output(self.DIG1, GPIO.LOW)
        GPIO.output(self.DIG2, GPIO.LOW)
        self.p1.start(0)
        self.p2.start(0)
        sleep(t)

    def forward(self,speed=50,t=0):
        GPIO.output(self.DIG1, GPIO.LOW)
        GPIO.output(self.DIG2, GPIO.LOW)
        self.p1.start(speed)
        self.p2.start(speed)
        self.servo.reset()
        sleep(t)

    def forward_right(self,speed=50,t=0):
        GPIO.output(self.DIG1, GPIO.LOW)
        GPIO.output(self.DIG2, GPIO.LOW)
        self.p1.start(speed)
        self.p2.start(speed)
        self.servo.turnRight()
        sleep(t)

    def backward_right(self,speed=50,t=0):
        GPIO.output(self.DIG1, GPIO.HIGH)
        GPIO.output(self.DIG2, GPIO.HIGH)
        self.p1.start(speed)
        self.p2.start(speed)
        self.servo.turnRight()
        sleep(t)

    def backward(self,speed=50,t=0):
        GPIO.output(self.DIG1, GPIO.HIGH)
        GPIO.output(self.DIG2, GPIO.HIGH)
        self.p1.start(speed)
        self.p2.start(speed)
        self.servo.reset()
        sleep(t)

    def terminated(self):
        GPIO.cleanup()

if __name__ == '__main__':
    motor = Motor()
    motor.terminated()
    print('DONE')