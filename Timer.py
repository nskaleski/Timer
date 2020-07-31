from tkinter import *
root=Tk()
root.geometry("180x150")

t=0

def set_timer():
    global t
    t = t + int(e1.get())
    return t

def countdown():
    global t
    if t > 0:
        label1.config(text=t)
        t=t-1
        label1.after(1000, countdown)
    elif t==0:
        print("end")
        label1.config(text="DONE")

label1=Label(root,font="times 20")
label1.grid(row=1,column=2)

times=StringVar()
e1=Entry(root,textvariable=times)
e1.grid(row=3,column=2)

b1=Button(root,text="SET",width=20,command=set_timer)
b1.grid(row=4,column=2,padx=20)

b2=Button(root,text="START",width=20,command=countdown)
b2.grid(row=6,column=2,padx=20)





root.mainloop()

