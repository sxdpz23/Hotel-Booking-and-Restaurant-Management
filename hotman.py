from tkinter import *
import random
import time
import datetime
import os


ro = Tk()  # Opens new window
ro.title('Hotel Bookings')
ro.geometry('2000x4000')  # Makes the window a certain size

#---------------- Background Image --------------------
C1 = Canvas(ro, bg="blue")
filname = PhotoImage(file = "img2.png")
background_lab = Label(ro, image=filname)
background_lab.place(x=0, y=0, relwidth=1, relheight=1)
C1.grid()

#------------- Labels --------------------
lab1 = Label(ro, text="First Name: ", font=('arial',20,'bold'), fg="white",bg= "brown",bd=10,anchor='w').grid(row=0,column=0)
lab2 = Label(ro, text="Middle Name: ", font=('arial',20,'bold'), fg="white",bg= "brown",bd=10,anchor='w').grid(row=1,column=0)
lab3 = Label(ro, text="Last Name: ", font=('arial',20,'bold'), fg="white",bg= "brown",bd=10,anchor='w').grid(row=2,column=0)
lab4 = Label(ro, text="Type: ", font=('arial',20,'bold'), fg="white", bg= "brown", bd=10,anchor='w').grid(row=3,column=0)
lab5 = Label(ro, text="Location: ", font=('arial',20,'bold'), fg="white", bg= "brown", bd=10,anchor='w').grid(row=4,column=0)
##lab6 = Label(ro, text="Hotel Selection:- ", font=('arial',20,'bold'), fg="white", bg= "brown",bd=10,anchor='w').grid(row=6,column=0)      
#---------------- Entries -------------------- ( These now puts a text box waiting for input )
ent1 = Entry(ro, font=('arial',16,'bold'), bd=10,insertwidth=4,bg="brown",justify='left').grid(row=0, column=1)
ent2 = Entry(ro, font=('arial',16,'bold'), bd=10,insertwidth=4,bg="brown",justify='left').grid(row=1, column=1)
ent3 = Entry(ro, font=('arial',16,'bold'), bd=10,insertwidth=4,bg="brown",justify='left').grid(row=2, column=1)

def lqExit():
    ro.destroy()

def lplace(place):
    roots=Toplevel(ro)
    roots.title("Bookings in " + place + " Branch")
    roots.geometry("2000x4000")
    func(roots)

