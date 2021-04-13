from Tkinter import *
from datetime import datetime as d
import time as t 
import Tkinter
import xlwt,xlrd
from xlutils.copy import copy
import os.path

if(os.path.isfile("attendence.xls")==False):
    rb = xlwt.Workbook()
    sheet = rb.add_sheet("1")
    rb.save("attendence.xls")

def submit():

    roll = int (roll_input.get())
    name = str (name_input.get())
    branch = str (branch_input.get())
    date = d.today().strftime('%d/%m/%y')
    time = t.strftime('%H:%M:%S')
    print "submitted"

    b1 = xlrd.open_workbook('attendence.xls','r')
    s1 = b1.sheet_by_index(0)

    rowx = s1.nrows
    colx = s1.ncols
    
    b2 = copy(b1)
    sheet1 = b2.get_sheet(0)
    for i in range(colx+1):
        sheet1.write(rowx,0,roll)
        sheet1.write(rowx,1,name)
        sheet1.write(rowx,2,branch)
        sheet1.write(rowx,3,date)
        sheet1.write(rowx,4,time)

    b2.save("attendence.xls")
    
window=Tk()
window.title("Attendence System")
window.configure(bg="white")
window.geometry("480x640")

roll_Label=Label(window,width=20,text="Enter your roll number")
roll_Label.pack(fill=X,padx="10",pady="5")

roll_input=Entry(window,width=20,bg="silver")
roll_input.pack(fill=X,padx="10",pady="5")

name_Label=Label(window,width=20,text="Enter Your name")
name_Label.pack(fill=X,padx="10",pady="5")

name_input=Entry(window,width=20,bg="silver")
name_input.pack(fill=X,padx="10",pady="5")

branch_Label=Label(window,width=20,text="Enter your branch")
branch_Label.pack(fill=X,padx="10",pady="5")

branch_input=Entry(window,width=20,bg="silver")
branch_input.pack(fill=X,padx="10",pady="5")

date_Label=Label(window,width=20,text="Date: ")
date_Label=Tkinter.Label(window,text = d.today().strftime('%d/%m/%y'))
date_Label.pack(fill=X,padx="10",pady="5")

time_Label=Label(window,width=20,text="Time: ")
time_Label=Tkinter.Label(window,text = t.strftime('%H:%M:%S'))
time_Label.pack(fill=X,padx="10",pady="5")

btn = Button(window,text="submit",bg = "silver",command = submit,width=10)
btn.pack(fill=X,padx="10",pady="5")


window.mainloop()
