from ultrasonicSensor import ultraSonicSensor
from mdd10 import Motor
import keyboardControl as kc

sensorA = ultraSonicSensor("A",18,22)
sensorB = ultraSonicSensor("B",15,23)
sensorC = ultraSonicSensor("C",14,25)
motor = Motor()
kc.init()

def keyboardControl():
    global setGear
    if kc.getKey('d'):
        setGear = True
        print(f'setGear={setGear}: Drive Gear is Activated')
    elif kc.getKey('r'):
        setGear = False
        print('setGear={setGear}: Reverse Gear is Activated')
    elif kc.getKey('e'):
        motor.stop()
        motor.terminated()
        print('All GPIO is clean up')
    elif kc.getKey('UP'):
        motor.forward(50,0.1)
    elif kc.getKey('DOWN'):
        motor.backward(50,0.1)
    elif kc.getKey('LEFT'):
        if setGear == True:
            motor.forward_left(50,0.1)
            print("forwardLeft")
        if setGear == False:
            motor.backward_left(50,0.1)
            print("backwardLeft")
        print('Turning left')
    elif kc.getKey('RIGHT'):
        if setGear == True:
            motor.forward_right(50,0.1)
            print("forwardRight")
        if setGear == False:
            motor.backward_right(50,0.1)
            print("backwardRight")
    else:
        motor.stop()

setGear = None
while True:
    if kc.getKey('k'):
        motor.stop()
        print('Keyboard control is activated')
        while True:
            keyboardControl()
            if kc.getKey('o'):
                print('Keyboard control is terminated')
                break
    if kc.getKey('a'):
        print('Autodrive mode is activated')
        motor.forward()
        while True:
            if sensorA.distance() <= 30 or sensorB.distance() <= 30 or sensorC.distance() <= 30:
                if sensorA.distance() <= 30:
                    motor.forward_right()
                if sensorB.distance() <= 30:
                    motor.backward()
                if sensorC.distance() <= 30:
                    motor.forward_left()

