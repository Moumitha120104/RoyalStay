import pickle
import os
customer_id=[]
g_id=""
room_rent=0
game_rent=0
restaurant_rent=0
from tkinter import *
root=Tk()

def show():
    global root
    root.destroy()
    root=Tk()
    g_id=IntVar()
    c_name=StringVar()
    c_ad=StringVar()
    c_age=IntVar()
    c_country=StringVar()
    c_email=StringVar()
    def display():
        try:
            int(g_id.get())
            str(c_name.get())
            int(c_age.get())
            int(c_no.get())
            file_exists = os.path.exists('Hotel2.dat')
            if file_exists and os.path.getsize('Hotel2.dat') > 0:
                f = open('Hotel2.dat', 'rb')
                l = pickle.load(f)
                f.close()
            else:
                l = []
            l.append([g_id.get(),c_name.get(),c_ad.get(),c_age.get(),c_no.get(),c_country.get()])
            file=open("Hotel2.dat","wb")
            pickle.dump(l,file)
            file.close()
            from tkinter import messagebox
            messagebox.showinfo("WELCOME","The Customer details are updated Successful")
            customer_id.append(g_id.get())
        except:
            from tkinter import messagebox
            messagebox.showerror("ERROR","Enter proper value")

    g_id=IntVar()
    c_name=StringVar()
    c_age=IntVar()
    c_no=IntVar()
    c_ad=StringVar()
    c_country=StringVar()
    
    l2=Label(root,text="Guest details",fg="red",font=("times",60))
    l2.grid(row=0,column=1)
    g_id=Entry(root,width=60,font=30)
    g_l=Label(root,text="Enter Customer Id number : ",font=("times",20),width=40)
    g_l.grid(row=1,column=0)
    g_id.grid(row=1,column=1)  
    c_name=Entry(root,width=60,font=30)
    c_l=Label(root,text="Enter Customer Name :",font=("times",20),width=40)
    c_l.grid(row=2,column=0)
    c_name.grid(row=2,column=1)
    c_ad=Entry(root,width=60,font=30)
    ca_l=Label(root,text="Enter Customer Address:",font=("times",20),width=40)
    ca_l.grid(row=3,column=0)
    c_ad.grid(row=3,column=1)
    c_age=Entry(root,width=60,font=30)
    cage_l=Label(root,text="Enter Customer Age :",font=("times",20),width=40)
    cage_l.grid(row=4,column=0)
    c_age.grid(row=4,column=1)
    c_country=Entry(root,width=60,font=30)
    c_country.grid(row=5,column=1)
    cc_l=Label(root,text="Enter Customer country :",font=("times",20),width=40)
    cc_l.grid(row=5,column=0)
    c_no=Entry(root,width=60,font=30)
    c_no.grid(row=6,column=1)
    cn_l=Label(root,text="Enter Customer Number :",font=("times",20),width=40)
    cn_l.grid(row=6,column=0)
    c_but=Button(root,text="SUBMIT",command=display,fg="blue",font=("times",40))
    c_but.grid(row=8,column=1)
    c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
    c1_but.grid(row=8,column=2)
    root.mainloop()

