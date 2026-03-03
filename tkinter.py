import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.geometry("500x500")
ln=tk.Label(win,text="STUDENT REGISTRATION FORM").grid(row=0,column=0)
# name 
l1=tk.Label(win,text="Enter Name:").grid(row=1,column=0)
e1=tk.Entry(win,width=30).grid(row=1,column=1)

#phno
l2=tk.Label(win,text="Enter Phno:").grid(row=2,column=0)
e2=tk.Entry(win,width=30).grid(row=2,column=1)

#email
l3=tk.Label(win,text="Enter Email:").grid(row=3,column=0)
e3=tk.Entry(win,width=30).grid(row=3,column=1)

# combo box for group selection
gp=tk.Label(win,text="Enter Group:").grid(row=4,column=0)
def select(event):
   sel=cb.get()
cb=ttk.Combobox(win,values=["--select--","BSC-CS","BCA","BSC-AI","BSC-DS"],state="readonly")
cb.grid(row=4,column=1,pady=5)
cb.set("--select--")
'''In Tkinter, layout methods like:

.grid()

.pack()

.place()

always return None'''
cb.bind("<<ComboboxSelected>>",select)#cb.grid(row=4, column=1, pady=5)   # Layout separately You cannot mix grid() and pack() in the same parent window.
# radio button
gn=tk.Label(win,text="Enter Gender:").grid(row=5,column=0)
v1=tk.IntVar()
tk.Radiobutton(win,text="Male",variable=v1,value=1).grid(row=5,column=1,sticky=tk.W)
tk.Radiobutton(win,text="Female",variable=v1,value=2).grid(row=5,column=2,sticky=tk.W)
#checkbox
course=tk.Label(win,text="Enter course:").grid(row=8,column=0)
c1=tk.IntVar()
tk.Checkbutton(win,text="python programming",variable=c1).grid(row=9,column=1,sticky=tk.W)
c2=tk.IntVar()
tk.Checkbutton(win,text="AI",variable=c2).grid(row=10,column=1,sticky=tk.W)
c3=tk.IntVar()
tk.Checkbutton(win,text="Cyber Security",variable=c3).grid(row=11,column=1,sticky=tk.W)
c4=tk.IntVar()
tk.Checkbutton(win,text="Block chain",variable=c4).grid(row=12,column=1,sticky=tk.W)

# submit button 

bt=tk.Button(win,text="Submit",width=20,activebackground="lightgreen")
bt.grid(row=20,column=1)
win.mainloop()


~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
:i
