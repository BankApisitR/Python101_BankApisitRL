from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from tkinter import PhotoImage


gui = Tk()
gui.title("โปรแกรมบันทึกข้อมูล")
gui.geometry('1024x720')

image = PhotoImage(file="MaleFemalePic.png")

#part1: Heading
heading = Label(gui,text="จำนวนประชากรไทย ปี 2565",font=('Angsana New',30),fg='black') 
heading.place(x=30, y=30)

#part2: Picture
pic = ttk.Button(gui, text="แสดง ยอดเงิน ปัจจุบัน")
pic = ttk.Label(gui, image=image)
pic.pack(side='top', anchor='center', pady=100)


#part3.1: functions for Buttons
def FemaleButton():
    FemaleText = "ปี 2565 ประชากรหญิง จำนวน 33,351,449 คน"
    messagebox.showinfo("ประชากรหญิง", FemaleText)

def MaleButton():
    MaleText = "ปี 2565 ประชากรชาย จำนวน 31,755,032 คน"
    messagebox.showinfo("ประชากรชาย", MaleText)
    

#part3.2: Buttons Frame
fb_female = LabelFrame(gui, text="ประชากรหญิง", font=('Angsana New',20),fg='black')
fb_female.place(x=240, y=480)

fb_male = LabelFrame(gui, text="ประชากรชาย", font=('Angsana New',20),fg='black')
fb_male.place(x=620, y=480)

#part3.3: Button
b_female = ttk.Button(fb_female, text="แสดงจำนวน", command=FemaleButton)
b_female.pack(ipadx=50, ipady=20, padx=10, pady=10)

b_male = ttk.Button(fb_male, text="แสดงจำนวน", command=MaleButton)
b_male.pack(ipadx=50, ipady=20, padx=10, pady=10)




gui.mainloop()
