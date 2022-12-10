import tkinter as tk
from tkinter import *
from tkinter import messagebox
import billing 

sroot = Tk()
sroot.title("Project")
sroot.minsize(height=500,width=1150)
sroot.configure(bg='#7FFFD4')

photo = PhotoImage(file = "icon.png")
sroot.iconphoto(False, photo)

img =PhotoImage(file="fg.png")
Label(sroot,image=img).place(x=0,y=0)
Label(sroot,text="I.P. Project",font='Timesnewroman 30 bold ',bg='#7FFFD4',fg='black').place(x=840)
Label(sroot,text="===========================================",font='Timesnewroman 15 ',bg='#7FFFD4',fg='black').place(x=740,y=60)
Label(sroot,text="Bill Management System ",font='Timesnewroman 23 bold ',bg='#7FFFD4',fg='white').place(x=770,y=100)
Label(sroot,text="===========================================",font='Timesnewroman 15 ',bg='#7FFFD4',fg='black').place(x=740,y=140)
Label(sroot,text="Made By -",font='Timesnewroman 20',bg='#7FFFD4',fg='black').place(x=740,y=180)
Label(sroot,text="----------------------------------------------------------",font='Timesnewroman 15 ',bg='#7FFFD4',fg='black').place(x=740,y=220)
Label(sroot,text="Name:-Naman Sharma",font='Timesnewroman 20',bg='#7FFFD4',fg='grey').place(x=740,y=260)
Label(sroot,text="Class:- XII-A",font='Timesnewroman 20',bg='#7FFFD4',fg='grey').place(x=740,y=300)
Label(sroot,text="Roll No. :- 15",font='Timesnewroman 20',bg='#7FFFD4',fg='grey').place(x=740,y=340)
Label(sroot,text="NamanSharma3194@gmail.com",font='Timesnewroman 20',bg='#7FFFD4',fg='grey').place(x=740,y=380)
Label(sroot,text="----------------------------------------------------------",font='Timesnewroman 15 ',bg='#7FFFD4',fg='black').place(x=740,y=420)
Label(sroot,text="===========================================",font='Timesnewroman 15 ',bg='#7FFFD4',fg='black').place(x=740,y=440)

def login():
    sroot.destroy()
    fr=tk.Tk()
    fr.title("Login Page")
    fr.geometry("900x700")
    fr.resizable(False,False)
    photo = PhotoImage(file = "icon.png")
    fr.iconphoto(False, photo)
    text_user=StringVar()
    text_pass=StringVar()

    img =PhotoImage(file="dro.png")
    Label(fr, image=img).pack()
    f=Frame(fr,bg="white")
    f.place(x=200,y=150,height=410,width=500)
    t=Label(f,text="Login Here",font=("Impact",35),fg="#d77337",bg="white").place(x=90,y=30)
    t1=Label(f,text="Employee Login Area",font=("Goudy Old Style",15),fg="#d25d17",bg="white").place(x=90,y=100)
           
    user=Label(f,text="Username",font=("Goudy Old Style",15),fg="grey",bg="white").place(x=90,y=140)
    textuser=Entry(f,font=("times new roman",15),textvariable=text_user,bg='lightgray').place(x=90,y=170,width=350,height=35)
    
    password=Label(f,text="Password",font=("Goudy Old Style",15),fg="grey",bg="white").place(x=90,y=210)
    textpass=Entry(f,font=("times new roman",15),textvariable=text_pass,bg='lightgray').place(x=90,y=240,width=350,height=35)
         
    def login_func():
        if text_pass.get()=="" or text_user.get() =="":
                messagebox.showerror("Error!","All Fields Required",parent=f)
        elif text_pass.get()!="p" or text_user.get()!="n":
                messagebox.showerror("Error!","Invalid Username/Password")
        else:
            messagebox.showinfo("Welcome",f"Welcome { text_user.get()}")
            fr.destroy()
            billing.self()
    login=Button(f,text="Login",command=login_func,bg="#d77337",fg="White",font=("times new roman",20)).place(x=300,y=350,width=180,height=40)
    fr.mainloop()
    
sroot.after(3200,login)
mainloop()