def booking_details():
    global root
    root.destroy()
    root=Tk()
    def bk():
        global root
        root.destroy()
        root=Tk()
        bk4=Label(root,text="Enter check in date : ",font=("times",20),width=40)
        bk4.grid(row=0,column=0)
        bk7=Entry(root,width=60,font=30)
        bk7.grid(row=0,column=1)
        bk5=Label(root,text="Number of days : ",font=("times",20),width=40)
        bk5.grid(row=1,column=0)
        bk8=Entry(root,width=60,font=30)
        bk8.grid(row=1,column=1)
        r_id=Entry(root,width=60,font=30)
        r_l=Label(root,text="Enter Customer ID No. : ",font=("times",20),width=40)
        r_l.grid(row=2,column=0)
        r_id.grid(row=2,column=1)
        c_but=Button(root,text="SUBMIT",command=booking_details,fg="blue",font=("times",30))
        c_but.grid(row=5,column=0)
        
    def ck():
        global root
        root.destroy()
        root=Tk()
        bk9=Label(root,text="Enter check out date:",font=("times",20),width=60)
        bk9.grid(row=0,column=0)
        bk12=Entry(root,width=30)
        bk12.grid(row=0,column=1)
        bk10=Label(root,text="Number of days:",font=("times",20),width=60)
        bk10.grid(row=1,column=0)
        bk11=Entry(root,width=30)
        bk11.grid(row=1,column=1)
        r_id=Entry(root,width=60,font=30)
        r_l=Label(root,text="Enter Customer ID No. : ",font=("times",20),width=40)
        r_l.grid(row=2,column=0)
        r_id.grid(row=2,column=1)
        c_but=Button(root,text="SUBMIT",command=booking_details,fg="blue",font=("times",30))
        c_but.grid(row=5,column=0)
    def disp():
        from tkinter import messagebox
        messagebox.showinfo("THANK YOU","Info updated")
    bk1=Label(root,text="BOOKING DETAILS",font=("times",40),bg="orange",fg="black")
    bk1.grid(row=0,column=1)
    bk2=Button(root,text="CHECK INN",command=bk,font=("times",20),width=40)
    bk2.grid(row=2,column=1)
    bk3=Button(root,text="CHECK OUT",command=ck,font=("times",20),width=40)
    bk3.grid(row=3,column=1)
    c_but=Button(root,text="SUBMIT",command=disp,fg="blue",font=("times",30))
    c_but.grid(row=5,column=0)
    c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",30))
    c1_but.grid(row=5,column=2)
    root.mainloop()
    
