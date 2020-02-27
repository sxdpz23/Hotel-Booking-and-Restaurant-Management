from tkinter import*
import os
import random

"""
#!/usr/bin/python

hostname = 'localhost'
username = 'USERNAME'
password = 'PASSWORD'
database = 'DBNAME'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print firstname, lastname


print "Using MySQLdb…"
import MySQLdb
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print "Using pymysql…"
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print "Using mysql.connector…"
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()
"""

root=Tk() #creating a window
root.geometry("2000x4000") #window geometry
root.title("Restaurant Management System") #window title

#========================= Background Image ============================
C = Canvas(root, bg="blue")
fname = PhotoImage(file = "img5.png")
background_lbl = Label(root, image=fname)
background_lbl.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()

def qParse():
    creds = 'tempfile-rb.txt' # This just sets the variable creds to 'tempfile.temp'

#=============================== Login Logic =============================== 
    def Signup(): #function for signing up
        global pwordE #globals variables
        global nameE
        global r1
 
        r1 = Toplevel(root) #makes a child window 
        r1.title('Login') 
        intruction = Label(r1, text='Please Enter new Credidentials\n').grid(row=0, column=0, sticky=E) 
        nameL = Label(r1, text='New Username: ').grid(row=1, column=0, sticky=W) #uses Username as text
        pwordL = Label(r1, text='New Password: ').grid(row=2, column=0, sticky=W)  
        nameE = Entry(r1)
        nameE.grid(row=1, column=1) 
        pwordE = Entry(r1, show='*')
        pwordE.grid(row=2, column=1)  #difference 'show="*"'replace the text with *, like a password box
        signupButton = Button(r1, text='Signup', command=FSSignup).grid(columnspan=2, sticky=W) 

        r1.mainloop() 
 
    def FSSignup():
        with open(creds, 'w') as f: #creates a document
            f.write(nameE.get()) #storing the input
            f.write('\n') #splits the line
            f.write(pwordE.get()) 
            f.close() #closes the file
        r1.destroy()
        Login() #calling Login Function
 
    def Login():
        global nameEL
        global pwordEL
        global r2
 
        r2 = Toplevel(root) 
        r2.title('Login')
        intruction = Label(r2, text='Please Login\n').grid(sticky=E)
        nameL = Label(r2, text='Username: ').grid(row=1, sticky=W)
        pwordL = Label(r2, text='Password: ').grid(row=2, sticky=W)
        nameEL = Entry(r2)
        nameEL.grid(row=1, column=1)
        pwordEL = Entry(r2, show='*')
        pwordEL.grid(row=2, column=1)
        loginB = Button(r2, text='Login', command=CheckLogin).grid(columnspan=2, sticky=W)  
        rmuser = Button(r2, text='Delete User', fg='red', command=DelUser).grid(columnspan=2, sticky=W)
        r2.mainloop()
 
    def CheckLogin(): 
        with open(creds) as f:
            data = f.readlines() #taking the entire document & putting it into the data variable
            uname = data[0].rstrip() #data[0], 0 is the first line, 1 is the second and so on.
            pword = data[1].rstrip() #removing the inputted new line

##------------------------ Hotel Management Coding ------------------------------ 
        if nameEL.get() == uname and pwordEL.get() == pword: #checks if entered data is correct
            ro = Toplevel(r2)  # Opens new window
            ro.title('Hotel Bookings')
            ro.geometry('2000x4000')  # Makes the window a certain size

            #-------------- Background Image --------------------
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

                C2 = Canvas(roots, bg="blue")
                filename = PhotoImage(file = "img3.png")
                background_label = Label(roots, image=filename)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)
                C2.grid()

                func(roots)

            def func(roots):
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
            
        else:
            r = TopLevel(r2)
            r.title('Login Issue')
            r.geometry('500x500')
            rlbl = Label(r, text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()
 
    def DelUser():
        os.remove(creds) #removes the file
        r2.destroy() 
        Signup() #going back to the start!
 
    if os.path.isfile(creds):
        Login()
    else: 
        Signup()


def Ref():
    x=random.randint(10908,500876) #for a random value in rand
    randomRef=str(x)
    rand.set(randomRef)

    if (ChickenBurger.get()==""):
        CoChickenBurger=0
    else:
        CoChickenBurger=float(ChickenBurger.get())

    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())

    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())

    if (Frankie.get()==""):
        CoFrankie=0
    else:
        CoFrankie=float(Frankie.get())
        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())
     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

