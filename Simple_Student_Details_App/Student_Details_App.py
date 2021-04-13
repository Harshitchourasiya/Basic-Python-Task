
from Tkinter import *

window = Tk()

window.title("Student details system")
window.geometry('480x640')

enterPrompt= Label (window,text="enter your roll no:")
enterPrompt.grid(column=0, row=0)

entrybox1 = Entry(window,width = 20)
entrybox1.grid(column=1, row=0)
entrybox1.focus()

def clicked():
    roll = int(enterprompt.get())

    attendance = xlwt.workbook()
    sheet1 = attendance.add_sheet("My_attendance_system")
    cols = ["roll number"]
    sheet1.write(0)
    attendance.save("attend.xls")
    
btn = Button(window, text="Enter", bg = "#2196f3",command = clicked)
btn.grid(column=16,row=80)

window.mainloop()