def room_rent():
    global customer_id
    global root
    root.destroy()
    root=Tk()
    a=IntVar()
    def rm():
        global root
        root.destroy()
        root=Tk()
        ab=IntVar()
        def room():
            global root
            root.destroy()
            root=Tk()
            r_name=IntVar()
            r_ad=IntVar()
            r_id=IntVar()
            r_no=IntVar()
            def display1():
                global room_rent
                room_rent=int(ab.get())*int(r_name.get())*int(r_ad.get())
                file=open("Hotel2.dat","rb")
                l=pickle.load(file)
                file.close()
                for i in l:
                    if i[0]==r_id.get():
                        i.insert(6,room_rent)
                        from tkinter import messagebox
                        messagebox.showinfo("THANK YOU","YOUR TOTAL ROOM RENT IS {}".format(room_rent))
                file=open("Hotel2.dat","wb")
                pickle.dump(l,file)
                file.close()


            room=Label(root,text="PLEASE ENTER THE DETAILS : ",fg="red",font=("times",50))
            room.grid()
            r_id=Entry(root,width=60,font=30)
            r_l=Label(root,text="Enter Customer ID No. : ",font=("times",20),width=40)
            r_l.grid(row=2,column=0)
            r_id.grid(row=2,column=1)
            r_name=Entry(root,width=60,font=30)
            r_l=Label(root,text="Enter No. of days : ",font=("times",20),width=40)
            r_l.grid(row=3,column=0)
            r_name.grid(row=3,column=1)
            r_ad=Entry(root,width=60,font=30)
            ra_l=Label(root,text="Enter No. of Rooms : ",font=("times",20),width=40)
            ra_l.grid(row=4,column=0)
            r_ad.grid(row=4,column=1)
            r_but=Button(root,text="SUBMIT",command=display1,fg="blue",font=("times",40))
            r_but.grid(row=5,column=0)
            r1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
            r1_but.grid(row=5,column=1)
        l3=Label(root,text="ROOM CHOICE",fg="red",font=("times",60))
        l3.grid(row=0,column=2)
        r1=Radiobutton(root,text="Ultra Royal",variable=ab,value=10000,command=room,width=40,fg="red",font=("times",30))
        r1.grid(row=1,column=2)
        r2=Radiobutton(root,text="Royal",fg="red",variable=ab,value=5000,command=room,width=40,font=("times",30))
        r2.grid(row=2,column=2)
        r3=Radiobutton(root,text="Elite",fg="red",width=40,variable=ab,value=3500,command=room,font=("times",30))
        r3.grid(row=3,column=2)
        r4=Radiobutton(root,text="Budget",fg="red",width=40,variable=ab,value=1500,command=room,font=("times",30))
        r4.grid(row=4,column=2)
        r1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
        r1_but.grid(row=8,column=4)
        r_but=Button(root,text="SUBMIT",command=room,fg="blue",font=("times",40))
        r_but.grid(row=5,column=0)
        root.mainloop()
    
    l=Label(root,text="ROOM BOOKING",fg="yellow",bg="black").grid(row=0,column=2)
    l2=Label(root,text="Pick a room").grid(row=5,column=2)
    b1=Radiobutton(root,text="1",padx=20,pady=20,command=rm,variable=a,value=1,font=("times",30),activebackground="blue")
    b1.grid(row=1,column=0)
    b2=Radiobutton(root,text="2",padx=20,pady=20,command=rm,variable=a,value=2,font=("times",30),activebackground="blue")
    b2.grid(row=1,column=1)
    b3=Radiobutton(root,text="3",padx=20,pady=20,command=rm,variable=a,value=3,font=("times",30),activebackground="blue")
    b3.grid(row=1,column=2)
    b4=Radiobutton(root,text="4",padx=20,pady=20,command=rm,variable=a,value=4,font=("times",30),activebackground="blue")
    b4.grid(row=1,column=3)
    b5=Radiobutton(root,text="5",padx=20,pady=20,command=rm,variable=a,value=5,font=("times",30),activebackground="blue")
    b5.grid(row=1,column=4)
    b6=Radiobutton(root,text="6",padx=20,pady=20,command=rm,variable=a,value=6,font=("times",30),activebackground="blue")
    b6.grid(row=2,column=0)
    b7=Radiobutton(root,text="7",padx=20,pady=20,command=rm,variable=a,value=7,font=("times",30),activebackground="blue")
    b7.grid(row=2,column=1)
    b8=Radiobutton(root,text="8",padx=20,pady=20,command=rm,variable=a,value=8,font=("times",30),activebackground="blue")
    b8.grid(row=2,column=2)
    b9=Radiobutton(root,text="9",padx=20,pady=20,command=rm,variable=a,value=9,font=("times",30),activebackground="blue")
    b9.grid(row=2,column=3)
    b10=Radiobutton(root,text="10",padx=20,pady=20,command=rm,variable=a,value=10,font=("times",30),activebackground="blue")
    b10.grid(row=2,column=4)
    b11=Radiobutton(root,text="11",padx=20,pady=20,command=rm,variable=a,value=11,font=("times",30),activebackground="blue")
    b11.grid(row=3,column=0)
    b12=Radiobutton(root,text="12",padx=20,pady=20,command=rm,variable=a,value=12,font=("times",30),activebackground="blue")
    b12.grid(row=3,column=1)
    b13=Radiobutton(root,text="13",padx=20,pady=20,command=rm,variable=a,value=13,font=("times",30),activebackground="blue")
    b13.grid(row=3,column=2)
    b14=Radiobutton(root,text="14",padx=20,pady=20,command=rm,variable=a,value=14,font=("times",30),activebackground="blue")
    b14.grid(row=3,column=3)
    b15=Radiobutton(root,text="15",padx=20,pady=20,command=rm,variable=a,value=15,font=("times",30),activebackground="blue")
    b15.grid(row=3,column=4)
    root.mainloop()

