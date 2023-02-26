Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import messagebox
>>> GUI = Tk()
>>> GUI.title('เที่ยวทำเลไทยตามฤดูกาล')
''
>>> GUI.geometry('500x500')
''
>>> 
>>> def Button1():
...     text='ทะเลฝั่งอันดามัน ภูเก็ต กระบี่ พัทยา ชะอำ'
...     messagebox.showinfo('ทะเลที่เหมาะแก่การไปเที่ยว',text)
... 
...     
>>> def Button2():
...     text='ทะเลอ่าวไทย สมุย พงัน นางยวน'
...     messagebox.showinfo('ทะเลที่เหมาะแก่การไปเที่ยว',text)
... 
...     
>>> def Button3():
...     text='ทะเลฝั่งตะวันตก ชะอำ หีวหิน ประจวบ'
...     messagebox.showinfo('ทะเลที่เหมาะแก่การไปเที่ยว',text)
... 
...     
>>> B1=Button(text='มกราคม-กุมพาพันธ์',command=Button1)
>>> B1.place(x=20,y=20)
>>> B2=Button(text='มีนาคม-เมษายน',command=Button2)
B2.place(x=100,y=20)
>>> B2.pack()
>>> B2.place(x=300,y=20)