#======================= Cost Logic ===============================
    CostofChickenBurger =CoChickenBurger * 40
    CostofDrinks=CoD * 40
    CostofNoodles = CoNoodles* 80
    CostofSoup = CoSoup * 50
    CostFrankie = CoFrankie* 40
    CostSandwich=CoSandwich * 50

    CostofMeal= "Rs", str('%.2f' % (CostofChickenBurger+CostofDrinks+CostofNoodles+CostofSoup+CostFrankie+CostSandwich))
    PayTax=((CostofChickenBurger+CostofDrinks+CostofNoodles+CostofSoup+CostFrankie+CostSandwich) * 0.2)
    TotalCost=(CostofChickenBurger+CostofDrinks+CostofNoodles+CostofSoup+CostFrankie+CostSandwich)
    Ser_Charge= ((CostofChickenBurger+CostofDrinks+CostofNoodles+CostofSoup+CostFrankie+CostSandwich)/99)
    Service = "Rs", str ('%.2f' % Ser_Charge)
    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))
    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    ChickenBurger.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Frankie.set("")
    Sandwich.set("")    
#========================== Variables Assignments ==========================
rand = StringVar()
ChickenBurger=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Frankie=StringVar()
Sandwich=StringVar()

#======================= Restaraunt Info 1 ======================
lblChickenBurger= Label(root, font=('arial', 16, 'bold'),text="Chicken Burger (Rs 45)",bd=16,fg="blue",anchor="w").grid(row=0, column=0)
txtChickenBurger=Entry(root, font=('arial',16,'bold'),textvariable=ChickenBurger,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=0,column=1)
lblNoodles= Label(root, font=('arial', 16, 'bold'),text="Noodles (Rs 80)",bd=16,fg="blue",anchor="w").grid(row=1, column=0)
txtNoodles=Entry(root, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=1,column=1)
lblSoup= Label(root, font=('arial', 16, 'bold'),text="Soup (Rs 80)",bd=16,fg="blue",anchor="w").grid(row=2, column=0)
txtSoup=Entry(root, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=2,column=1)
lblFrankie= Label(root, font=('arial', 16, 'bold'),text="Frankie (Rs 60)",bd=16,fg="blue",anchor="w").grid(row=3, column=0)
txtFrankie=Entry(root, font=('arial',16,'bold'),textvariable=Frankie,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=3,column=1)
lblSandwich= Label(root, font=('arial', 16, 'bold'),text="Sandwich (Rs 50)",bd=16,fg="blue",anchor="w").grid(row=4, column=0)
txtSandwich=Entry(root, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=4,column=1)
lblDrinks= Label(root, font=('arial', 16, 'bold'),text="Drinks (Rs 80)",bd=16,fg="blue",anchor="w").grid(row=5, column=0)
txtDrinks=Entry(root, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=5,column=1)

#=================== RESTAURANT INFO 2 ====================
lblReference= Label(root, font=('arial', 16, 'bold'),text="Reference",bd=16,fg="blue",anchor="w").grid(row=0, column=2)
txtReference=Entry(root, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=0,column=3)
lblCost= Label(root, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,fg="blue",anchor="w").grid(row=1, column=2)
txtCost=Entry(root, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=1,column=3)
lblService= Label(root, font=('arial', 16, 'bold'),text="Service Charge",bd=16,fg="blue",anchor="w").grid(row=2, column=2)
txtService=Entry(root, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=2,column=3)
lblStateTax= Label(root, font=('arial', 16, 'bold'),text="GST",bd=16,fg="blue",anchor="w").grid(row=3, column=2)
txtStateTax=Entry(root, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=3,column=3)
lblSubTotal= Label(root, font=('arial', 16, 'bold'),text="Sub Total",bd=16,fg="blue",anchor="w").grid(row=4, column=2)
txtSubTotal=Entry(root, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=4,column=3)
lblTotalCost= Label(root, font=('arial', 16, 'bold'),text="Total Cost",bd=16,fg="blue",anchor="w").grid(row=5, column=2)
txtTotalCost=Entry(root, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="cyan",justify='right').grid(row=5,column=3)

#===================== Buttons ==========================
btnTotal=Button(root,padx=16,pady=8,bd=16,fg="red",font=('arial',16,'bold'),width=10,text="Total",bg="cyan",command=Ref).grid(row=7,column=1)
btnReset=Button(root,padx=16,pady=8,bd=16,fg="red",font=('arial',16,'bold'),width=10,text="Reset",bg="cyan",command=Reset).grid(row=7,column=2)
btnExit=Button(root,padx=16,pady=8,bd=16,fg="red",font=('arial',16,'bold'),width=10,text="Exit",bg="cyan",command=qExit).grid(row=7,column=3)
btnHM=Button(root,padx=16,pady=8,bd=16,fg="red",font=('arial',16,'bold'),width=15,text="Hotel Management",bg="yellow",command=qParse).grid(row=9,column=4)

root.mainloop()