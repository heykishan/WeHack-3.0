from analyze import begin_analyze
import csv
from tkinter import *

screen = Tk()
screen.geometry("1000x720")
screen.title("Honeywell Saftey board")

heading = Label(text = "Fault Insertion testing dashboard", bg = "white", fg = "black", width = "720", height = "3")
heading.pack()

usage_guidelines = Label(text="Please enter the component number of the IC to being Fault insertion testing")
usage_guidelines.place(x = 20, y = 200)
usage_guidelines.pack()

def begin_test():
    cinfo_one = component_one.get()
    cinfo_two = component_two.get()
    cinfo_three = component_three.get()
    cinfo_four = component_four.get()
    cinfo_five = component_five.get()

    myData = [[cinfo_one], [cinfo_two], [cinfo_three], [cinfo_four], [cinfo_five]] 
    myFile = open('test.csv', 'w')  
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
        print("written successfully")
    
    begin_analyze()

    
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