def restaurant():
    global restaurant_rent
    global root
    root.destroy()
    root=Tk()
    a=IntVar()
    b=IntVar()
    c=IntVar()
    d=IntVar()
    e=IntVar()
    def restaurant_details():
        global root
        root.destroy()
        root=Tk()
        x_ad=IntVar()
        r_id=IntVar()
        def display():
            global restaurant_rent
            restaurant_cost=int(a.get())+int(b.get())+int(c.get())
            restaurant_rent=int(restaurant_cost)*int(x_ad.get())
            int(restaurant_rent)
            file=open("Hotel2.dat","rb")
            l=pickle.load(file)
            file.close()
            for i in l:
                if i[0]==r_id.get():
                    i.insert(8,restaurant_rent)
                    from tkinter import messagebox
                    messagebox.showinfo("THANK YOU","YOUR RESTAURANT BILL IS {}".format(restaurant_rent))
            file=open("Hotel2.dat",'wb')
            pickle.dump(l,file)
            file.close()
        l_x=Label(root,text="Guest details",fg="blue",font=("times",40))
        l_x.grid(row=0,column=1)
        x_ad=Entry(root,width=60,font=30)
        r_id=Entry(root,width=60,font=30)
        r_l=Label(root,text="Enter Customer ID No. : ",font=("times",20),width=40)
        r_l.grid(row=3,column=0)
        r_id.grid(row=3,column=1)
        xa_l=Label(root,text="Enter The number of persons : ",font=("times",20),width=40)
        xa_l.grid(row=2,column=0)
        x_ad.grid(row=2,column=1)
        y_ad=Entry(root,width=60,font=30)
        c_but=Button(root,text="SUBMIT",command=display,fg="blue",font=("times",40))
        c_but.grid(row=8,column=1)
        c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
        c1_but.grid(row=8,column=2)
    l2=Label(root,text="RESTAURANT",fg="red",font=("Helvetica",60))
    l2.grid(row=0,column=2)
    l=Label(root,text="WE HAVE A BUFFET SYSTEM HERE",fg="green",font=("times",20))
    l.grid(row=1,column=2)
    g1=Checkbutton(root,text="Vegetarian Combo",variable=a,onvalue=2000,offvalue=0,fg="purple",font=("Helvetica",20),width=40)
    g1.grid(row=2,column=2)
    g2=Checkbutton(root,text="Non-Vegetarian",variable=b,onvalue=2500,offvalue=0,fg="purple",font=("Helvetica",20),width=40)
    g2.grid(row=3,column=2)
    g3=Checkbutton(root,text="Veg and Non-Veg",variable=c,onvalue=3000,offvalue=0,fg="purple",font=("Helvetica",20),width=40)
    g3.grid(row=4,column=2)
    g1.deselect()
    g2.deselect()
    g3.deselect()
    a_but=Button(root,text="SUBMIT",command=restaurant_details,fg="blue",font=("times",40))
    a_but.grid(row=5,column=0)
    c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
    c1_but.grid(row=5,column=4)
    root.mainloop()
