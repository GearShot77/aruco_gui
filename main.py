from tkinter import *
from tkinter.ttk import Combobox  
from tkinter import messagebox  
import os
import rospy
import time
from std_msgs.msg import String



def callback(data):
    time.sleep(1)
    rospy.loginfo("Aruco-simple/pose",data.data)

def subscriber():
    rospy.init_node('Aruco-simple/pose')
    rospy.Subscriber("Aruco-simple/pose", String, callback)

    rospy.spin()

def btnclick1():
  os.system ("rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.02517 image:=/usb_cam/image_raw camera:=/usb_cam --no-service-check")

def btnklick2():
  os.system("roslaunch aruco_marker_finder.launch markerId:=701 markerSize:=0.05")
  messagebox.showinfo('Info', 'поиск запущен') 

def btnklick3():
  os.system("roslaunch aruco_marker_finder.launch markerId:=47,13,36 markerSize:=0.05")
  messagebox.showinfo('Info', 'поиск запущен')
def btnklick4():
  os.system("roslaunch aruco_marker_finder.launch markerId:=701 markerSize:=0.05")
  messagebox.showinfo('Info', 'поиск запущен')

def btnklick5():
  os.system("cd /tmp/ ")
  time.sleep(2)
  os.system("mv calibrationdata.tar.gz /.ros/camera....")   # 
  time.sleep(2)
  os.system("tar -xvf calibration.tar.gz")
  time.sleep(5)
  os.system ("mv ost.yaml camera_head.yaml" )
  messagebox.showinfo('Info', 'файл успешно записан')

def btnklick7():
   messagebox.showinfo('Info', rospy.Subscriber("Aruco-simple/pose", String, callback) )




window = Tk()
window.title("Aruco_gui")
window.geometry('2000x1000')

canvas = Canvas(window, width=800, height=600)
canvas.pack()
table_obj = PhotoImage(file="/home/qwer/Downloads/table20232.png")
#canvas.create_image (column=5,row = 1,anchor=NW,image=table_obj)
canvas.grid(column=1, row=70)

lbl = Label(window, text="выбирите сторону")
lbl.grid(column=0, row=0)

combo = Combobox(window) 
combo['values'] = ("green","blue")   
combo.current()   
combo.grid(column=0, row=1)

btn = Button(window, text="Calibrate_camera", command=btnclick1)
btn.grid(column=1, row=1)

btn = Button(window, text=" запись калибровочного файла", command=btnklick5)  
btn.grid(column=1, row=20)

btn = Button(window, text="Поиск только роботов ", command=btnklick2)  # aruco №
btn.grid(column=1, row=30)

btn = Button(window, text="Поиск только Коржей ", command=btnklick3) #aruco № 47 (glazur) 13 (krem) 36 (biscuit)
btn.grid(column=1, row=40)

btn = Button(window, text=" Совмещенный поиск ", command=btnklick4)  
btn.grid(column=1, row=50)


btn = Button(window, text=" aruco_pose ", command=btnklick7)  
btn.grid(column=1, row=60)

our_image = PhotoImage(file='/home/qwer/Downloads/table20232.png')
our_image = our_image.subsample (1,1)
our_label = Label(window)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place ( x = 50 , y = 50)


window.mainloop()

