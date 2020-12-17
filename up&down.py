import time
import threading
import serial
from PCA9685 import PCA9685
import MotorDriver
from time import ctime

print("start")

pwm = PCA9685(0x40)
pwm.setPWMFreq(50)

Pos0 = 1500
Pos1 = 1500

Step0 = 0
Step1 = 0

pwm.setServoPulse(0, Pos0)
pwm.setServoPulse(1, Pos1)

s = serial.Serial("/dev/ttyUSB0", 115200)
time.sleep(5)


def handle():
    global Step0, Step1
    while True:
        data = s.read(1)
        data = data.decode('utf-8')
        data = str(data)
        print(data)
        if data == "0":
            (Step0, Step1) = (-5, 5)
            print("up")
        elif data == "1":
            (Step0, Step1) = (5, -5)
            print("down")


def timerfunc():
    global Step0, Step1, Pos0, Pos1, pwm

    if (Step0 != 0):
        Pos0 += Step0
        if (Pos0 >= 2500):
            Pos0 = 2500
        if (Pos0 <= 500):
            Pos0 = 500
        # set channel 0
        pwm.setServoPulse(0, Pos0)

    if (Step1 != 0):
        Pos1 += Step1
        if (Pos1 >= 2500):
            Pos1 = 2500
        if (Pos1 <= 500):
            Pos1 = 500
        # set channel 1
        pwm.setServoPulse(1, Pos1)
    global t  # Notice: use global variable!
    t = threading.Timer(0.02, timerfunc)
    t.start()


t = threading.Timer(0.02, timerfunc)
t.setDaemon(True)
t.start()

handle()
timerfunc()
print('running....')