def game_play():
    global game_rent
    global root
    root.destroy()
    root=Tk()
    a=IntVar()
    b=IntVar()
    c=IntVar()
    d=IntVar()
    e=IntVar()
    def game_details():
        global root
        root.destroy()
        root=Tk()
        x_ad=IntVar()
        r_id=IntVar()
        def display():
            global game_rent
            game_cost=int(a.get())+int(b.get())+int(c.get())+int(d.get())+int(e.get())
            game_rent=int(game_cost)*int(x_ad.get())
            file=open("Hotel2.dat","rb")
            l=pickle.load(file)
            file.close()
            for i in l:
                if i[0]==r_id.get():
                    i.insert(7,game_rent)
                    from tkinter import messagebox
                    messagebox.showinfo("THANK YOU","YOUR TOTAL GAME COST IS {}".format(game_rent))
            file=open("Hotel2.dat",'wb')
            pickle.dump(l,file)
            file.close()
        l_x=Label(root,text="Guest details",fg="blue",font=("times",40))
        l_x.grid(row=0,column=1)
        x_ad=Entry(root,width=60,font=30)
        r_id=Entry(root,width=60,font=30)
        r_l=Label(root,text="Enter Customer ID No. : ",font=("times",20),width=40)
        r_l.grid(row=3,column=0)
        r_id.grid(row=3,column=1)
        xa_l=Label(root,text="Enter No. of Hours you want to play:",font=("times",20),width=40)
        xa_l.grid(row=2,column=0)
        x_ad.grid(row=2,column=1)
        y_ad=Entry(root,width=60,font=30)
        c_but=Button(root,text="SUBMIT",command=display,fg="blue",font=("times",40))
        c_but.grid(row=8,column=1)
        c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
        c1_but.grid(row=8,column=2)
    l2=Label(root,text="GAMMING INFORMATION",fg="red",font=("Helvetica",60))
    l2.grid(row=0,column=2)
    g1=Checkbutton(root,text="CRICKET",variable=a,onvalue=200,offvalue=0,fg="purple",font=("Helvetica",20),width=20)
    g1.grid(row=5,column=2)
    g2=Checkbutton(root,text="SHUTTLE BATMITTON",variable=b,onvalue=150,offvalue=0,fg="purple",font=("Helvetica",20),width=20)
    g2.grid(row=1,column=2)
    g3=Checkbutton(root,text="TABLE TENNIS",variable=c,onvalue=100,offvalue=0,fg="purple",font=("Helvetica",20),width=20)
    g3.grid(row=2,column=2)
    g4=Checkbutton(root,text="SNOOKER",variable=d,onvalue=150,offvalue=0,fg="purple",font=("Helvetica",20),width=20)
    g4.grid(row=3,column=2)
    g5=Checkbutton(root,text="ARCHERY",variable=e,onvalue=100,offvalue=0,fg="purple",font=("Helvetica",20),width=20)
    g5.grid(row=4,column=2)
    g1.deselect()
    g2.deselect()
    g3.deselect()
    g4.deselect()
    g5.deselect()
    a_but=Button(root,text="SUBMIT",command=game_details,fg="blue",font=("times",40))
    a_but.grid(row=6,column=0)
    c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
    c1_but.grid(row=6,column=4)
    root.mainloop()

def payment():
    global root
    root.destroy()
    from tkinter import messagebox
    root=Tk()
    def show():
        messagebox.showinfo("THANK YOU","PAYMENT SUCCESSFUL")
    l91=Label(root,text="SELECT PAYMENT MODE",font=('times 40'),fg='red')
    l91.grid(row=0,column=3)
    n=IntVar()
    chk91=Radiobutton(root,text="Credit card/Debit card",font=('times', 30),fg='blue',value=1,variable=n)    
    chk91.grid(row=1,column=3)
    chk92=Radiobutton(root,text="phonepay/paytm",font=('times',30),fg='blue',value=2,variable=n)
    chk92.grid(row=2,column=3)
    chk93=Radiobutton(root,text="cash",font=('times',30),fg='blue',value=3,variable=n)
    chk93.grid(row=3,column=3)
    V=Button(root,text="PROCEED TO PAY",command=show,fg="green",font=("times",30))
    V.grid(row=6,column=1)
    chk91.deselect()
    chk92.deselect()
    chk93.deselect()
    c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
    c1_but.grid(row=6,column=4)
    root.mainloop()
def guest_details():
    global root
    root.destroy()
    root=Tk()
    a_id=IntVar()
    a_id=Entry(root,width=60,font=30)
    a_l=Label(root,text="Enter Customer Id number : ",font=("times",20),width=40)
    a_l.grid(row=1,column=0)
    a_id.grid(row=1,column=1)
    def details():
        file=open("Hotel2.dat","rb")
        l=pickle.load(file)
        file.close()
        for i in l:
            if i[0]==a_id.get():
                name=i[1]
                address=i[2]
                age=i[3]
                number=i[4]
                country=i[5]
                room_rent=i[6]
                game_rent=i[7]
                restaurant_rent=i[8]
                s=Tk()
                L=Label(s,text="********************************************************\n-----------------------------Hôtel Grandé da Louvre------------------------------------- \n NAME : {} \n ADDRESS :{} \n AGE : {} \n NUMBER : {} \nCOUNTRY : {} ROOM RENT : {} \n GAME COST : {} \n RESTAURANT RENT : {} \n".format(name,address,age,number,country,room_rent,game_rent,restaurant_rent),font=("times",40))
                L.pack()
    a_but=Button(root,text="SUBMIT",command=details,fg="blue",font=("times",40))
    a_but.grid(row=6,column=0)
    c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
    c1_but.grid(row=6,column=4)
    root.mainloop()

