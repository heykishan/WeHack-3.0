import csv
from tkinter import *
import os
from pandas import DataFrame
from itertools import *


screen = Tk()
screen.geometry("1000x720")
screen.title("Honeywell Saftey board")

heading = Label(text = "Fault Insertion testing dashboard", bg = "white", fg = "black", width = "720", height = "3")
heading.pack()

usage_guidelines = Label(text="Please enter the component number of the IC to being Fault insertion testing")
usage_guidelines.place(x = 20, y = 200)
usage_guidelines.pack()

def create_dict(keys, values):
    return dict(zip(keys, values + [None] * (len(keys) - len(values))))

def begin_test():
    cinfo_one = component_one.get()
    cinfo_two = component_two.get()
    cinfo_three = component_three.get()
    cinfo_four = component_four.get()
    cinfo_five = component_five.get()

    myData = [cinfo_one, cinfo_two, cinfo_three, cinfo_four, cinfo_five] 

    target_errors = []

    for i in myData:
        if(i[0][0:3] == 'T'):
            target_errors.append("Op-Amp,4 – 11,Dangerous Fault,Op-Amp cannot be operated,Iin = 250μA & Vin = 6mV")
        elif(i[0][0:3] == 'G'):
            target_errors.append("MOSFET Relay,1 – 2,Dangerous Fault,Output cannot be driven,Vin Max = 1.48V & IFT = 3mA")
        elif(i[0][0:3] == 'M'):
            target_errors.append("Maxim,1 – 19,Safe Fault,Normal Functioning,Iin = +1μA & Vin = +40")
        else:
            target_errors.append("Ivalid value. Check spelling or update dataset")
    
    main_dict  = create_dict(myData, target_errors)
    print(main_dict)

component_one = Label(text = "Componenet 1")
component_one.place(x = 2, y = 150)

component_two = Label(text = "Componenet 2")
component_two.place(x = 2, y = 230)

component_three = Label(text = "Componenet 3")
component_three.place(x = 2, y = 310)

component_four = Label(text = "Componenet 4")
component_four.place(x = 2, y = 390)

component_five = Label(text = "Componenet 5")
component_five.place(x = 2, y = 470)

component_one = StringVar()
component_two = StringVar()
component_three = StringVar()
component_four = StringVar()
component_five = StringVar()

cp1_entry = Entry(textvariable = component_one, width = 30)
cp2_entry = Entry(textvariable = component_two, width = 30)
cp3_entry = Entry(textvariable = component_three, width = 30)
cp4_entry = Entry(textvariable = component_four, width = 30)
cp5_entry = Entry(textvariable = component_five, width = 30)

cp1_entry.place( x= 150, y = 150)
cp2_entry.place( x= 150, y = 230)
cp3_entry.place( x= 150, y = 310)
cp4_entry.place( x= 150, y = 390)
cp5_entry.place( x= 150, y = 470)

register = Button(screen,text = "Analyze", width = "30", height = "3", command = begin_test, bg = "white")
register.place(x = 500, y = 600)
