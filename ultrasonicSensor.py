import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class ultraSonicSensor():
    def __init__(self,sensorName,trigger,echo):
        self.sensorName = sensorName
        self.GPIO_TRIGGER = trigger
        self.GPIO_ECHO = echo
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance(self):
        GPIO.output(self.GPIO_TRIGGER,True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER,False)
        startTime = time.time()
        stopTime = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            startTime = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            stopTime = time.time()

        timeElapsed = stopTime - startTime
        distance = (timeElapsed*sonicSpeed) / 2
        print(f'Sensor{self.sensorName}: Measured Distance = {distance}')
        return distance

def calSonicSpeed():
    temp = int(input("Enter the current room temp in Calcuis: "))
    sonic_speed = 33145*math.sqrt((temp+273.15)/273.15)
    print(f'sonic speed = {sonic_speed}')
    return sonic_speed

sonicSpeed = calSonicSpeed()

if __name__ == '__main__':
    sensorA = ultraSonicSensor("A",18,22)
    sensorB = ultraSonicSensor("B",15,23)
    sensorC = ultraSonicSensor("C",14,25)
    while True:
        sensorA.distance()
        sensorB.distance()
        sensorC.distance()
        time.sleep(1)