def total_bill():
    global root
    root.destroy()
    root=Tk()
    room_rent=StringVar()
    game_rent=StringVar()
    restaurant_rent=StringVar()
    tot_bill=StringVar()
    a_id=IntVar()
    a_id=Entry(root,width=60,font=30)
    a_l=Label(root,text="Enter Customer Id number : ",font=("times",20),width=40)
    a_l.grid(row=1,column=0)
    a_id.grid(row=1,column=1)
    def details():
        file=open("Hotel2.dat","rb")
        l=pickle.load(file)
        for i in l:
            if i[0]==a_id.get():
                room_rent=i[6]
                game_rent=i[7]
                restaurant_rent=i[8]
                tot_bill=room_rent+game_rent+restaurant_rent
                s=Tk()
                str(room_rent)
                str(restaurant_rent)
                str(game_rent)
                L=Label(s,text="\n ~~~~Hôtel Grandé da Louvre~~~~\n ****CUSTOMER BILLING ****\n CUSTOMER NAME: {}\n ROOM RENT : Rs.{}\n GAME BILL : Rs. {}\n RESTAURANT BILL : Rs.{}\n---------------------------------------------------------------\n TOTAL AMOUNT : Rs. {}.".format(i[1],room_rent,restaurant_rent,game_rent,tot_bill),font=("times",30))
                L.pack()
    a_but=Button(root,text="SUBMIT",command=details,fg="blue",font=("times",40))
    a_but.grid(row=6,column=0)
    c1_but=Button(root,text="HOME",command=home,fg="blue",font=("times",40))
    c1_but.grid(row=6,column=4)
    root.mainloop()
    
def finish():
    global root
    from tkinter import messagebox
    messagebox.showinfo("EXIT","THANK YOU")
    root.destroy()    
    
def home():
    '''**************************************************
    Press |         To
   -------+----------------------------
      1   | Enter Guest Details.
      2   | Enter Booking Details.
      3   | Select Room Type.
      4   | Display Guest Details.
      5   | Gaming Informations.
      6   | Generate Total Bill Amount.
      7   | Finish Up and Exit.
       **************************************************'''
    global root
    root.destroy()
    root=Tk()
    l1=Label(root,text="Hôtel Grandé da Louvre",fg="yellow",bg="black",font=("times",40))
    l1.grid(row=0,column=1)
    b1=Button(root,text="Enter Guest Details.",command=show,width=40,fg="red",font=("times",20))
    b1.grid(row=1,column=1)
    b2=Button(root,text="Enter Booking Details.",command=booking_details,fg="red",width=40,font=("times",20))
    b2.grid(row=2,column=1)
    b3=Button(root,text="Select Room Type.",command=room_rent,fg="red",width=40,font=("times",20))
    b3.grid(row=3,column=1)
    b4=Button(root,text="Select Restaurant Type.",command=restaurant,fg="red",width=40,font=("times",20))
    b4.grid(row=4,column=1)
    b5=Button(root,text="Display Guest Details.",command=guest_details,fg="red",width=40,font=("times",20))
    b5.grid(row=6,column=1)
    b6=Button(root,text="Gaming Informations.",command=game_play,fg="red",width=40,font=("times",20))
    b6.grid(row=5,column=1)
    l=Label(root,text="Please Enter one by one")
    l.grid(row=10,column=1)
    b9=Button(root,text="Payment Method.",command=payment,fg="red",width=40,font=("times",20))
    b9.grid(row=7,column=1)
    b7=Button(root,text="Generate Total Bill Amount.",command=total_bill,fg="red",width=40,font=("times",20))
    b7.grid(row=8,column=1)
    b8=Button(root,text="Finish Up and Exit.",fg="red",command=finish,width=40,font=("times",20))
    b8.grid(row=9,column=1)
    root.mainloop()


home()
