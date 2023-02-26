Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import messagebox
>>> GUI = Tk()
>>> GUI.title('เที่ยวทะเลไทยตามฤดูกาล')
''
>>> GUI.geometry('500x500')
''
>>> def Button1():
...     text='ฝั่งอันดามัน ภูเก็ต กระบี่ พัทยา ชะอำ'
...     messagebox.showinfo('ทะเลที่เหมาะแก่การไปเที่ยว',text)
... 
...     
>>> def Button2():
...     text='ทะเลอ่าวไทย สมุย พงัน นางยวน'
...     messagebox.showinfo('ทะเลที่เหมาะแก่การไปเที่ยว',text)
... 
...     
>>> def Button3():
...     text='ฝั่งอันดามัน เกาะพีพี หมู่เกาะสุรินทร์ เกาะหลีเป๊ะ ตรัง'
...     messagebox.showinfo('ทะเลที่เหมาะแก่การไปเที่ยว',text)
... 
...     
>>> def Button4():
...     text='ได้ทั้งฝั่งอันดามันและฝั่งตะวันตก ชะอำ หัวหิน'
...     messagebox.showinfo('ทะเลที่เหมาะแก่การเที่ยว',text)
... 
...     
>>> B1 = Button(text='มกราคม-กุมพาพันธ์',command=Button1)
>>> B1.place(x=20,y=20)
>>> B2 = Button(text='มีนาคม-เมษายน',command=Button1)
>>> B2.place(x=300,y=20)
>>> B3 = Button(text='พฤษภาคม-มิถุนายน',command=Button2)
>>> B3.place(x=20,y=150)
B4 = Button(text='กรกฏาคม-สิงหาคม',command=Button2)
B4.place(x=300,y=150_
         
SyntaxError: invalid decimal literal
B4.place(x=300,y=150)
         
B5 = Button(text='กันยายน-ตุลาคม',command=Button2)
         
B5.place(x=20,y=300)
         
B6 = Button(text='พฤศจิกายน-ธันวาค',command=Button4)
         
B6.place(x=300,y=300)
         
