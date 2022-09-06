#=================importing files
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
from tkinter import messagebox




##================ creating a das as a main frame ============
das=tk.Tk()
das.title("----------------")
das.geometry('1920x1080+0+0')


login_btn = PhotoImage(file = "C:/Users/salvi/Desktop/ic work/start.png")
exit_btn = PhotoImage(file = "C:/Users/salvi/Desktop/ic work/exit.png")


side_f1 = Frame(das,bg='#FFF',width=400,height=880 )
side_f1.pack(side=LEFT)

box1 = Frame(side_f1, bg="#113A5D",width=300,height =210)
box1.pack(side=TOP ,padx=20,pady =54)

img = Button(box1,bg="#113A5D",image = login_btn,borderwidth = 0)
img.pack(side=TOP,padx=80,pady=80)

logo = Frame(side_f1, bg="#EEE",width=100,height =100)
logo.pack(padx=30,pady =20)

box2 = Frame(side_f1, bg="#113A5D",width=300,height =210)
box2.pack(side=BOTTOM ,padx=20,pady =54)

img2 = Button(box2,bg="#113A5D",image = exit_btn,borderwidth = 0)
img2.pack(side=BOTTOM,padx=80,pady=80)

side_f2 = tk.Text(das,bg='#FFF',width=400,height=880 )
side_f2.pack(side=RIGHT)


inputtxt = tk.Text(side_f2,height = 10,width = 10,bg='#113A5D')
inputtxt.pack()

text_area =Frame(side_f2,bg='#113A5D',width=350,height=800 )
text_area.pack(fill = BOTH , expand=True,padx =25,pady=25)




main= Frame(das,bg='#113A5D',width=1120,height=880 )
main.pack(side=TOP)

camera = Frame(main,bg='#FFF',width=1020,height=1000)
camera.pack(fill= BOTH, expand= True, padx= 50, pady=50)