def func(roots):
    C2 = Canvas(roots, bg="blue")
    filename = PhotoImage(file = "img3.png")
    background_label = Label(roots, image=filename)
    background_label.place(x=1, y=1, relwidth=1, relheight=1)
    C2.grid()
    def qTotal():
        if (Days.get() == ""):
            CoDays = 0
        else:
            CoDays = int(Days.get())

        if (Per.get() == ""):
            CoPer = 0
        else:
            CoPer = int(Per.get())

        if (Rooms.get() == ""):
            CoRooms = 0
        else:
            CoRooms = int(Rooms.get())

        if (e1.get() == ""):
            fDay = 0
        else:
            fDay = int(e1.get())

        if (e2.get() == ""):
            fMonth = 0
        else:
            fMonth = int(e2.get())

        if (e3.get() == ""):
            fYear = 0
        else:
            fYear = int(e3.get())

        if (e4.get() == ""):
            tDay = 0
        else:
            tDay = int(e4.get())

        if (e5.get() == ""):
            tMonth = 0
        else:
            tMonth = int(e5.get())

        if (e6.get() == ""):
            tYear = 0
        else:
            tYear = int(e6.get())

        if (Total.get() == ""):
            CoTotal = 0
        #--------------------------- Costs Logic --------------------------------------
        CostofDays = CoDays * 700
        CostofPer = CoPer * 300
        CostofRooms = CoRooms * 1000
        TotalCost = "Rs.", str('%.2f' % (CostofDays + CostofRooms))
        Total.set(TotalCost)

    def qExit():
        roots.destroy()

    def Reset():
        Days.set("")
        Per.set("")
        Rooms.set("")
        e1.set("")
        e2.set("")
        e3.set("")
        e4.set("")
        e5.set("")
        e6.set("")
        Total.set("")

    #------------------------------------- Assignments ------------------------------------
    Days = StringVar()
    Per = StringVar()
    Rooms = StringVar()
    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4 = StringVar()
    e5 = StringVar()
    e6 = StringVar()
    Total = StringVar()

    #------------------------------------- Labels & Grid --------------------------------------
    lblDays = Label(roots, font=('arial', 20, 'bold'), text="Number of days need room for---", bd=16, fg="blue", anchor="w").grid(row=0, column=0)
    txtDays = Entry(roots, font=('arial', 16, 'bold'), textvariable=Days, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=0, column=2)
    lblPer = Label(roots, font=('arial', 20, 'bold'), text="Number of Persons are staying---", bd=16, fg="blue", anchor="w").grid(row=1, column=0)
    txtPer = Entry(roots, font=('arial', 16, 'bold'), textvariable=Per, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=1, column=2)
    lblRooms = Label(roots, font=('arial', 20, 'bold'), text="Number of rooms needed---", bd=16, fg="blue", anchor="w").grid(row=2, column=0)
    txtRooms = Entry(roots, font=('arial', 16, 'bold'), textvariable=Rooms, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=2, column=2)
    lblFromDate = Label(roots, text="Room needed From Date---", font=('arial', 20, 'bold'), fg="blue", bd=16, anchor='w').grid(row=3, column=0)
    txtday = Entry(roots, font=('arial', 16, 'bold'), textvariable=e1, bd=8, insertwidth=2, bg="cyan", justify='right').grid(row=3, column=1)
    txtmonth = Entry(roots, font=('arial', 16, 'bold'), textvariable=e2, bd=8, insertwidth=2, bg="cyan", justify='right').grid(row=3, column=2)
    txtyear = Entry(roots, font=('arial', 16, 'bold'), textvariable=e3, bd=8, insertwidth=2, bg="cyan", justify='right').grid(row=3, column=3)
    lblTilDate = Label(roots, font=('arial', 20, 'bold'), text="Room needed To Date---(dd,mm,yy)", bd=16, fg="blue", anchor="w").grid(row=4, column=0)
    txtday = Entry(roots, font=('arial', 16, 'bold'), textvariable=e4, bd=8, insertwidth=2, bg="cyan", justify='right').grid(row=4, column=1)
    txtmonth = Entry(roots, font=('arial', 16, 'bold'), textvariable=e5, bd=8, insertwidth=2, bg="cyan", justify='right').grid(row=4, column=2)
    txtyear = Entry(roots, font=('arial', 16, 'bold'), textvariable=e6, bd=8, insertwidth=2, bg="cyan", justify='right').grid(row=4, column=3)
    lblTotalCost = Label(roots, font=('arial', 20, 'bold'), text="Total Cost ---", bd=16, fg="purple", anchor="w").grid(rows=5, column=0)
    txtTotalCost = Entry(roots, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=5, column=2)

    # ------------------------------ Buttons ---------------------------------------
    btnTot = Button(roots, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Total", bg="yellow", command=qTotal).grid(row=7, column=1)
    btnRst = Button(roots, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Reset", bg="yellow", command=Reset).grid(row=7, column=2)
    btnExt = Button(roots, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Exit", bg="yellow", command=qExit).grid(row=7, column=3)

#-------------- Radio Button --------------------
var_chk = IntVar()
rd1 = Radiobutton(ro, text="A\C", variable=var_chk, value=1, bg="brown").grid(row=3, column=1, sticky=W)
rd2 = Radiobutton(ro, text="NON A\C", variable=var_chk, value=2, bg="brown").grid(row=3, column=1, sticky=E)

#--------------- Buttons --------------------
btnDah = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Dahanu", bg="orange", command=lambda: lplace("Dahanu")).grid(row=4, column=1)
btnBoi = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Boisar", bg="orange", command=lambda: lplace("Boisar")).grid(row=4, column=2)
btnPal = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Palghar", bg="orange", command=lambda: lplace("Palghar")).grid(row=4, column=3)
btnVir = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Virar", bg="orange", command=lambda: lplace("Virar")).grid(row=5, column=1)
btnBor = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Borivali", bg="orange", command=lambda: lplace("Borivali")).grid(row=5, column=2)
btnChu = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Churchgate", bg="orange", command=lambda: lplace("Churchgate")).grid(row=5, column=3)
btnEx = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=10, text="Exit", bg="orange", command=lqExit).grid(row=6, column=2)

ro.mainloop()

