import time
import serial
import threading
from PCA9685 import PCA9685
from time import ctime

print("start")

pwm = PCA9685(0x40)
pwm.setPWMFreq(50)

Pos0 = 1500
Pos1 = 1500

Step0 = 0
Step1 = 0
Ret0 = 0

pwm.setServoPulse(0, Pos0)
pwm.setServoPulse(1, Pos1)

# s = serial.Serial("/dev/ttyUSB0", 115200)
# time.sleep(0.01)

class Servo:
    def timerfunc(self):
        global Step0 , Step1 , Pos0 , Pos1 , pwm
        while True:
            if (Ret0 == 0):
                if (Step0 != 0):
                    Pos0 += Step0
                    if(Pos0 >= 1800):
                        Pos0 = 1800
                    if(Pos0 <= 1200):
                        Pos0 = 1200
                    pwm.setServoPulse(0,Pos0)

                if (Step1 != 0):
                    Pos1 += Step1
                    if(Pos1 >= 1800):
                        Pos1 = 1800
                    if(Pos1 <= 1200):
                        Pos1 = 1200
                    pwm.setServoPulse(1,Pos1)
            elif (Ret0 == 1):
                pwm.setServoPulse(0,1500)
                pwm.setServoPulse(1,1500)

    def adjust(self, head_command):
        global Step0, Step1, Ret0, pwm
        if head_command[0] in ['D', 'd']:
            pass
        else:
            return

        if head_command[1] in ['D', 'd']:
            Ret0 = 0
            (Step0,Step1) = (10,-10)
            print("down")
        elif head_command[1] in ['F', 'f']:
            Ret0 = 0
            (Step0,Step1) = (-10,10)
            print("up")
        elif head_command[1] in ['S', 's']:
            Ret0 = 1
            print("flat")
        else:
            return


# t = threading.Thread(target=timerfunc)
# t.setDaemon(True)
# t.start()

#def handle():
#    global Step0, Step1
# try:
#     while True:
#         data =s.read(1)
#         data = data.decode('utf-8')
#         data = str(data)
#         print(data)
#         if data == "DF000F000":
#             Ret0 = 0
#             (Step0,Step1) = (-10,10)
#             print("up")
#         if data == "DD000D000":
#             Ret0 = 0
#             (Step0,Step1) = (10,-10)
#             print("down")
#         if data== "DS000S000":
#             Ret0 = 1
#             print("flat")
#     time.sleep(0.0001)
# except KeyboardInterrupt:
#     if s!= None:
#         s.close()

