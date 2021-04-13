from Tkinter import *

window = Tk()

window.title("Claculator")
window.geometry('220x150')

show=Label(window,bg="#2196f3",width=8,height=4)
show.grid(column=0,row=0)

show.focus()

btn = Button(window, text="7" ,width= 2 , height=2)
btn.grid(column =0,row=1)

btn = Button(window, text="8",width= 2 , height=2)
btn.grid(column =1,row=1)

btn = Button(window, text="9",width= 2 , height=2)
btn.grid(column =2,row=1)

btn = Button(window, text="4",width= 2 , height=2)
btn.grid(column =0,row=2)

btn = Button(window, text="5",width= 2 , height=2)
btn.grid(column =1,row=2)

btn = Button(window, text="6",width= 2 , height=2)
btn.grid(column =2,row=2)

btn = Button(window, text="1",width= 2 , height=2)
btn.grid(column =0,row=3)

btn = Button(window, text="2",width= 2 , height=2)
btn.grid(column =1,row=3)

btn = Button(window, text="3",width= 2 , height=2)
btn.grid(column =2,row=3)

btn = Button(window, text="0",width= 2 , height=2)
btn.grid(column =1,row=4)

btn = Button(window, text="X",width= 2 , height=2)
btn.grid(column =3,row=2)

btn = Button(window, text="-",width= 2 , height=2)
btn.grid(column =3,row=3)

btn = Button(window, text="+",width= 2 , height=2)
btn.grid(column =3,row=4)

btn = Button(window, text="=",width= 2 , height=2)
btn.grid(column =0,row=4)

btn = Button(window, text=".",width= 2 , height=2)
btn.grid(column =2,row=4)

btn = Button(window, text="CE",width= 2 , height=2)
btn.grid(column =4,row=1)

btn = Button(window, text="<x",width= 2 , height=2)
btn.grid(column =3,row=1)

btn = Button(window, text="/",width= 2 , height=2)
btn.grid(column =4,row=2)

btn = Button(window, text="%",width= 2 , height=2)
btn.grid(column =4,row=3)

btn = Button(window, text="^",width= 2 , height=2)
btn.grid(column =4,row=4)
window.mainloop()
