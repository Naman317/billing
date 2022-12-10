import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
import time
import datetime as dt
from time import strftime
import math,random,os
from tkinter import messagebox

def self():
    s = []
    root=tk.Tk()
    root.title("Bill Management System")
    root.geometry('1300x690+5+5')
    photo = PhotoImage(file = "icon.png")
    root.iconphoto(False, photo)
    root.resizable(False,False)
    b="#074463"     
    title=Label(root,text="BILLING",font=("times new roman",30),fg="yellow",bg=b,bd=12,relief=GROOVE)
    title.pack(fill=X)

    category=["select option","Mobile","Clothes","Personal Care"]
    subcloth=["Pants","T-shirts","Shirts","Suits"]

    pants=["Louis Philippe","Raymond","John Players","Park Avenue"]
    price_Louis=950
    price_Raymond=1100
    price_JohnPlayers=1200
    price_ParkAvenue=750

    tshirts=["Jack n Jones","H&M","Spykar","Zara"]
    pricejack=849
    priceh=1356
    pricespykar=1799
    pricezara=1290
    shirts=["Denim","Polo","Arrow","Allen solly"]
    pricedenim=2999
    pricepolo=1659
    pricearrow=1229
    priceallen=1369
    suit=["Gucci","Wills Lifestyle","Blackberry","Burberry"]
    pricegucci=6500
    pricewillslifestyle=7500
    priceblack=8599
    pricebur=9899

    submobile=["Vivo","IPhone","OPPO","Samsung"]
    vivo=["Vivo Y20G","Vivo V9 Pro","Vivo Y72","Vivo Y12s"]
    pricevivoy20=15990
    pricevivov9=10499
    pricevivoy72=20990
    pricevivoy12=10990
    Iphone=["IPhone 12 Pro","IPhone 12","IPhone 11","IPhone XR"]
    priceiphone11=57500
    priceiphone12=80700
    priceiphonexr=42999
    priceiphone12pro=125900
    oppo=["Oppo A31","Oppo F17","Oppo A74","Oppo F11"]
    priceoppoa31=12490
    priceoppof17=16990
    priceoppoa74=17990
    priceoppof11=16990
    samsung=["Samsung Galaxy Flip3","Galaxy M32","Galaxy A52","Galaxy M12","Galaxy F12"]
    priceflip=84999
    pricegalaxym32=20999
    pricegalaxya52=35999
    pricegalaxym12=13499
    pricegalaxyf12=11999
    subcare=["Face Wash","Trimmer","Soap","Perfumes","Hair Dyes/Shampoo"]
    facewash=["Foaming Face Wash","Beardo Insta-Bright Face","Ponds Men","The Face Kit"]
    pricefoming=6450
    pricebeardo=699
    priceponds=205
    priceface=4071
    trimmer=["Philips","Nova NG 1152","Mi Cordless","Syska Ht200u"]
    pricephilip=850
    pricenova=1169
    pricemi=1049
    pricesyska=718
    Soap=["Pears","Cinthol","Dove","Lux","Nykaa"]
    pricepears=67
    pricecinthol=88
    pricedove=39
    pricelux=15
    pricenykaa=75
    perfumes=["Villian","Wild Stone","FOGG","Ustraa Insignia","WHITE OUD"]
    pricevillian=600
    pricestone=319
    pricefogg=285
    priceustra=1499
    pricewhite=499

    hair=["Wow combo kit","Brawn Hair Wax","beardo Dapper Hair Combo","Hair Care Kit-by Stride"]
    pricewow=1099
    pricebrawn=249
    pricebeardodapper=1524
    pricehair=3797

    C_name=StringVar()
    phone=StringVar()
    bll=StringVar()
    o=random.randint(100,10000)
    bll.set(str(o))
    qtlyy=IntVar()
    product=StringVar()
    Subtotal=StringVar()
    tax=StringVar()
    total=StringVar()
    prices=IntVar()
    
    def categories(choice=""):
        if cate.get()=="Clothes":
            sub_cate.config(value=subcloth)
            sub_cate.current(0)
        if cate.get()=="Mobile":
            sub_cate.config(value=submobile)
            sub_cate.current(0)
        if cate.get()=="Personal Care":
            sub_cate.config(value=subcare)
            sub_cate.current(0)

    def products(choice=""):
        if sub_cate.get()=="Suits":
            prod_Na.config(value=suit)
            prod_Na.current(0)
        if sub_cate.get()=="Pants":
            prod_Na.config(value=pants)
            prod_Na.current(0)
        if sub_cate.get()=="T-shirts":
            prod_Na.config(value=tshirts)
            prod_Na.current(0)
        if sub_cate.get()=="Shirts":
            prod_Na.config(value=shirts)
            prod_Na.current(0)

        
        if sub_cate.get()=="Vivo":
            prod_Na.config(value=vivo)
            prod_Na.current(0)
        if sub_cate.get()=="IPhone":
            prod_Na.config(value=Iphone)
            prod_Na.current(0)
        if sub_cate.get()=="OPPO":
            prod_Na.config(value=oppo)
            prod_Na.current(0)
        if sub_cate.get()=="Samsung":
            prod_Na.config(value=samsung)
            prod_Na.current(0)
        
        
        if sub_cate.get()=="Hair Dyes/Shampoo":
            prod_Na.config(value=hair)
            prod_Na.current(0)
        if sub_cate.get()=="Face Wash":
            prod_Na.config(value=facewash)
            prod_Na.current(0)
        if sub_cate.get()=="Soap":
            prod_Na.config(value=Soap)
            prod_Na.current(0)
        if sub_cate.get()=="Perfumes":
            prod_Na.config(value=perfumes)
            prod_Na.current(0)
        if sub_cate.get()=="Trimmer":
            prod_Na.config(value=trimmer)
            prod_Na.current(0)
            
    def Productprice(choice=""):
        if prod_Na.get()=="Raymond":
            prices.set(value=price_Raymond)
            qtlyy.set(1)
        if prod_Na.get()=="Louis Philippe":
            prices.set(value=price_Louis)
            qtlyy.set(1)
        if prod_Na.get()=="John Players":
            prices.set(value=price_JohnPlayers)
            qtlyy.set(1)
        if prod_Na.get()=="Park Avenue":
            prices.set(value=price_ParkAvenue)
            qtlyy.set(1)
        if prod_Na.get()=="Jack n Jones":
            prices.set(value=pricejack)
            qtlyy.set(1)
        if prod_Na.get()=="H&M":
            prices.set(value=priceh)
            qtlyy.set(1)
        if prod_Na.get()=="Spykar":
            prices.set(value=pricespykar)
            qtlyy.set(1)
        if prod_Na.get()=="Zara":
            prices.set(value=pricezara)
            qtlyy.set(1)
        if prod_Na.get()=="Denim":
            prices.set(value=pricedenim)
            qtlyy.set(1)
        if prod_Na.get()=="Polo":
            prices.set(value=pricepolo)
            qtlyy.set(1)
        if prod_Na.get()=="Arrow":
            prices.set(value=pricearrow)
            qtlyy.set(1)
        if prod_Na.get()=="Allen solly":
            prices.set(value=priceallen)
            qtlyy.set(1)
        if prod_Na.get()=="Gucci":
            prices.set(value=pricegucci)
            qtlyy.set(1)
        if prod_Na.get()=="Wills Lifestyle":
            prices.set(value=pricewillslifestyle)
            qtlyy.set(1)
        if prod_Na.get()=="Blackberry":
            prices.set(value=priceblack)
            qtlyy.set(1)
        if prod_Na.get()=="Burberry":
            prices.set(value=pricebur)
            qtlyy.set(1)
        if prod_Na.get()=="Vivo Y20G":
            prices.set(value=pricevivoy20)
            qtlyy.set(1)
        if prod_Na.get()=="Vivo V9 Pro":
            prices.set(value=pricevivov9)
            qtlyy.set(1)
        if prod_Na.get()=="Vivo Y72":
            prices.set(value=pricevivoy72)
            qtlyy.set(1)
        if prod_Na.get()=="Vivo Y12s":
            prices.set(value=pricevivoy12)
            qtlyy.set(1)
        if prod_Na.get()=="IPhone 12 Pro":
            prices.set(value=priceiphone12pro)
            qtlyy.set(1)
        if prod_Na.get()=="IPhone 12":
            prices.set(value=priceiphone12)
            qtlyy.set(1)
        if prod_Na.get()=="IPhone 11":
            prices.set(value=priceiphone11)
            qtlyy.set(1)
        if prod_Na.get()=="IPhone XR":
            prices.set(value=priceiphonexr)
            qtlyy.set(1)
        if prod_Na.get()=="Oppo A31":
            prices.set(value=priceoppoa31)
            qtlyy.set(1)
        if prod_Na.get()=="Oppo F17":
            prices.set(value=priceoppof17)
            qtlyy.set(1)
        if prod_Na.get()=="Oppo A74":
            prices.set(value=priceoppoa74)
            qtlyy.set(1)
        if prod_Na.get()=="Oppo F11":
            prices.set(value=priceoppof11)
            qtlyy.set(1)
        if prod_Na.get()=="Samsung Galaxy Flip3":
            prices.set(value=priceflip)
            qtlyy.set(1)
        if prod_Na.get()=="Galaxy M32":
            prices.set(value=pricegalaxym32)
            qtlyy.set(1)
        if prod_Na.get()=="Galaxy A52":
            prices.set(value=pricegalaxya52)
            qtlyy.set(1)
        if prod_Na.get()=="Galaxy M12":
            prices.set(value=pricegalaxym12)
            qtlyy.set(1)
        if prod_Na.get()=="Galaxy F12":
            prices.set(value=pricegalaxyf12)
            qtlyy.set(1)
        if prod_Na.get()=="Foaming Face Wash":
            prices.set(value=pricefoming)
            qtlyy.set(1)
        if prod_Na.get()=="Beardo Insta-Bright Face":
            prices.set(value=pricebeardo)
            qtlyy.set(1)
        if prod_Na.get()=="Ponds Men":
            prices.set(value=priceponds)
            qtlyy.set(1)
        if prod_Na.get()=="The Face Kit":
            prices.set(value=priceface)
            qtlyy.set(1)
        if prod_Na.get()=="Philips":
            prices.set(value=pricephilip)
            qtlyy.set(1)
        if prod_Na.get()=="Nova NG 1152":
            prices.set(value=pricenova)
            qtlyy.set(1)
        if prod_Na.get()=="Mi Cordless":
            prices.set(value=pricemi)
            qtlyy.set(1)
        if prod_Na.get()=="Syska Ht200u":
            prices.set(value=pricesyska)
            qtlyy.set(1)
        if prod_Na.get()=="Pears":
            prices.set(value=pricepears)
            qtlyy.set(1)
        if prod_Na.get()=="Cinthol":
            prices.set(value=pricecinthol)
            qtlyy.set(1)
        if prod_Na.get()=="Dove":
            prices.set(value=pricedove)
            qtlyy.set(1)
        if prod_Na.get()=="Lux":
            prices.set(value=pricelux)
            qtlyy.set(1)
        if prod_Na.get()=="Nykaa":
            prices.set(value=pricenykaa)
            qtlyy.set(1)
        if prod_Na.get()=="Villian":
            prices.set(value=pricevillian)
            qtlyy.set(1)
        if prod_Na.get()=="Wild Stone":
            prices.set(value=pricestone)
            qtlyy.set(1)
        if prod_Na.get()=="FOGG":
            prices.set(value=pricefogg)
            qtlyy.set(1)
        if prod_Na.get()=="Ustraa Insignia":
            prices.set(value=priceustra)
            qtlyy.set(1)
        if prod_Na.get()=="WHITE OUD":
            prices.set(value=pricewhite)
            qtlyy.set(1)
        if prod_Na.get()=="Wow combo kit":
            prices.set(value=pricewow)
            qtlyy.set(1)
        if prod_Na.get()=="Brawn Hair Wax":
            prices.set(value=pricebrawn)
            qtlyy.set(1)
        if prod_Na.get()=="beardo Dapper Hair Combo":
            prices.set(value=pricebeardodapper)
            qtlyy.set(1)
        if prod_Na.get()=="Hair Care Kit-by Stride":
            prices.set(value=pricebeardodapper)
            qtlyy.set(1)
            
    def wlcme_bll():
        txtarea.insert(END,"\t        Hastee Mart       \n")
        txtarea.insert(END,f"\t\t\t     Date: {dt.datetime.now():%a, %b %d %Y}")
        txtarea.insert(END,f"\t\t\t\t\t\t\t           Time: {strftime('%H:%M %p')}")
        txtarea.insert(END,f"\nBill No. :{bll.get()}")
        txtarea.insert(END,f"\nCustomer Name : {C_name.get() }")
        txtarea.insert(END,f"\nPhone No. :{phone.get()}")
        txtarea.insert(END,"\n===========================================")
        txtarea.insert(END,"\nProducts\t\tQty\t\tPrice")
        txtarea.insert(END,"\n===========================================")
        
    f=LabelFrame(root,bd=6,text="Customer Detail",font=("times new roman",12,BOLD),fg="yellow",bg=b)
    f.place(x=0,y=70,relwidth=1)
    bill=Label(f,text="Bill Number",bg=b,fg="white",font=("times new roman",12))
    bill.grid(row=0,column=4,padx=20,pady=5)
    bill_txt=Entry(f,font=("arial"),textvariable=bll,bd=2,relief=SUNKEN,width=20)
    bill_txt.grid(row=0,column=5,padx=10,pady=5)

    name=Label(f,text="Customer Name",bg=b,fg="white",font=("times new roman",12,))
    name.grid(row=0,column=0,padx=20,pady=5)
    txt=Entry(f,font=("arial"),bd=2,textvariable=C_name,relief=SUNKEN,width=20)
    txt.grid(row=0,column=1,padx=10,pady=5)

    ph=Label(f,text="Phone Number",bg=b,fg="white",font=("times new roman",12,))
    ph.grid(row=0,column=2,padx=20,pady=5)
    ph_txt=Entry(f,font=("arial"),bd=2,textvariable=phone,relief=SUNKEN,width=20)
    ph_txt.grid(row=0,column=3,padx=10,pady=5)

    f2=LabelFrame(root,bd=6,text="Product",font=("times new roman",12,BOLD),fg="yellow",bg=b)
    f2.place(x=0,y=160,width=350,height=380)

    img =PhotoImage(file="pic.png")
    Label(root,image=img).place(x=323,y=160)
    
    cat=Label(f2,font=('arial',12),text="Select Category",bg=b,fg='lightyellow')
    cat.grid(row=0,column=0,padx=10,pady=5)
    cate=ttk.Combobox(f2,font=('arial'),width=15,value=category,state='readonly')
    cate.current(0)
    cate.grid(row=0,column=1,padx=10,pady=5)
    cate.bind("<<ComboboxSelected>>",categories)
    sub_cat=Label(f2,font=('arial',12),text="SubCategory",bg=b,fg='lightyellow')
    sub_cat.grid(row=1,column=0,padx=10,pady=5)
    sub_cate=ttk.Combobox(f2,font=('arial'),value=[""],width=15,state='readonly')
    sub_cate.grid(row=1,column=1,padx=10,pady=5)
    sub_cate.current(0)
    sub_cate.bind("<<ComboboxSelected>>",products)
    prod_N=Label(f2,font=('arial',12),text="Product Name",bg=b,fg='lightyellow')
    prod_N.grid(row=2,column=0,padx=10,pady=5)
    prod_Na=ttk.Combobox(f2,font=('arial'),textvariable=product,value=[""],width=15,state='readonly')
    prod_Na.current(0)
    prod_Na.bind("<<ComboboxSelected>>",Productprice)
    prod_Na.grid(row=2,column=1,padx=10,pady=5)
    Pric=Label(f2,font=('arial',12),text="Price",bg=b,fg='lightyellow')
    Pric.grid(row=3,column=0,padx=10,pady=5)
    Price=ttk.Entry(f2,font=('arial'),textvariable=prices,width=17,state='readonly')
    Price.grid(row=3,column=1,padx=10,pady=5)
    Qt=Label(f2,font=('arial',12),text="Qty",bg=b,fg='lightyellow')
    Qt.grid(row=4,column=0,padx=10,pady=5)
    Qty=ttk.Entry(f2,font=('arial'),textvariable=qtlyy,width=17)
    Qty.grid(row=4,column=1,padx=10,pady=5)
    f5=Frame(root,bd=10,relief=GROOVE)
    f5.place(x=905,y=160,height=380,width=390)
    title=Label(f5,text="BILL AREA",bd=7,font=("arial",25),relief=GROOVE).pack(fill=X)
    scrol=Scrollbar(f5,orient=VERTICAL)
    txtarea=Text(f5,fg=b,bg='white',font=('arial',10,BOLD),yscrollcommand=scrol.set)
    scrol.pack(side=RIGHT,fill=Y)
    scrol.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH)

    f6=LabelFrame(root,bd=6,text="Bill",font=("times new roman",12,BOLD),fg="yellow",bg=b)
    f6.place(x=0,y=540,relwidth=1,height=150)
    b1=Label(f6,text="Sub Total",bg=b,fg="lightyellow",font=("times new roman",12,))
    b1.grid(row=0,column=0,padx=0,pady=0)
    b1txt=Entry(f6,font=("arial"),bd=2,textvariable=Subtotal,relief=SUNKEN,width=13)
    b1txt.grid(row=0,column=1,padx=10,pady=2)
    b2=Label(f6,text="Total Price",bg=b,fg="lightyellow",font=("times new roman",12,))
    b2.grid(row=1,column=0,padx=0,pady=0)
    b2_txt=Entry(f6,font=("arial"),bd=2,textvariable=total,relief=SUNKEN,width=13)
    b2_txt.grid(row=1,column=1,padx=10,pady=2)

    t1=Label(f6,text="Tax",bg=b,fg="lightpink",font=("times new roman",12,))
    t1.grid(row=0,column=2,padx=20,pady=0)
    t1_txt=Entry(f6,font=("arial"),bd=2,relief=SUNKEN,textvariable=tax,width=13)
    t1_txt.grid(row=0,column=3,padx=20,pady=20)
    wlcme_bll()

    def Add():
        if C_name.get()=="" or ph_txt.get()=="":
            messagebox.showerror('Error!','Customer Details are must')
        elif product.get()=="":
            messagebox.showerror('Error!','No Product Pruchased')
        elif product.get()==" ":
            messagebox.showerror("Error!","Please Select The Product ")
        else:
            u=prices.get()
            v=qtlyy.get()*u
            s.append(v)
            txtarea.insert(END,f"\n{product.get()}\t\t{qtlyy.get()}\t\t{v}")
            cate.set("select option")
            prices.set("")
            prod_Na.set("")
            sub_cate.set("")
            qtlyy.set("")


    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000, time)
        date = dt.datetime.now()
        format_date = f"{date:%a, %b %d %Y}"
    war = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg=b, font=("helvetica",25))
    war.place(x=50,y=15)
    lbl = Label(root,font = ('calibri',25, 'bold'),bg=b,foreground = 'white')
    lbl.place(x=1100,y=15)
    time()

    def done():
        txtarea.delete('1.0',END)
        wlcme_bll()
        
    def genratebill():
        if C_name.get()=="" or ph_txt.get()=="":
            messagebox.showerror('Error!','Customer Details are must')
        else:
            txtarea.insert(END,"\n-------------------------------------------")
            txtarea.insert(END,f"\nSub Total\t\t{Subtotal.get() }")
            txtarea.insert(END,f"\nTax Amount\t\t{tax.get() }")
            txtarea.insert(END,"\n-------------------------------------------")
            txtarea.insert(END,f"\nTotal Bill:\t\t{total.get() }")
            txtarea.insert(END,"\n-------------------------------------------")
            txtarea.insert(END,"\n========THANKS FOR PURCHASING=============")
            txtarea.insert(END,"\n================VISIT AGAIN=================")
            save()
            
    def save():
        op=messagebox.askyesno('Save Bill','Do You Want To Save The Bill?')
        if op>0:
            billdata=txtarea.get('1.0',END)
            f1=open("Bills/"+str(bll.get())+" .txt",'w')
            f1.write(billdata)
            f1.close()
            messagebox.showinfo('Saved',f'bill no.:{bll.get()}saved successfully')
        else:
            return
    def clear ():
        C_name.set("")
        phone.set("")
        o=random.randint(100,10000)
        bll.set(str(o))
        txtarea.delete('1.0',END)
        Subtotal.set("")
        tax.set("")
        total.set("")
        cate.set("select option")
        prices.set("")
        prod_Na.set("")
        sub_cate.set("")
        qtlyy.set("")
        wlcme_bll()

    def Total():
        if C_name.get()=="" or ph_txt.get()=="":
            messagebox.showerror('Error!','Customer Details are must')
        else:
            Subtotal.set(str('%.2f'%(sum(s))))
            tax.set(str('%.2f'%((sum(s))*0.01)))
            a = float(Subtotal.get())
            b = float(tax.get())
            total.set("Rs. "+ str(a+b))

    def Exit():
        og=messagebox.askyesno("Exit",'Do you really want to exit?')
        if og>0:
            root.destroy()
        
    btnsF=Frame(f6,bd=4,relief=GROOVE)
    btnsF.place(x=495,height=110,width=780)    
    buton1=Button(btnsF,text="Total",font=('arial',19),width=5,bg=b,bd=5,fg="cyan",command=Total)
    buton1.grid(row=0,column=1,padx=10,pady=16)
    buton2=Button(btnsF,text="Generate Bill",font=('arial',19),command=genratebill,width=10,bg=b,bd=5,fg="cyan")
    buton2.grid(row=0,column=2,padx=10,pady=16)
    buton3=Button(btnsF,text="Clear All",command=clear,font=('arial',19),width=8,bg=b,bd=5,fg="cyan")
    buton3.grid(row=0,column=3,padx=10,pady=16)
    buton4=Button(btnsF,text="Exit",command=Exit,font=('arial',19),width=7,bg=b,bd=5,fg="cyan")
    buton4.grid(row=0,column=4,padx=10,pady=16)
    buton5=Button(btnsF,text="Add to Cart",font=('arial',19),command=Add,width=10,bg=b,bd=5,fg="cyan")
    buton5.grid(row=0,column=0,padx=10,pady=16)
    buton6=Button(f,text="OK",font=('arial',19),command=done,width=7,bg=b,bd=5,fg="cyan")
    buton6.grid(row=0,column=6,padx=10,pady=5)

    tk.mainloop()
