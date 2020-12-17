#-*- coding: utf-8 -*
import tkinter as tk
from tkinter.simpledialog import askstring, askinteger, askfloat
import serial
try:
    portx="COM3"
    bps=115200
    timex=5
    ser=serial.Serial(portx,bps,timeout=timex)
except Exception as e:
    print("---异常---：",e)


def command_up():
    ser.write("0".encode("gbk"))
def command_down():
    ser.write("1".encode("gbk"))
def command_forward():
    ser.write("MF100F100".encode("gbk"))
def command_backward():
    ser.write("MB100B100".encode("gbk"))
def command_left():
    ser.write("MB100F100".encode("gbk"))
def command_right():
    ser.write("MF100B100".encode("gbk"))
def command_stop():
    ser.write("MF000F000".encode("gbk"))
# def command_auto():
#     ser.write("5".encode("gbk"))

root = tk.Tk()
l = tk.Label(root, width=10, height=1, text=" ")


connection_status = tk.StringVar()
l = tk.Label(root, textvariable=connection_status)
l.pack()

botton_frame = tk.Frame(root)
botton_frame.pack()
botton_up = tk.Button(botton_frame, text='上升', font=('黑体', 20), width=30, height=2, command=command_up)
botton_close = tk.Button(botton_frame, text='下降', font=('黑体', 20), width=30, height=2, command=command_down)

botton_up.pack(side="left")
botton_close.pack(side="left")
l = tk.Label(root, width=10, height=1, text=" ")
l.pack()

botton_up.pack(side="left")
botton_close.pack(side="left")
l = tk.Label(root, width=10, height=1, text=" ")
l.pack()
arrow_frame = tk.Frame(root)
arrow_frame.pack()
arrow_frame0 = tk.Frame(arrow_frame)
arrow_frame1 = tk.Frame(arrow_frame)
arrow_frame2 = tk.Frame(arrow_frame)
arrow_frame0.pack(side="left")
arrow_frame1.pack(side="left")
arrow_frame2.pack(side="right")
img_left = tk.PhotoImage(file='left.png')
arrow_left = tk.Button(arrow_frame0, image=img_left, width = 120,height=120, command=command_left).pack(side="left")
img_up = tk.PhotoImage(file='up.png')
arrow_up = tk.Button(arrow_frame1, image=img_up,width = 120,height=120,  command=command_forward).pack()
img_stop = tk.PhotoImage(file='stop.png')
arrow_stop = tk.Button(arrow_frame1, image=img_stop,width = 120,height=120,  command=command_stop).pack()
img_down = tk.PhotoImage(file='down.png')
arrow_dowm = tk.Button(arrow_frame1, image=img_down,width = 120,height=120,  command=command_backward).pack()
img_right = tk.PhotoImage(file='right.png')
arrow_right = tk.Button(arrow_frame2, image=img_right,width = 120,height=120,  command=command_right).pack(side="right")

l = tk.Label(root, width=10, height=1, text=" ")
l.pack()

# 进入消息循环
root.mainloop()