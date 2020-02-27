from tkinter import *
import random
import time
import datetime
import os

#-------------------MySQL Connection details------------------
hostname = 'localhost'
username = 'root'
password = ''
database = 'pythonconn'
import pymysql

ro = Tk()  # Opens new window
ro.title('Hotel Bookings')
ro.geometry('1510x810')  # Makes the window a certain size

#---------------- ro Background Image --------------------
C = Canvas(ro, bg="blue")
filename = PhotoImage(file = "img2.png")
background_lab = Label(ro, image=filename)
background_lab.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()

lab1 = Label(ro, text=" HOTEL ROOM BOOKING ", font=('arial',30,'bold'), fg="white", width=30, bg= "brown",bd=10).grid(row=0,column=1,columnspan=3)
global bid

def qExit():
    ro.destroy()
def qNew():
    ro0 = Toplevel(ro)  # Opens new window
    ro0.title('Hotel Bookings')
    ro0.geometry('1510x810')  # Makes the window a certain size

#----------------ro0 Background Image --------------------
    C0 = Canvas(ro0, bg="blue")
    filename0 = PhotoImage(file = "img5.jpg")
    background_lab = Label(ro0, image=filename0)
    background_lab.place(x=1, y=1, relwidth=1, relheight=1)
    C0.grid()

    def Reset():
        first_name.set("")
        middle_name.set("")
        last_name.set("")
        address.set("")
        contact_id.set("")
        email_id.set("")

        from_date.set("")
        till_date.set("")
        no_of_rooms.set("")
        floor.set("")
        room_no.set("")
        payment_status.set("")
        planning.set("")

    def qLeave():
        ro0.destroy()
                
    def qDone():
        global first
        if (first_name.get() == ""):
            from tkinter import messagebox
            messagebox.showinfo("Empty box!", "Please enter your name")
        else:
            first = str(first_name.get())

        ro01 = Toplevel(ro0)  # Opens new window
        ro01.title('Hotel Bookings')
        ro01.geometry('769x90')  # Makes the window a certain size
        def qOkay():
            ro01.destroy()
            ro0.destroy()
        lab = Label(ro01, text="Your customer details are successfully saved. Hence your desired room is also booked!!", font=('arial',12,'italic'), fg="navy",bg= "white",bd=10,anchor='w').grid(row=0,column=0)
        btnOK = Button(ro01, padx=1, pady=1, bd=8, font=('arial', 13, 'italic'), width=10, text="Okay",fg="navy",bg="white", command=qOkay).grid(row=1, column=1)

        myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
        def doQuery( conn ) :
            cur = conn.cursor()
            """first='Shantanu'
            last='Prajapati'
            user='Blunderbuzz'
            passw='13452'  """
            #    cur.execute( "SELECT uname, pname FROM employee" )
            #cur.execute( "INSERT INTO `employee` VALUES (%s,%s,%s,%s);",(first, last, user, passw) )
            cur.execute( "SELECT * FROM employee WHERE fname=%s;",(first) )
            for firstname, lastname, username, password in cur.fetchall() :
                print (firstname, lastname, username, password) 
            print ("Connection Successful!!!")
        doQuery( myConnection )
        myConnection.close() 
    
    #------------------------------------- Assignments ------------------------------------
    first_name = StringVar()
    middle_name = StringVar()
    last_name = StringVar()
    address = StringVar()
    contact_id = StringVar()
    email_id = StringVar()
    bid = 1
    """myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
    def doQuery( conn ) :
        cur = conn.cursor()
        cur.execute("SELECT `booking_id` FROM `room_booking` WHERE `booking_id`=%s;",(bid))
        for booking_id in cur.fetchall() :
            print (booking_id)
            b_id=int(booking_id)+int(1)
           
    doQuery( myConnection )
    myConnection.close()"""

    booking_id = IntVar()
    booking_id.set(bid)
    from_date = StringVar()
    till_date = StringVar()
    no_of_rooms = IntVar()
    floor = IntVar()
    room_no = StringVar()
    payment_status = StringVar()
    planning = StringVar()
    
    #------------------------------------- Labels & Grid --------------------------------------
    lblFN = Label(ro0, font=('arial', 20, 'bold'), text="First Name :- ", bd=16, fg="blue", anchor="w").grid(row=2, column=0)
    txtFN = Entry(ro0, font=('arial', 16, 'bold'), textvariable=first_name, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=2, column=1)
    lblMN = Label(ro0, font=('arial', 20, 'bold'), text="Middle Name :- ", bd=16, fg="blue", anchor="w").grid(row=3, column=0)
    txtMN = Entry(ro0, font=('arial', 16, 'bold'), textvariable=middle_name, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=3, column=1)
    lblLN = Label(ro0, font=('arial', 20, 'bold'), text="Last Name :- ", bd=16, fg="blue", anchor="w").grid(row=4, column=0)
    txtLN = Entry(ro0, font=('arial', 16, 'bold'), textvariable=last_name, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=4, column=1)
    lblAdd = Label(ro0, font=('arial', 20, 'bold'), text="Address :- ", bd=16, fg="blue", anchor="w").grid(row=5, column=0)
    txtAdd = Entry(ro0, font=('arial', 16, 'bold'), textvariable=address, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=5, column=1)
    lblCon = Label(ro0, font=('arial', 20, 'bold'), text="Contact Number :- ", bd=16, fg="blue", anchor="w").grid(row=6, column=0)
    txtCon = Entry(ro0, font=('arial', 16, 'bold'), textvariable=contact_id, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=6, column=1)
    lblEmid = Label(ro0, font=('arial', 20, 'bold'), text="Email Address :- ", bd=16, fg="blue", anchor="w").grid(row=7, column=0)
    txtEmid = Entry(ro0, font=('arial', 16, 'bold'), textvariable=email_id, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=7, column=1)

    lblBid = Label(ro0, font=('arial', 20, 'bold'), text="Booking id :- ", bd=16, fg="blue", anchor="w").grid(row=0, column=1)
    txtBid = Entry(ro0, font=('arial', 16, 'bold'), textvariable=booking_id, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=0, column=2)
    lblHead = Label(ro0, font=('arial', 25, 'bold'), text="Please Fill out ALL the following boxes for successful booking :- ", bd=16, fg="blue", anchor="w").grid(row=1, column=0, columnspan=4)
    lblFD = Label(ro0, font=('arial', 20, 'bold'), text="From Date :- ", bd=16, fg="blue", anchor="w").grid(row=2, column=2)
    txtFD = Entry(ro0, font=('arial', 16, 'bold'), textvariable=from_date, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=2, column=3)
    lblTD = Label(ro0, font=('arial', 20, 'bold'), text="Till Date :- ", bd=16, fg="blue", anchor="w").grid(row=3, column=2)
    txtTD = Entry(ro0, font=('arial', 16, 'bold'), textvariable=till_date, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=3, column=3)
    lblNoR = Label(ro0, font=('arial', 20, 'bold'), text="No. of Rooms :- ", bd=16, fg="blue", anchor="w").grid(row=4, column=2)
    txtNoR = Entry(ro0, font=('arial', 16, 'bold'), textvariable=no_of_rooms, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=4, column=3)
    lblFloor = Label(ro0, font=('arial', 20, 'bold'), text="Which floor :- ", bd=16, fg="blue", anchor="w").grid(row=5, column=2)
    txtFloor = Entry(ro0, font=('arial', 16, 'bold'), textvariable=floor, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=5, column=3)
    lblPS = Label(ro0, font=('arial', 20, 'bold'), text="Payment Status :- ", bd=16, fg="blue", anchor="w").grid(row=6, column=2)
    txtPS = Entry(ro0, font=('arial', 16, 'bold'), textvariable=payment_status, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=6, column=3)
    lblPlan = Label(ro0, font=('arial', 20, 'bold'), text="AC/Non-AC :- ", bd=16, fg="blue", anchor="w").grid(row=7, column=2)
    txtPlan = Entry(ro0, font=('arial', 16, 'bold'), textvariable=planning, bd=10, insertwidth=4, bg="cyan", justify='right').grid(row=7, column=3)
        
    btnRst = Button(ro0, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=14, text="Reset", bg="yellow", command=Reset).grid(row=8, column=1)
    btnDone = Button(ro0, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=14, text="Done", bg="yellow", command=qDone).grid(row=8, column=2)
    btnLeave = Button(ro0, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=14, text="Leave", bg="yellow", command=qLeave).grid(row=8, column=3)

    ro0.mainloop()
    
def qFind():
        ro.destroy()
def qUpdate():
        ro.destroy()
def qCancel():
        ro.destroy()

# ------------------------------ Buttons ---------------------------------------
btnNew = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=14, text="New Booking", bg="orange", command=qNew).grid(row=3, column=1, sticky='w')
btnFind = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=14, text="Find Bookings", bg="orange", command=qFind).grid(row=3, column=2, sticky='e')
btnUpdate = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=32, text="Update Booking Information", bg="orange", command=qUpdate).grid(row=4, column=1, columnspan=3)
btnCancel = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=14, text="Cancel Bookings", bg="orange", command=qCancel).grid(row=5, column=1, sticky='w')
btnExt = Button(ro, padx=16, pady=8, bd=16, fg="red", font=('arial', 16, 'bold'), width=14, text="Exit App", bg="orange", command=qExit).grid(row=5, column=2, sticky='e')

ro.mainloop()
