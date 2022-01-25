from tkinter import *
import datetime
from tkinter import messagebox 
s = datetime.datetime.now()
a = s.date()
admin=Tk()
admin.title("Bank Management System")
admin.state("zoomed")
admin.resizable(width=TRUE,height=TRUE)

bg = PhotoImage(file = "bank.png")
cg=PhotoImage(file="logo.png")
ad=PhotoImage(file="logo5.png")
def main_body():
    def login():
        from tkinter import messagebox
        import sqlite3 as s
        user = entry1.get()
        password = entry2.get()


        if var.get()==1:
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            re=cur.execute("select * from Administrator where Email=? and password=? ",(user,password))
            er=re.fetchall()
            if (len(user) == 0 or len(password) == 0):
                messagebox.showwarning("Validation", "id/password is not blank")
            else:

                if er:
                    messagebox.showinfo("welcome", "Login success")
                    adminis()
                    con.close()
                else:
                    messagebox.showerror("Invalid ", "either id and password")
        elif var.get()==2:
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            em=cur.execute("select * from Employee where Email=? and password=?",(user,password))
            emp=em.fetchall()
            if (len(user) == 0 or len(password) == 0):
                messagebox.showwarning("Validation", "id/password is not blank")
            else:
                if emp:
                    messagebox.showinfo("welcome", "Login success")
                    bankstaff()
                    
                    con.close()
                else:
                    messagebox.showerror("Invalid ", "either id and password")
        elif var.get()==3:
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            bs=cur.execute("select * from Customer where Email=? and passwo=?",(user,password))
            ba1=bs.fetchall()
            
            
            if (len(user) == 0 or len(password) == 0):
                messagebox.showwarning("Validation", "id/password is not blank")
                
            else:

                if ba1:
                    messagebox.showinfo("welcome", "Login success")
                    customer(ba1)
                    
                    
                    
                    con.close()
                    
                else:
                    messagebox.showerror("Invalid ", "either id and password")
                    button4.place(relx=0.65,rely=0.40)
        else:
           messagebox.showwarning("Validation", "Please The Option") 
    def clear_it():
        entry1.delete(0, "end")
        entry2.delete(0, "end")
    logo=Frame(admin)
    logo.configure(bg="#ebe6e6")
    logo.place(x=0,y=0,relwidth=1,relheight=0.15)
    label1 = Label( logo, image = bg)
    label1.place(relx = 0.25, rely = 0.05) 
    label2 = Label( logo, image = bg)
    label2.place(relx = 0.75, rely = 0.05) 
    adminwork=Frame(admin)
    adminwork.configure(bg="#00ffa6")
    adminwork.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
    label23 = Label(logo, text="Bank Management System",  bg="#ebe6e6", font="Courier 25 bold")
    label23.place(relx=0.36,rely=0.2)
    label4=Label(adminwork, text="LOGIN", bg="#00ffa6", font="calibri 25 bold")
    label4.place(relx=0.45,rely=0.05)
    # display Date
    label11 = Label(adminwork, text="Date", bg="#00ffa6", font="arial 10 bold")
    label0 = Label(adminwork, text=a,  bg="#00ffa6", font="arial 10 bold")
    label11.place(relx=0.8,rely=0.1)
    label0.place(relx=0.85,rely=0.1)

    # Username
    label1 = Label(adminwork, text="EmailID", bg="#00ffa6", font="arial 13 bold")
    entry1 = Entry(adminwork, width=50)
    label1.place(relx=0.4,rely=0.20)
    entry1.place(relx=0.4,rely=0.25)
    entry1.focus()
    # Password
    label2 = Label(adminwork, text="Password", bg="#00ffa6", font="arial 13 bold")
    entry2 = Entry(adminwork, width=50,show="*")
    label2.place(relx=0.4,rely=0.4)
    entry2.place(relx=0.4,rely=0.45)
    entry2.focus()
    # Radiobuttons
    var=IntVar()
    # Administrator
    checkbutton1 = Radiobutton(adminwork, text="Administrator", variable=var,value=1,  bg="#00ffa6", font="arial 13 bold")
    checkbutton1.place(relx=0.39,rely=0.55)
    # Bank Staff
    checkbutton2 = Radiobutton(adminwork, text="Bank Staff", variable=var,value=2,  bg="#00ffa6", font="arial 13 bold")
    checkbutton2.place(relx=0.50,rely=0.55)
    # Customer
    checkbutton3 = Radiobutton(adminwork, text="Customer", variable=var, value=3, bg="#00ffa6", font="arial 13 bold")
    checkbutton3.place(relx=0.60,rely=0.55)
    # Clear
    button1 = Button(adminwork, text="Clear", width=10,  bg="White", font="arial 13 bold",command=clear_it)
    button1.place(relx=0.39,rely=0.65)
    # Quit
    button2 = Button(adminwork, text="Quit", width=10,  bg="White", font="arial 13 bold")
    button2.place(relx=0.50,rely=0.65)
    # Submit
    button3 = Button(adminwork, text="Submit", width=15,  bg="White", height=2, font="arial 13 bold",command=login)
    button3.place(relx=0.42,rely=0.75)
    button4 = Button(adminwork, text="Forget Password", width=15,  bg="White", height=2, font="arial 10 bold",command=otp)
    
        
def adminis():
    logoa=Frame(admin)
    logoa.configure(bg="#ebe6e6")
    logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
    label1 = Label( logoa, image = bg)
    label1.place(relx = 0.25, rely = 0.05) 
    label2 = Label( logoa, image = bg)
    label2.place(relx = 0.75, rely = 0.05) 
    label3=Label(logoa,text="Administrator panel",bg="#ebe6e6",font="Courier 25 bold")
    label3.place(relx=0.39,rely=0.2)       
    def logout():
        from tkinter import messagebox
        messagebox.showinfo("Log Out", "Thank you")

        main_body()
    admins=Frame(admin)
    admins.configure(bg="#00ffa6")
    admins.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
    #All Ten Functions
    #Account Details
    def checkAc():
        logoch=Frame(admin)
        logoch.configure(bg="#ebe6e6")
        logoch.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoch, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoch, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        label5=Label(logoch,text="Check Account Details",bg="#ebe6e6",font="Courier 25 bold")
        label3=Label(logoch,text="Administrator panel",bg="#ebe6e6",font="Courier 25 bold")
        label3.place(relx=0.39,rely=0.2)  

        def cleAr():
            FirstName.delete(0,"end")
            Phonenu.delete(0,"end")
            Email.delete(0,"end")
            address.delete(0,"end")
            dob.delete(0,"end")
            PassWord.delete(0,"end")
            sex.delete(0,"end")
            InAm.delete(0,"end")
            cred.delete(0,"end")
            

           
        def details():
            FirstName.delete(0,"end")
            Phonenu.delete(0,"end")
            Email.delete(0,"end")
            address.delete(0,"end")
            dob.delete(0,"end")
            PassWord.delete(0,"end")
            sex.delete(0,"end")
            InAm.delete(0,"end")
            cred.delete(0,"end")

            import sqlite3 as s
            a=int(AcnU.get())
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            de=cur.execute("Select Accno From Customer ")
            acc=de.fetchall()

            add=[]
            for i in acc:
                for sa in i:
                    add.append(sa)
            
            if not(a in add):
                from tkinter import messagebox
                messagebox.showerror("Not Match","Account Number is not valid")
            else:
                de=cur.execute("Select * from Customer WHERE Accno=?",[AcnU.get()])
                ri=de.fetchall()

                FirstName.insert(0,"")
                FirstName.insert(0,ri[0][1])
                Phonenu.insert(0,"")
                Phonenu.insert(0,ri[0][2])
                Email.insert(0,"")
                Email.insert(0,ri[0][3])
                address.insert(0,"")
                address.insert(0,ri[0][4])
                dob.insert(0,"")
                dob.insert(0,ri[0][5])
                PassWord.insert(0,"")
                PassWord.insert(0,ri[0][6])
                sex.insert(0,"")
                sex.insert(0,ri[0][7])
                InAm.insert(0,"")
                InAm.insert(0,ri[0][8])
                cred.insert(0,"")
                cred.insert(0,ri[0][9])
                con.close()  
        
        admins.place_forget()
        work=Frame(admin)
        work.configure(bg="#00ffa6")
        work.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
                    
        label5=Label(logoch,text="Check Account Details",bg="#ebe6e6",font="Courier 25 bold")
        label5.place(relx=0.36,rely=0.2)

        #Account Number
        AcNu = Label(work, text="Account Number",bg="#00ffa6",font="arial 13 bold")
        AcnU = Entry(work, width=50)
        AcNu.place(relx=0.05, rely=0.1)
        AcnU.place(relx=0.15, rely=0.1)
        #Name
        Firstname = Label(work, text="Name",bg="#00ffa6",font="arial 13 bold")
        FirstName = Entry(work, width=50)
        Firstname.place(relx=0.05, rely=0.20)
        FirstName.place(relx=0.15, rely=0.20)
        #Phone Number
        Pnumber = Label(work, text="Phone Number",bg="#00ffa6",font="arial 13 bold")
        Phonenu = Entry(work, width=50)
        Pnumber.place(relx=0.05, rely=0.60)
        Phonenu.place(relx=0.15, rely=0.60)
        #Email
        email = Label(work, text="Email",bg="#00ffa6",font="arial 13 bold")
        Email = Entry(work, width=50)
        email.place(relx=0.05, rely=0.8)
        Email.place(relx=0.15, rely=0.8)
        #Address
        Address = Label(work, text="Address",bg="#00ffa6",font="arial 13 bold")
        address = Entry(work, width=50)
        Address.place(relx=0.05, rely=0.50)
        address.place(relx=0.15, rely=0.50)
        #Date of Birth
        DOB = Label(work, text="Date of Birth",bg="#00ffa6",font="arial 13 bold")
        dob = Entry(work, width=50)
        DOB.place(relx=0.05, rely=0.30)
        dob.place(relx=0.15, rely=0.30)
        #Password
        Password = Label(work, text="Password",bg="#00ffa6",font="arial 13 bold")
        PassWord = Entry(work, width=50)
        Password.place(relx=0.60, rely=0.1)
        PassWord.place(relx=0.7, rely=0.1)
        #Created On
        Cre=Label(work, text="Created-on",bg="#00ffa6",font="arial 13 bold")
        cred = Entry(work, width=50)
        Cre.place(relx=0.60, rely=0.2)
        cred.place(relx=0.7, rely=0.2)
        #Sex
        Sex = Label(work, text="Sex",bg="#00ffa6",font="arial 13 bold")
        sex = Entry(work, width=50)
        Sex.place(relx=0.05, rely=0.70)
        sex.place(relx=0.15, rely=0.70)
        #Intial Amount
        inam = Label(work, text="Intial Amount",bg="#00ffa6",font="arial 13 bold")
        InAm = Entry(work, width=50)
        inam.place(relx=0.05, rely=0.40)
        InAm.place(relx=0.15, rely=0.40)


        #Buttons
        Submit = Button(admin, text="Submit",command=details,font="arial 13 bold")
        Clear = Button(admin, text="Clear",font="arial 13 bold",command=cleAr)
        Quit = Button(admin, text="Quit",font="arial 13 bold",command=adminis)
        Submit.place(relx=0.6, rely=0.4)
        Clear.place(relx=0.66,rely=0.4) 
        Quit.place(relx=0.71, rely=0.4)
    #user Admin
    def userad():
        def creemp():

            def generatew():
                entry1.configure(state=NORMAL)
                entry8.configure(state=NORMAL)

                import datetime
                s = datetime.datetime.now()
                a = s.date()
                entry8.insert(0, "")
                entry8.insert(0, a)

                import sqlite3 as s
                con = s.connect(database="bank.sqlite")
                cur = con.cursor()
                re = cur.execute("Select EmpID from Employee")

                fe = re.fetchall()

                a = []
                for c in fe:
                    for b in c:
                        a.append(b)

                d = a[-1] + 1
                entry1.insert(0, "")
                entry1.insert(0, d)
                entry1.configure(state=DISABLED)
                entry8.configure(state=DISABLED)

            def inserte():

                from tkinter import messagebox
                if var.get() == 1:
                    d = "Male"
                elif var.get() == 2:
                    d = "Female"
                elif var.get() == 3:
                    d = "Other"
                if hvar.get() == 0:
                    messagebox.showwarning("Not selected", "Select the option")
                elif hvar.get() == 1:

                    import sqlite3 as s
                    con = s.connect(database="bank.sqlite")
                    cur = con.cursor()
                    cur.execute("INSERT INTO Employee VALUES(?,?,?,?,?,?,?,?,?,?)",
                                [entry1.get(), entry2.get(), entry3.get(), entry15.get(), entry4.get(), entry5.get(),
                                entry6.get(), entry7.get(),d,entry8.get()])
                    con.commit()
                    messagebox.showinfo("Data Inserted", "All data inserted successfully")

            def cle():
                entry2.delete(0, "end")
                entry3.delete(0, "end")
                entry4.delete(0, "end")
                entry5.delete(0, "end")
                entry6.delete(0, "end")
                entry7.delete(0, "end")
                entry15.delete(0, "end")

            logous=Frame(admin)
            logous.configure(bg="#ebe6e6")
            logous.place(x=0,y=0,relwidth=1,relheight=0.15)
            label1 = Label( logous, image = bg)
            label1.place(relx = 0.25, rely = 0.05) 
            label2 = Label( logous, image = bg)
            label2.place(relx = 0.75, rely = 0.05) 
            CretAc = Frame(admin)
            CretAc.configure(bg="#00ffa6")
            CretAc.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
            label4s8=Label(logous,text="Create Employee",bg="#ebe6e6",font="Courier 25 bold")   
            label4s8.place(relx=0.36,rely=0.2)

            # Account Number
            label1 = Label(CretAc, text="Employee ID", bg="#00ffa6", font="arial 13 bold")
            entry1 = Entry(CretAc, width=30)
            label1.place(relx=0.1, rely=0.1)
            entry1.place(relx=0.25, rely=0.1)

            # First Name
            label2 = Label(CretAc, text="Name", bg="#00ffa6", font="arial 13 bold")
            entry2 = Entry(CretAc, width=30)
            label2.place(relx=0.1, rely=0.2)
            entry2.place(relx=0.25, rely=0.2)

            # Last Name
            label3 = Label(CretAc, text=" Phone Number", bg="#00ffa6", font="arial 13 bold")
            entry3 = Entry(CretAc, width=30)
            label3.place(relx=0.1, rely=0.3)
            entry3.place(relx=0.25, rely=0.3)

            # Initial Amount
            label4 = Label(CretAc, text="Email", bg="#00ffa6", font="arial 13 bold")
            entry15 = Entry(CretAc, width=30)
            label4.place(relx=0.1, rely=0.4)
            entry15.place(relx=0.25, rely=0.4)

            # Initial Amount

            label5 = Label(CretAc, text=" Address", bg="#00ffa6", font="arial 13 bold")
            entry4 = Entry(CretAc, width=30)
            label5.place(relx=0.1, rely=0.5)
            entry4.place(relx=0.25, rely=0.5)
            # Address
            label6 = Label(CretAc, text="Date of Birth", bg="#00ffa6", font="arial 13 bold")
            entry5 = Entry(CretAc, width=30)
            label6.place(relx=0.1, rely=0.6)
            entry5.place(relx=0.25, rely=0.6)

            # Phone Number
            label7 = Label(CretAc, text="Password", bg="#00ffa6", font="arial 13 bold")
            entry6 = Entry(CretAc, width=30)
            label7.place(relx=0.1, rely=0.7)
            entry6.place(relx=0.25, rely=0.7)

            # Gender
            var = IntVar()
            label8 = Label(CretAc, text="Gender", bg="#00ffa6", font="arial 13 bold")
            radio3 = Radiobutton(CretAc, text="Male", bg="#00ffa6", font="arial 13 bold", variable=var, value=1)
            radio4 = Radiobutton(CretAc, text="Female", bg="#00ffa6", font="arial 13 bold", variable=var, value=2)
            radio5 = Radiobutton(CretAc, text="Other", bg="#00ffa6", font="arial 13 bold", variable=var, value=3)
            label8.place(relx=0.1, rely=0.8)
            radio3.place(relx=0.20, rely=0.8)
            radio4.place(relx=0.30, rely=0.8)
            radio5.place(relx=0.40, rely=0.8)
            # DOB
            label9 = Label(CretAc, text="Salary", bg="#00ffa6", font="arial 13 bold")
            entry7 = Entry(CretAc, width=30)
            label9.place(relx=0.1, rely=0.9)
            entry7.place(relx=0.25, rely=0.9)

            # Generate Account Number
            button1 = Button(CretAc, text="Generate", font="arial 13 bold", command=generatew)
            button1.place(relx=0.50, rely=0.1)

            # Email
            label10 = Label(CretAc, text="Date of Joining", bg="#00ffa6", font="arial 13 bold")
            entry8 = Entry(CretAc, width=30)
            label10.place(relx=0.50, rely=0.2)
            entry8.place(relx=0.60, rely=0.2)

            # Clear
            button2 = Button(CretAc, text="Clear", font="arial 13 bold", command=cle)
            button2.place(relx=0.50, rely=0.3)
            # Quit
            button3 = Button(CretAc, text="Quit", font="arial 13 bold", command=userad)
            button3.place(relx=0.60, rely=0.3)
            # Checkbutton
            hvar = IntVar()
            check1 = Checkbutton(CretAc, text="I here by declare all these details are correct.", bg="#00ffa6",
                                font="arial 13 bold", variable=hvar, onvalue=1, offvalue=0)
            check1.place(relx=0.50, rely=0.4)
            # submit
            Sub = Button(CretAc, text="Submit", font="arial 13 bold", command=inserte)
            Sub.place(relx=0.5, rely=0.5)
        def checkAce():
            def cleAr():
                FirstName.delete(0, "end")
                Phonenu.delete(0, "end")
                Email.delete(0, "end")
                address.delete(0, "end")
                dob.delete(0, "end")
                PassWord.delete(0, "end")
                sex.delete(0, "end")
                InAm.delete(0, "end")
                cred.delete(0, "end")

            def details():
                FirstName.delete(0, "end")
                Phonenu.delete(0, "end")
                Email.delete(0, "end")
                address.delete(0, "end")
                dob.delete(0, "end")
                PassWord.delete(0, "end")
                sex.delete(0, "end")
                InAm.delete(0, "end")
                cred.delete(0, "end")

                import sqlite3 as s
                con = s.connect(database="bank.sqlite")
                cur = con.cursor()
                de=cur.execute("Select EmpID From Employee ")
                acc=de.fetchall()
                add = []
                for i in acc:
                    for sa in i:
                        add.append(sa)
                
                aw=int(AcnU.get())       
                if not(aw in add):
                    from tkinter import messagebox
                    messagebox.showerror("Not Match","Employee Id is not valid")
                
                
                else: 
                    de = cur.execute("Select * from Employee WHERE EmpID=?", [AcnU.get()])
                    ri = de.fetchall()
                    FirstName.insert(0, "")
                    FirstName.insert(0, ri[0][1])
                    Phonenu.insert(0, "")
                    Phonenu.insert(0, ri[0][2])
                    Email.insert(0, "")
                    Email.insert(0, ri[0][3])
                    address.insert(0, "")
                    address.insert(0, ri[0][4])
                    dob.insert(0, "")
                    dob.insert(0, ri[0][5])
                    PassWord.insert(0, "")
                    PassWord.insert(0, ri[0][6])
                    sex.insert(0, "")
                    sex.insert(0, ri[0][7])
                    InAm.insert(0, "")
                    InAm.insert(0, ri[0][8])
                    cred.insert(0,"")
                    cred.insert(0,ri[0][9])
                    con.close()

            admins.place_forget()
            logouscj=Frame(admin)
            logouscj.configure(bg="#ebe6e6")
            logouscj.place(x=0,y=0,relwidth=1,relheight=0.15)
            label1 = Label( logouscj, image = bg)
            label1.place(relx = 0.25, rely = 0.05) 
            label2 = Label( logouscj, image = bg)
            label2.place(relx = 0.75, rely = 0.05) 
            work = Frame(admin)
            work.configure(bg="#00ffa6")
            work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
            label4ss8=Label(logouscj,text="Check Employee details",bg="#ebe6e6",font="Courier 25 bold")
            label4ss8.place(relx=0.36,rely=0.2)
            # Employee id
            AcNu = Label(work, text="Employee ID", bg="#00ffa6", font="arial 13 bold")
            AcnU = Entry(work, width=50)
            AcNu.place(relx=0.05, rely=0.1)
            AcnU.place(relx=0.15, rely=0.1)
            # Name
            Firstname = Label(work, text="Name", bg="#00ffa6", font="arial 13 bold")
            FirstName = Entry(work, width=50)
            Firstname.place(relx=0.05, rely=0.20)
            FirstName.place(relx=0.15, rely=0.20)
            # Phone Number
            Pnumber = Label(work, text="Phone Number", bg="#00ffa6", font="arial 13 bold")
            Phonenu = Entry(work, width=50)
            Pnumber.place(relx=0.05, rely=0.60)
            Phonenu.place(relx=0.15, rely=0.60)
            # Email
            email = Label(work, text="Email", bg="#00ffa6", font="arial 13 bold")
            Email = Entry(work, width=50)
            email.place(relx=0.05, rely=0.8)
            Email.place(relx=0.15, rely=0.8)
            # Address
            Address = Label(work, text="Address", bg="#00ffa6", font="arial 13 bold")
            address = Entry(work, width=50)
            Address.place(relx=0.05, rely=0.50)
            address.place(relx=0.15, rely=0.50)
            # Date of Birth
            DOB = Label(work, text="Date of Birth", bg="#00ffa6", font="arial 13 bold")
            dob = Entry(work, width=50)
            DOB.place(relx=0.05, rely=0.30)
            dob.place(relx=0.15, rely=0.30)
            # Password
            Password = Label(work, text="Password", bg="#00ffa6", font="arial 13 bold")
            PassWord = Entry(work, width=50)
            Password.place(relx=0.60, rely=0.1)
            PassWord.place(relx=0.7, rely=0.1)
            # Date of joining
            Cre = Label(work, text="Date of joining", bg="#00ffa6", font="arial 13 bold")
            cred = Entry(work, width=50)
            Cre.place(relx=0.60, rely=0.2)
            cred.place(relx=0.7, rely=0.2)
            # Sex
            Sex = Label(work, text="Salary", bg="#00ffa6", font="arial 13 bold")
            sex = Entry(work, width=50)
            Sex.place(relx=0.05, rely=0.70)
            sex.place(relx=0.15, rely=0.70)
            # Salary
            inam = Label(work, text="Sex", bg="#00ffa6", font="arial 13 bold")
            InAm = Entry(work, width=50)
            inam.place(relx=0.05, rely=0.40)
            InAm.place(relx=0.15, rely=0.40)

            # Buttons
            Submit = Button(admin, text="Submit", command=details, font="arial 13 bold")
            Clear = Button(admin, text="Clear", font="arial 13 bold", command=cleAr)
            Quit = Button(admin, text="Quit", font="arial 13 bold", command=userad)
            Quit.place(relx=0.72,rely=0.4)
            Submit.place(relx=0.6, rely=0.4)
            Clear.place(relx=0.66, rely=0.4)
        def updateemp():
            def uo():
                textfield.delete("1.0","end")
                entry2.delete(0,"end")
                entry5.delete(0,"end")
                entry7.delete(0,"end")
                entry4.delete(0,"end")
                entry6.delete(0,"end")
                entry3.delete(0,"end")
                entry64.delete(0,"end")
                en4.delete(0,"end")
                
                import sqlite3 as s
                con=s.connect(database="bank.sqlite")
                cur=con.cursor()
                up=cur.execute("Select * from Employee WHERE EmpID=?",[entry1.get()])
                pu=up.fetchall()
                a=[]             
                for c in pu:                 
                    for b in c:                     
                        a.append(b)
                de=cur.execute("Select EmpID From Employee ")
                acc=de.fetchall()
                ab=int(entry1.get())
                accno=[]
                for i in acc:
                    for b in i:
                        accno.append(b)
                if not(ab in accno):
                    from tkinter import messagebox
                    messagebox.showerror("Not Match","Account Number is not valid")
                else:
                    
                    textfield.insert(END,"Employee ID:\t\t "+ str(a[0])+ "\n""\n")
                    textfield.insert(END,"Name:\t\t "+ a[1]+ "\n""\n")
                    textfield.insert(END,"Phone Number:\t\t "+ a[2] + "\n""\n")
                    textfield.insert(END,"Email:\t\t "+ a[3] + "\n""\n")
                    textfield.insert(END,"Address:\t\t "+ a[4] + "\n""\n")
                    textfield.insert(END,"DOB:\t\t "+ a[5] + "\n""\n")
                    textfield.insert(END,"Password:\t\t "+ a[6] + "\n""\n")
                    textfield.insert(END,"Sex:\t\t "+ str(a[8]) + "\n""\n")
                    textfield.insert(END,"Salary:\t\t "+ str(a[7]) + "\n""\n")
                    entry2.insert(0,"")
                    entry2.insert(0,a[1])
                    entry5.insert(0,"")
                    entry5.insert(0,a[2])
                    entry7.insert(0,"")
                    entry7.insert(0,a[3])
                    entry4.insert(0,"")
                    entry4.insert(0,a[4])
                    entry6.insert(0,"")
                    entry6.insert(0,a[5])
                    entry3.insert(0,"")
                    entry3.insert(0,a[6])
                    entry64.insert(0,"")
                    entry64.insert(0,a[7])
                    en4.insert(0,"")
                    en4.insert(0,a[8])
                    con.close()
            def update():
                from tkinter import messagebox
                import sqlite3 as s
                con=s.connect(database="bank.sqlite")
                cur=con.cursor()
                cur.execute("UPDATE Employee SET  Ename =(?) ,Phno = (?) ,Email = (?),DOB=(?), password = (?),Salary =(?),adde=(?) WHERE EmpID =(?)",[entry2.get(),entry5.get(),entry7.get(),entry6.get(),entry3.get(),entry64.get(),entry4.get(),entry1.get()])
                messagebox.showinfo("Data Updated","Data Updated Successfuly")  

                con.commit()
                  
                up=cur.execute("Select * from Employee WHERE EmpID=?",[entry1.get()])
                pu=up.fetchall()
                a=[]             
                for c in pu:                 
                    for b in c:                     
                        a.append(b)
                textfield.delete("1.0","end")
                textfield.insert(END,"Employee ID:\t\t "+ str(a[0])+ "\n""\n")
                textfield.insert(END,"Name:\t\t "+ a[1]+ "\n""\n")
                textfield.insert(END,"Phone Number:\t\t "+ a[2] + "\n""\n")
                textfield.insert(END,"Email:\t\t "+ a[3] + "\n""\n")
                textfield.insert(END,"Address:\t\t "+ a[4] + "\n""\n")
                textfield.insert(END,"DOB:\t\t "+ a[5] + "\n""\n")
                textfield.insert(END,"Password:\t\t "+ a[6] + "\n""\n")
                textfield.insert(END,"Sex:\t\t "+ str(a[8]) + "\n""\n")
                textfield.insert(END,"Salary:\t\t "+ str(a[7]) + "\n""\n")
                con.close()
            def clews():
                entry1.delete(0,"end")
                textfield.delete("1.0","end")
                entry2.delete(0,"end")
                entry5.delete(0,"end")
                entry7.delete(0,"end")
                entry4.delete(0,"end")
                entry6.delete(0,"end")
                entry3.delete(0,"end")
                entry64.delete(0,"end")
                en4.delete(0,"end")


                
                        
            logousup=Frame(admin)
            logousup.configure(bg="#ebe6e6")
            logousup.place(x=0,y=0,relwidth=1,relheight=0.15)
            label1 = Label( logousup, image = bg)
            label1.place(relx = 0.25, rely = 0.05) 
            label2 = Label( logousup, image = bg)
            label2.place(relx = 0.75, rely = 0.05) 
            adminwork=Frame(admin)
            adminwork.configure(bg="#00ffa6")
            adminwork.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
            label4sa8=Label(logousup,text="Update Employee details",bg="#ebe6e6",font="Courier 25 bold")
            label4sa8.place(relx=0.36,rely=0.2)

            # Account Number
            label1 = Label(adminwork, text="Employee Id", bg="#00ffa6", font="arial 13 bold")
            entry1 = Entry(adminwork, width=40)
            label1.place(relx=0.05, rely=0.1)
            entry1.place(relx=0.20, rely=0.1)

            # First Name
            label2 = Label(adminwork, text=" Name", bg="#00ffa6", font="arial 13 bold")
            entry2 = Entry(adminwork, width=40)
            label2.place(relx=0.5, rely=0.1)
            entry2.place(relx=0.60, rely=0.1)

            #Password
            label3 = Label(adminwork, text="Password", bg="#00ffa6", font="arial 13 bold")
            entry3 = Entry(adminwork, width=40)
            label3.place(relx=0.5, rely=0.2)
            entry3.place(relx=0.6,rely=0.2)

            # Amount
            label4 = Label(adminwork, text="Sex", bg="#00ffa6", font="arial 13 bold")
            en4=Entry(adminwork, width=40)
            label4.place(relx=0.5, rely=0.3)
            en4.place(relx=0.6,rely=0.3)

            # Address
            label5 = Label(adminwork, text="Address", bg="#00ffa6", font="arial 13 bold")
            entry4 = Entry(adminwork, width=40)
            label5.place(relx=0.5, rely=0.4)
            entry4.place(relx=0.6, rely=0.4)

            # Phone Number
            label6 = Label(adminwork, text="Phone Number", bg="#00ffa6", font="arial 13 bold")
            entry5 = Entry(adminwork, width=40)
            label6.place(relx=0.5, rely=0.5)
            entry5.place(relx=0.6, rely=0.5)

            # Gender
            label7 = Label(adminwork, text="Salary", bg="#00ffa6", font="arial 13 bold")
            entry64 = Entry(adminwork, width=40)
            label7.place(relx=0.5, rely=0.6)
            entry64.place(relx=0.6, rely=0.6)

            # DOB
            label8 = Label(adminwork, text="Date of Birth", bg="#00ffa6", font="arial 13 bold")
            entry6 = Entry(adminwork, width=40)
            label8.place(relx=0.5, rely=0.7)
            entry6.place(relx=0.6, rely=0.7)

            # Email
            label9 = Label(adminwork, text="Email", bg="#00ffa6", font="arial 13 bold")
            entry7 = Entry(adminwork, width=40)
            label9.place(relx=0.5, rely=0.8)
            entry7.place(relx=0.6, rely=0.8)

            # Update
            button0 = Button(adminwork, text="Update", bg="White", width=10, font="arial 13 bold",command=update)
            button0.place(relx=0.85, rely=0.1)

            # Submit
            button1 = Button(adminwork, text="Submit", bg="White", font="arial 13 bold",command=uo)
            button1.place(relx=0.2, rely=0.2)

            # Clear
            button2 = Button(adminwork, text="Clear", bg="White", font="arial 13 bold",command=clews)
            button2.place(relx=0.27, rely=0.2)

            # Quit
            button3 = Button(adminwork, text="Quit", bg="White", font="arial 13 bold",command=userad)
            button3.place(relx=0.34, rely=0.2)

            #Text field
            textfield=Text(adminwork, width=40,height=20,font="arial 13")
            textfield.place(relx=0.15,rely=0.3)
        def deleteac():
            from tkinter import ttk
            import sqlite3
            logoausde=Frame(admin)
            logoausde.configure(bg="#ebe6e6")
            logoausde.place(x=0,y=0,relwidth=1,relheight=0.15)
            label1 = Label( logoausde, image = bg)
            label1.place(relx = 0.25, rely = 0.05) 
            label2 = Label( logoausde, image = bg)
            label2.place(relx = 0.75, rely = 0.05) 
            work = Frame(admin)
            work.configure(bg="#00ffa6")
            work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
            label6=Label(logoausde,text="Deleted Account",bg="#ebe6e6",font="Courier 25 bold")
            label6.place(relx=0.36,rely=0.2)
            # connect to the database

            def search():

                for record in tree.get_children():
                    tree.delete(record)


                con1 = sqlite3.connect("bank.sqlite")

                cur1 = con1.cursor()

                cur1.execute("SELECT * From DeleteAcc WHERE Crea=(?) " , [e0.get()])

                rows = cur1.fetchall()
                
                for row in rows:

                    

                    tree.insert("", END, values=row)

            def show():

                for record in tree.get_children():
                    tree.delete(record)


                con1 = sqlite3.connect("bank.sqlite")

                cur1 = con1.cursor()

                cur1.execute("SELECT * FROM DeleteAcc")

                rows = cur1.fetchall()

                for row in rows:

                    

                    tree.insert("", END, values=row)


            def View():

                con1 = sqlite3.connect("bank.sqlite")

                cur1 = con1.cursor()

                cur1.execute("SELECT * FROM DeleteAcc")

                rows = cur1.fetchall()

                for row in rows:

                    

                    tree.insert("", END, values=row)

                con1.close()


            scroll_x = Scrollbar(work, orient=HORIZONTAL)
            scroll_y = Scrollbar(work, orient=VERTICAL)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)


            tree = ttk.Treeview(work, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11"), show='headings', xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.configure(command=tree.xview)
            scroll_y.configure(command=tree.yview)

            tree.column("#1", anchor=CENTER)

            tree.heading("#1", text="Acc No")

            tree.column("#2", anchor=CENTER)

            tree.heading("#2", text="CNAME")

            tree.column("#3", anchor=CENTER)

            tree.heading("#3", text="Phno")

            tree.column("#4", anchor=CENTER)

            tree.heading("#4", text="Email")

            tree.column("#5", anchor=CENTER)

            tree.heading("#5", text="Add")

            tree.column("#6", anchor=CENTER)

            tree.heading("#6", text="DOB")

            tree.column("#7", anchor=CENTER)

            tree.heading("#7", text="passwo")

            tree.column("#8", anchor=CENTER)

            tree.heading("#8", text="Sex")

            tree.column("#9", anchor=CENTER)

            tree.heading("#9", text="Amount")

            tree.column("#10", anchor=CENTER)

            tree.heading("#10", text="Create on")

            tree.column("#11", anchor=CENTER)

            tree.heading("#11", text="Delete")

            tree.place(relx=0, rely=0.15, height=490, width=1600)



            View()

            # Enter Date to Search
            label0 = Label(work, text="Enter Date To Search", bg="#00ffa6", font="arial 13 bold")
            label0.place(relx=0.1, rely=0.05)
            e0 = Entry(work, width=30)
            e0.place(relx=0.25, rely=0.05)


            # Submit
            button1 = Button(work, text="Submit", bg="White", font="arial 13 bold", width=10, command=search)
            button1.place(relx=0.4, rely=0.05)

            # Quit
            button2 = Button(work, text="Quit", bg="White", font="arial 13 bold", width=10, command=userad)
            button2.place(relx=0.9, rely=0.05)

            # Show All Data
            button3= Button(work, text="Show All", bg="White", font="arial 13 bold", width=10, command=show)
            button3.place(relx=0.5, rely=0.05)
        def activeem():
            import sqlite3
            from tkinter import ttk
            logoausac=Frame(admin)
            logoausac.configure(bg="#ebe6e6")
            logoausac.place(x=0,y=0,relwidth=1,relheight=0.15)
            label1 = Label( logoausac, image = bg)
            label1.place(relx = 0.25, rely = 0.05) 
            label2 = Label( logoausac, image = bg)
            label2.place(relx = 0.75, rely = 0.05) 
            work = Frame(admin)
            work.configure(bg="#00ffa6")
            work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
            label4saa8=Label(logoausac,text="Active Employee",bg="#ebe6e6",font="Courier 25 bold")
            label4saa8.place(relx=0.40,rely=0.2)

            # connect to the database

            def search():

                for record in tree.get_children():
                    tree.delete(record)


                con1 = sqlite3.connect("bank.sqlite")

                cur1 = con1.cursor()

                

                ew=cur1.execute("Select DateJoining From Employee")
                r=ew.fetchall()
                aed=[]
                for iw in r:
                    for bw in iw:
                        aed.append(bw)
                
                if not(e0.get()in aed):
                    from tkinter import messagebox
                    messagebox.showwarning("Not valid","Not Found")
                    
                else:
                    cur1.execute("SELECT * From Employee WHERE DateJoining=(?) " , [e0.get()])
                    rows = cur1.fetchall()
                    for row in rows:

                        

                        tree.insert("", END, values=row)

            def show():

                for record in tree.get_children():
                    tree.delete(record)


                con1 = sqlite3.connect("bank.sqlite")

                cur1 = con1.cursor()

                cur1.execute("SELECT * FROM Employee")

                rows = cur1.fetchall()

                for row in rows:

                    

                    tree.insert("", END, values=row)


            def View():

                con1 = sqlite3.connect("bank.sqlite")

                cur1 = con1.cursor()

                cur1.execute("SELECT * FROM Employee")

                rows = cur1.fetchall()

                for row in rows:

                    

                    tree.insert("", END, values=row)

                con1.close()


            scroll_x = Scrollbar(work, orient=HORIZONTAL)
            scroll_y = Scrollbar(work, orient=VERTICAL)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)


            tree = ttk.Treeview(work, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11"), show='headings', xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.configure(command=tree.xview)
            scroll_y.configure(command=tree.yview)

            tree.column("#1", anchor=CENTER)

            tree.heading("#1", text="EmpID")

            tree.column("#2", anchor=CENTER)

            tree.heading("#2", text="ENAME")

            tree.column("#3", anchor=CENTER)

            tree.heading("#3", text="Phno")

            tree.column("#4", anchor=CENTER)

            tree.heading("#4", text="Email")

            tree.column("#5", anchor=CENTER)

            tree.heading("#5", text="Add")

            tree.column("#6", anchor=CENTER)

            tree.heading("#6", text="DOB")

            tree.column("#7", anchor=CENTER)

            tree.heading("#7", text="passwo")

            tree.column("#8", anchor=CENTER)

            tree.heading("#8", text="Salary")

            tree.column("#9", anchor=CENTER)

            tree.heading("#9", text="Sex")

            tree.column("#10", anchor=CENTER)

            tree.heading("#10", text="Date of joining")


            tree.place(relx=0, rely=0.15, height=565, width=1600)



            View()

            # Enter Date to Search
            label0 = Label(work, text="Enter Date To Search", bg="#00ffa6", font="arial 13 bold")
            label0.place(relx=0.1, rely=0.05)
            e0 = Entry(work, width=30)
            e0.place(relx=0.25, rely=0.05)


            # Submit
            button1 = Button(work, text="Submit", bg="White", font="arial 13 bold", width=10, command=search)
            button1.place(relx=0.4, rely=0.05)

            # Quit
            button2 = Button(work, text="Quit", bg="White", font="arial 13 bold", width=10, command=userad)
            button2.place(relx=0.9, rely=0.05)

            # Show All Data
            button3= Button(work, text="Show All", bg="White", font="arial 13 bold", width=10, command=show)
            button3.place(relx=0.5, rely=0.05)
            pass
        
        def actibuser():
            import mwwin as mn
            mn.userac()

            
        logoausa=Frame(admin)
        logoausa.configure(bg="#ebe6e6")
        logoausa.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoausa, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoausa, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        admins.place_forget()
        userwork=Frame(admin)
        userwork.configure(bg="#00ffa6")
        userwork.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
        label478=Label(logoausa,text="User Admin",bg="#ebe6e6",font="Courier 25 bold")
        label478.place(relx=0.45,rely=0.2)
        #create user
        def cret(event):
            createus["bg"]="CYAN"
            creat.place(relx=0.30,rely=0.20)
        def crea(event):
            createus["bg"]="White"
            creat.place_forget()
        createus=Button(userwork,text="Create Employee",font=('arial', 13,'bold'),width=20,command=creemp)
        createus.place(relx=0.1,rely=0.20)
        creat=Label(userwork,text="> Create New Employee ID ", bg="#00ffa6", font="arial 13 bold")
        createus.bind("<Enter>",cret)
        createus.bind("<Leave>",crea)
                
    #delete user
        def de(event):
            dele["bg"]="CYAN"
            deLe.place(relx=0.30,rely=0.30)
        def deL(event):
            dele["bg"]="white"
            deLe.place_forget()
        dele=Button(userwork,text="Check Employee Details",font=('arial', 13,'bold'),width=20,command=checkAce)
        deLe=Label(userwork,text=">Check Employee Details ", bg="#00ffa6", font="arial 13 bold")
        dele.bind("<Enter>",de)
        dele.bind("<Leave>",deL)
        dele.place(relx=0.1,rely=0.30)
        #update user password
        def up(event):
            update["bg"]="CYAN"
            upd.place(relx=0.30,rely=0.40)
        def upe(event):
            update["bg"]="white"
            upd.place_forget()

        update=Button(userwork,text="Update Employee Details",font=('arial', 13,'bold'),width=20,command=updateemp)
        upd=Label(userwork,text="> Update Employee Details",bg="#00ffa6", font="arial 13 bold")
        update.place(relx=0.1,rely=0.40)
        update.bind("<Enter>",up)
        update.bind("<Leave>",upe)
        #Active Management 
        def ac(event):
            active["bg"]="CYAN"
            act.place(relx=0.30,rely=0.50)
        def acti(event):
            active["bg"]="White"
            act.place_forget()  

                

        active=Button(userwork,text="Delete Account",font=('arial', 13,'bold'),width=20,command=deleteac)
        act=Label(userwork,text="> Check Delete Account",bg="#00ffa6", font="arial 13 bold")
        active.place(relx=0.1,rely=0.50)
        active.bind("<Enter>",ac)
        active.bind("<Leave>",acti)
        #Active user
        def actvu(event):
            activeuser["bg"]="CYAN"
            activl.place(relx=0.30,rely=0.60)
        def actile(event):
            activeuser["bg"]="White"
            activl.place_forget()

                
        activeuser=Button(userwork,text="Active Empolyee",font=('arial', 13,'bold'),width=20,command=activeem)
        activl=Label(userwork,text="> Check all Active Customer Access",bg="#00ffa6", font="arial 13 bold")
        activeuser.place(relx=0.1,rely=0.60)
        activeuser.bind("<Enter>",actvu)
        activeuser.bind("<Leave>",actile)
         #Active Accounts
        def actvus(event):
            ActiveAcc["bg"]="CYAN"
            activeAccc.place(relx=0.30,rely=0.70)
        def actiles(event):
            ActiveAcc["bg"]="White"
            activeAccc.place_forget()
        ActiveAcc=Button(userwork,text="Active Accounts",font=('arial', 13,'bold'),width=20,command=actibuser)
        activeAccc=Label(userwork,text="> Check all Active Accounts",bg="#00ffa6", font="arial 13 bold")
        ActiveAcc.place(relx=0.1,rely=0.70)
        ActiveAcc.bind("<Enter>",actvus)
        ActiveAcc.bind("<Leave>",actiles)
        qu=Button(userwork,text="Quit", font="arial 13 bold",command=adminis)
        qu.place(relx=0.9,rely=0.05)
        dat=Label(userwork,text="Date:",bg="#00ffa6", font="arial 10 bold")
        dat.place(relx=0.5,rely=0.02)
        dat1=Label(userwork,text=a,font="arial 10 bold",bg="#00ffa6")
        dat1.place(relx=0.53 ,rely=0.02)

    #Delete User
    def delet():
        logoad=Frame(admin)
        logoad.configure(bg="#ebe6e6")
        logoad.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoad, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoad, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        label44=Label(logoad,text="Delete Account",bg="#ebe6e6",font="Courier 25 bold")
        label44.place(relx=0.36,rely=0.2)
        def cle():
            entry1.delete(0,"end")
        def deleteacno():
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()

            degf=cur.execute("Select * From Customer Where Accno=?",[entry1.get()])
            sdss=degf.fetchall()
            deleacc=[]
            for de in sdss:
                for qw in de:
                    deleacc.append(qw)
            
            
            
            import datetime
            da= datetime.datetime.now()
            a = da.date()
            cur.execute("INSERT OR IGNORE INTO DeleteAcc VALUES(?,?,?,?,?,?,?,?,?,?,?)",[deleacc[0],deleacc[1],deleacc[2],deleacc[3],deleacc[4],deleacc[5],deleacc[6],deleacc[7],deleacc[8],deleacc[9],a])
            cur.execute("DELETE FROM Customer WHERE Accno=(?)",[entry1.get()])


            con.commit()
            messagebox.showinfo("Data deleted","Data Deleted Successfully") 
        def Detai():
            t0.delete("1.0","end")

            
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            up=cur.execute("Select * from Customer WHERE Accno=?",[entry1.get()])
            pu=up.fetchall()
            a=[]             
            for c in pu:                 
                for b in c:                     
                    a.append(b)
            de=cur.execute("Select Accno From Customer ")
            acc=de.fetchall()
            ab=int(entry1.get())
            accno=[]
            for i in acc:
                for b in i:
                    accno.append(b)
            if not(ab in accno):
                from tkinter import messagebox
                messagebox.showerror("Not Match","Account Number is not valid")
            else:
                
                t0.insert(END,"Account Number:\t\t "+ str(a[0])+ "\n""\n")
                t0.insert(END,"Name:\t\t "+ a[1]+ "\n""\n")
                t0.insert(END,"Phone Number:\t\t "+ a[2] + "\n""\n")
                t0.insert(END,"Email:\t\t "+ a[3] + "\n""\n")
                t0.insert(END,"Address:\t\t "+ a[4] + "\n""\n")
                t0.insert(END,"DOB:\t\t "+ a[5] + "\n""\n")
                t0.insert(END,"Password:\t\t "+ a[6] + "\n""\n")
                t0.insert(END,"Sex:\t\t "+ a[7] + "\n""\n")
                t0.insert(END,"Amount:\t\t "+ str(a[8]) + "\n""\n")


         

        work = Frame(admin)
        work.configure(bg="#00ffa6")
        work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)

        # Account Number
        label1 = Label(work, text="Account Number", bg="#00ffa6", font="arial 13 bold")
        entry1 = Entry(work, width=65)
        label1.place(relx=0.3, rely=0.25)
        entry1.place(relx=0.5, rely=0.25)

        label2 = Label(work, text="Details ->", bg="#00ffa6", font="arial 13 bold")
        label2.place(relx=0.3, rely=0.35)

        # Submit
        button0 = Button(work, text="Submit", bg="White", font="arial 13 bold", width=10,command=Detai)
        button0.place(relx=0.3, rely=0.45)

        # Delete
        button1 = Button(work, text="Delete", bg="White", font="arial 13 bold", width=10,command=deleteacno)
        button1.place(relx=0.3, rely=0.55)

        # Clear
        button2 = Button(work, text="Clear", bg="White", font="arial 13 bold", width=10,command=cle)
        button2.place(relx=0.3, rely=0.65)

        # Quit
        button3 = Button(work, text="Quit", bg="White", font="arial 13 bold", width=10,command=adminis)
        button3.place(relx=0.3, rely=0.75)


        #All data contain

        t0 = Text(work, font="arial 10 bold", width=40, height=20)
        t0.place(relx=0.5, rely=0.35)
        
        #Update
    def upd():
        logoaup=Frame(admin)
        logoaup.configure(bg="#ebe6e6")
        logoaup.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoaup, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoaup, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        label52=Label(logoaup,text="Update Account",bg="#ebe6e6",font="Courier 25 bold")
        label52.place(relx=0.40,rely=0.2)

        def uo():
            textfield.delete("1.0","end")
            entry2.delete(0,"end")
            entry5.delete(0,"end")
            entry7.delete(0,"end")
            entry4.delete(0,"end")
            entry6.delete(0,"end")
            entry3.delete(0,"end")
            entry64.delete(0,"end")
            en4.delete(0,"end")
            
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            up=cur.execute("Select * from Customer WHERE Accno=?",[entry1.get()])
            pu=up.fetchall()
            a=[]             
            for c in pu:                 
                for b in c:                     
                    a.append(b)
            de=cur.execute("Select Accno From Customer ")
            acc=de.fetchall()
            ab=int(entry1.get())
            accno=[]
            for i in acc:
                for b in i:
                    accno.append(b)
            if not(ab in accno):
                from tkinter import messagebox
                messagebox.showerror("Not Match","Account Number is not valid")
            else:
                
                textfield.insert(END,"Account Number:\t\t "+ str(a[0])+ "\n""\n")
                textfield.insert(END,"Name:\t\t "+ a[1]+ "\n""\n")
                textfield.insert(END,"Phone Number:\t\t "+ a[2] + "\n""\n")
                textfield.insert(END,"Email:\t\t "+ a[3] + "\n""\n")
                textfield.insert(END,"Address:\t\t "+ a[4] + "\n""\n")
                textfield.insert(END,"DOB:\t\t "+ a[5] + "\n""\n")
                textfield.insert(END,"Password:\t\t "+ a[6] + "\n""\n")
                textfield.insert(END,"Sex:\t\t "+ a[7] + "\n""\n")
                textfield.insert(END,"Amount:\t\t "+ str(a[8]) + "\n""\n")
                entry2.insert(0,"")
                entry2.insert(0,a[1])
                entry5.insert(0,"")
                entry5.insert(0,a[2])
                entry7.insert(0,"")
                entry7.insert(0,a[3])
                entry4.insert(0,"")
                entry4.insert(0,a[4])
                entry6.insert(0,"")
                entry6.insert(0,a[5])
                entry3.insert(0,"")
                entry3.insert(0,a[6])
                entry64.insert(0,"")
                entry64.insert(0,a[7])
                en4.insert(0,"")
                en4.insert(0,a[8])
                con.close()
        def update():
            from tkinter import messagebox
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            cur.execute("UPDATE Customer SET Cname = (?), Phno =(?) ,Email = (?) ,address = (?),DOB = (?),passwo=(?), Sex = (?),Amount =(?) WHERE Accno =(?)",[entry2.get(),entry5.get(),entry7.get(),entry4.get(),entry6.get(),entry3.get(),entry64.get(),en4.get(),entry1.get()])
            messagebox.showinfo("Data Updated","Data Updated Successfuly")                                                                                                                     
            con.commit()
            up=cur.execute("Select * from Customer WHERE Accno=?",[entry1.get()])
            pu=up.fetchall()
            aw=[]             
            for c in pu:                 
                for b in c:                     
                    aw.append(b)
            textfield.delete("1.0",END)
            textfield.insert(END,"Account Number:\t\t "+ str(aw[0])+ "\n""\n")
            textfield.insert(END,"Name:\t\t "+ aw[1]+ "\n""\n")
            textfield.insert(END,"Phone Number:\t\t "+ aw[2] + "\n""\n")
            textfield.insert(END,"Email:\t\t "+ aw[3] + "\n""\n")
            textfield.insert(END,"Address:\t\t "+ aw[4] + "\n""\n")
            textfield.insert(END,"DOB:\t\t "+ aw[5] + "\n""\n")
            textfield.insert(END,"Password:\t\t "+ aw[6] + "\n""\n")
            textfield.insert(END,"Sex:\t\t "+ aw[7] + "\n""\n")
            textfield.insert(END,"Amount:\t\t "+ str(aw[8]) + "\n""\n")
            con.close()  
        def clews():
            entry1.delete(0,"end")
            textfield.delete("1.0","end")
            entry2.delete(0,"end")
            entry5.delete(0,"end")
            entry7.delete(0,"end")
            entry4.delete(0,"end")
            entry6.delete(0,"end")
            entry3.delete(0,"end")
            entry64.delete(0,"end")
            en4.delete(0,"end")


            

        adminwork=Frame(admin)
        adminwork.configure(bg="#00ffa6")
        adminwork.place(x=0,rely=0.15,relwidth=1,relheight=0.85)

        # Account Number
        label1 = Label(adminwork, text="Account Number", bg="#00ffa6", font="arial 13 bold")
        entry1 = Entry(adminwork, width=40)
        label1.place(relx=0.05, rely=0.1)
        entry1.place(relx=0.20, rely=0.1)

        # First Name
        label2 = Label(adminwork, text=" Name", bg="#00ffa6", font="arial 13 bold")
        entry2 = Entry(adminwork, width=40)
        label2.place(relx=0.5, rely=0.1)
        entry2.place(relx=0.60, rely=0.1)

        #Password
        label3 = Label(adminwork, text="Password", bg="#00ffa6", font="arial 13 bold")
        entry3 = Entry(adminwork, width=40)
        label3.place(relx=0.5, rely=0.2)
        entry3.place(relx=0.6,rely=0.2)

        # Amount
        label4 = Label(adminwork, text="Amount", bg="#00ffa6", font="arial 13 bold")
        en4=Entry(adminwork, width=40)
        label4.place(relx=0.5, rely=0.3)
        en4.place(relx=0.6,rely=0.3)

        # Address
        label5 = Label(adminwork, text="Address", bg="#00ffa6", font="arial 13 bold")
        entry4 = Entry(adminwork, width=40)
        label5.place(relx=0.5, rely=0.4)
        entry4.place(relx=0.6, rely=0.4)

        # Phone Number
        label6 = Label(adminwork, text="Phone Number", bg="#00ffa6", font="arial 13 bold")
        entry5 = Entry(adminwork, width=40)
        label6.place(relx=0.5, rely=0.5)
        entry5.place(relx=0.6, rely=0.5)

        # Gender
        label7 = Label(adminwork, text="Gender", bg="#00ffa6", font="arial 13 bold")
        entry64 = Entry(adminwork, width=40)
        label7.place(relx=0.5, rely=0.6)
        entry64.place(relx=0.6, rely=0.6)

        # DOB
        label8 = Label(adminwork, text="Date of Birth", bg="#00ffa6", font="arial 13 bold")
        entry6 = Entry(adminwork, width=40)
        label8.place(relx=0.5, rely=0.7)
        entry6.place(relx=0.6, rely=0.7)

        # Email
        label9 = Label(adminwork, text="Email", bg="#00ffa6", font="arial 13 bold")
        entry7 = Entry(adminwork, width=40)
        label9.place(relx=0.5, rely=0.8)
        entry7.place(relx=0.6, rely=0.8)

        # Update
        button0 = Button(adminwork, text="Update", bg="White", width=10, font="arial 13 bold",command=update)
        button0.place(relx=0.85, rely=0.1)

        # Submit
        button1 = Button(adminwork, text="Submit", bg="White", font="arial 13 bold",command=uo)
        button1.place(relx=0.2, rely=0.2)

        # Clear
        button2 = Button(adminwork, text="Clear", bg="White", font="arial 13 bold",command=clews)
        button2.place(relx=0.27, rely=0.2)

        # Quit
        button3 = Button(adminwork, text="Quit", bg="White", font="arial 13 bold",command=adminis)
        button3.place(relx=0.34, rely=0.2)

        #Text field
        textfield=Text(adminwork, width=40,height=20,font="arial 13")
        textfield.place(relx=0.15,rely=0.3)
            
    #Activty
    def activity():
        logoaac=Frame(admin)
        logoaac.configure(bg="#ebe6e6")
        logoaac.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoaac, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoaac, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        work = Frame(admin)
        work.configure(bg="#00ffa6")
        work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
        label4254=Label(logoaac,text="Activity",bg="#ebe6e6",font="Courier 25 bold")
        label4254.place(relx=0.40,rely=0.2)
        import sqlite3
        from tkinter import ttk

        def search():

            for record in tree.get_children():
                tree.delete(record)


            con1 = sqlite3.connect("bank.sqlite")

            cur1 = con1.cursor()
            cur1.execute("Select Createdon From Customer")
            we=cur1.fetchall()
            act=[]
            for ai in we:
                for ab in ai:
                    act.append(ab)
            if not(e0.get() in act):
                from tkinter import messagebox
                messagebox.showwarning("Not Found ","Invalid Date")
                
            else:
                cur1.execute("SELECT * From Customer WHERE Createdon=(?) " , [e0.get()])

                rows = cur1.fetchall()

                for row in rows:

                    tree.insert("", END, values=row)

        def show():

            for record in tree.get_children():
                tree.delete(record)


            con1 = sqlite3.connect("bank.sqlite")

            cur1 = con1.cursor()

            cur1.execute("SELECT * FROM Customer")

            rows = cur1.fetchall()

            for row in rows:

                tree.insert("", END, values=row)


        def View():

            con1 = sqlite3.connect("bank.sqlite")

            cur1 = con1.cursor()

            cur1.execute("SELECT * FROM Customer")

            rows = cur1.fetchall()

            for row in rows:

                tree.insert("", END, values=row)

            con1.close()


        scroll_x = Scrollbar(work, orient=HORIZONTAL)
        scroll_y = Scrollbar(work, orient=VERTICAL)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)


        tree = ttk.Treeview(work, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"), show='headings', xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.configure(command=tree.xview)
        scroll_y.configure(command=tree.yview)

        tree.column("#1", anchor=CENTER)

        tree.heading("#1", text="Acc No")

        tree.column("#2", anchor=CENTER)

        tree.heading("#2", text="CNAME")

        tree.column("#3", anchor=CENTER)

        tree.heading("#3", text="Phno")

        tree.column("#4", anchor=CENTER)

        tree.heading("#4", text="Email")

        tree.column("#5", anchor=CENTER)

        tree.heading("#5", text="Add")

        tree.column("#6", anchor=CENTER)

        tree.heading("#6", text="DOB")

        tree.column("#7", anchor=CENTER)

        tree.heading("#7", text="passwo")

        tree.column("#8", anchor=CENTER)

        tree.heading("#8", text="Sex")

        tree.column("#9", anchor=CENTER)

        tree.heading("#9", text="Amount")

        tree.column("#10", anchor=CENTER)

        tree.heading("#10", text="Create on")


        tree.place(relx=0, rely=0.15, height=490, width=1600)



        View()

        # Enter Date to Search
        label0 = Label(work, text="Enter Date To Search", bg="#00ffa6", font="arial 13 bold")
        label0.place(relx=0.1, rely=0.05)
        e0 = Entry(work, width=30)
        e0.place(relx=0.25, rely=0.05)


        # Submit
        button1 = Button(work, text="Submit", bg="White", font="arial 13 bold", width=10, command=search)
        button1.place(relx=0.4, rely=0.05)

        # Quit
        button2 = Button(work, text="Quit", bg="White", font="arial 13 bold", width=10, command=adminis)
        button2.place(relx=0.9, rely=0.05)

        # Show All Data
        button3= Button(work, text="Show All", bg="White", font="arial 13 bold", width=10, command=show)
        button3.place(relx=0.5, rely=0.05)
    #Transaction
    def tran():
        from tkinter import ttk
        import sqlite3
        logotr=Frame(admin)
        logotr.configure(bg="#ebe6e6")
        logotr.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logotr, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logotr, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        work = Frame(admin)
        work.configure(bg="#00ffa6")
        work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
        label45=Label(logotr,text="Transaction",bg="#ebe6e6",font="Courier 25 bold")
        label45.place(relx=0.40,rely=0.2)
        # connect to the database

        def search():

            for record in tree.get_children():
                tree.delete(record)

            con1 = sqlite3.connect("bank.sqlite")

            cur1 = con1.cursor()
            wr=cur1.execute("SELECT tranid FROM Tran ")
            ws=wr.fetchall()
            trans=[]
            for we in ws:
                for wb in we:
                    trans.append(wb)
            
            if not(e0.get() in trans):
                from tkinter import messagebox
                messagebox.showwarning("Not match","ID is incorrent")
            else:

                cur1.execute("SELECT * FROM Tran WHERE tranid=? " , [e0.get()])

                rows = cur1.fetchall()

                for row in rows:

                    tree.insert("", END, values=row)

        def show():

            for record in tree.get_children():
                tree.delete(record)

            con1 = sqlite3.connect("bank.sqlite")

            cur1 = con1.cursor()

            ewe=cur1.execute("SELECT * FROM Tran")

            rows = ewe.fetchall()

            for row in rows:

                tree.insert("", END, values=row)


        def View():

            con1 = sqlite3.connect("bank.sqlite")

            cur1 = con1.cursor()

            we=cur1.execute("SELECT * FROM Tran")

            rows = we.fetchall()

            for row in rows:

                tree.insert("", END, values=row)

            con1.close()


        scroll_x = Scrollbar(work, orient=HORIZONTAL)
        scroll_y = Scrollbar(work, orient=VERTICAL)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)


        tree = ttk.Treeview(work, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.configure(command=tree.xview)
        scroll_y.configure(command=tree.yview)

        tree.column("#1", anchor=CENTER)

        tree.heading("#1", text="Transaction ID")

        tree.column("#2", anchor=CENTER)

        tree.heading("#2", text="Amount")

        tree.column("#3", anchor=CENTER)

        tree.heading("#3", text="From Ac")

        tree.column("#4", anchor=CENTER)

        tree.heading("#4", text="To Ac")

        tree.column("#5", anchor=CENTER)

        tree.heading("#5", text="Date Of Transaction")

        tree.column("#6", anchor=CENTER)

        tree.heading("#6", text="Time")

        tree.place(relx=0, rely=0.15, height=495, width=1600)


        View()

        # Enter Date to Search
        label0 = Label(work, text="Enter Transaction ID", bg="#00ffa6", font="arial 13 bold")
        label0.place(relx=0.1, rely=0.05)
        e0 = Entry(work, width=30)
        e0.place(relx=0.25, rely=0.05)


        # Submit
        button1 = Button(work, text="Submit", bg="White", font="arial 13 bold", width=10, command=search)
        button1.place(relx=0.4, rely=0.05)

        # Quit
        button2 = Button(work, text="Quit", bg="White", font="arial 13 bold", width=10, command=adminis)
        button2.place(relx=0.9, rely=0.05)

        # Show All Data
        button3= Button(work, text="Show All", bg="White", font="arial 13 bold", width=10, command=show)
        button3.place(relx=0.5, rely=0.05)
            
    #Create Account
    def Createac():
        def generate():

            entry1.configure(state=NORMAL)
            entry8.configure(state=NORMAL)
            entry1.delete(0,"end")
            entry8.delete(0,"end")
            import datetime 
            s = datetime.datetime.now()
            a = s.date()
            entry8.insert(0,"")
            entry8.insert(0,a)

            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            re=cur.execute("Select Accno from Customer")
                    
            fe=re.fetchall()
                    
            a=[]
            for c in fe:
                for b in c:
                    a.append(b)

                   
            d=a[-1]+1
            entry1.insert(0,"")
            entry1.insert(0,d)
            entry1.configure(state=DISABLED)
            entry8.configure(state=DISABLED)

                
        def insert():
            
            from tkinter import messagebox
            if var.get()==1:
                d="Male"
            elif var.get()==2:
                d="Female"
            elif var.get()==3:
                d="Other"
            if hvar.get()==0:
                messagebox.showwarning("Not selected", "Select the option")
            elif hvar.get()==1:
                if (len(entry2.get()) == 0 or len(entry3.get()) == 0 or len(entry4.get())==0 or len(entry5.get())==0 or  len(entry6.get())==0 or len(entry7.get())==0 or len(entry15.get())==0):
                    messagebox.showwarning("Error", "All Entry Properly")
                else:
                    

                    import sqlite3 as s
                    con=s.connect(database="bank.sqlite")
                    cur=con.cursor()
                    cur.execute("INSERT INTO Customer VALUES(?,?,?,?,?,?,?,?,?,?)",[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),d,entry15.get(),a])
                    con.commit() 
                    messagebox.showinfo("Data Inserted", "All data inserted successfully") 
                    entry2.delete(0, "end")
                    entry3.delete(0, "end")
                    entry4.delete(0, "end")
                    entry5.delete(0, "end")
                    entry6.delete(0, "end")
                    entry7.delete(0, "end")
                    entry15.delete(0,"end")
                    entry1.delete(0,"end")
                    entry8.delete(0,"end")
               

            
        def cl():
                entry2.delete(0, "end")
                entry3.delete(0, "end")
                entry4.delete(0, "end")
                entry5.delete(0, "end")
                entry6.delete(0, "end")
                entry7.delete(0, "end")
                entry15.delete(0,"end")
               
        logocr=Frame(admin)
        logocr.configure(bg="#ebe6e6")
        logocr.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logocr, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logocr, image = bg)
        label2.place(relx = 0.75, rely = 0.05)    
        CretAc = Frame(admin)
        CretAc.configure(bg="#00ffa6")
        CretAc.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
        label4=Label(logocr,text="Create Account",bg="#ebe6e6",font="Courier 25 bold")
        label4.place(relx=0.36,rely=0.2)
        # Account Number
        label1 = Label(CretAc, text="Account Number", bg="#00ffa6", font="arial 13 bold")
        entry1 = Entry(CretAc, width=30)
        label1.place(relx=0.1, rely=0.1)
        entry1.place(relx=0.25, rely=0.1)
        

        # First Name
        label2 = Label(CretAc, text="Name", bg="#00ffa6", font="arial 13 bold")
        entry2 = Entry(CretAc, width=30)
        label2.place(relx=0.1,rely=0.2)
        entry2.place(relx=0.25, rely=0.2)

        # Last Name
        label3 = Label(CretAc, text=" Phone Number", bg="#00ffa6", font="arial 13 bold")
        entry3 = Entry(CretAc, width=30)
        label3.place(relx=0.1, rely=0.3)
        entry3.place(relx=0.25,rely=0.3)

        #Initial Amount
        label4 = Label(CretAc, text="Amount", bg="#00ffa6", font="arial 13 bold")
        entry15 = Entry(CretAc, width=30)
        label4.place(relx=0.1,rely=0.4)
        entry15.place(relx=0.25,rely=0.4)           

        # Initial Amount
        
        label5 = Label(CretAc, text="Email Address", bg="#00ffa6", font="arial 13 bold")
        entry4 = Entry(CretAc, width=30)
        label5.place(relx=0.1,rely=0.5)
        entry4.place(relx=0.25,rely=0.5)
        # Address
        label6 = Label(CretAc, text="Address", bg="#00ffa6", font="arial 13 bold")
        entry5 = Entry(CretAc, width=30)
        label6.place(relx=0.1,rely=0.6)
        entry5.place(relx=0.25,rely=0.6)

        # Phone Number
        label7 = Label(CretAc, text="Date Of Birth", bg="#00ffa6", font="arial 13 bold")
        entry6 = Entry(CretAc, width=30)
        label7.place(relx=0.1,rely=0.7)
        entry6.place(relx=0.25,rely=0.7)

        # Gender
        var=IntVar()
        label8 = Label(CretAc, text="Gender", bg="#00ffa6", font="arial 13 bold")
        radio3 = Radiobutton(CretAc, text="Male", bg="#00ffa6", font="arial 13 bold",variable=var,value=1)
        radio4 = Radiobutton(CretAc, text="Female", bg="#00ffa6", font="arial 13 bold",variable=var,value=2)
        radio5 = Radiobutton(CretAc, text="Other", bg="#00ffa6", font="arial 13 bold",variable=var,value=3)
        label8.place(relx=0.1,rely=0.8)
        radio3.place(relx=0.20,rely=0.8)
        radio4.place(relx=0.30,rely=0.8)
        radio5.place(relx=0.40,rely=0.8)
        # DOB
        label9 = Label(CretAc, text="Password", bg="#00ffa6", font="arial 13 bold")
        entry7 = Entry(CretAc, width=30)
        label9.place(relx=0.1,rely=0.9)
        entry7.place(relx=0.25,rely=0.9)

        # Generate Account Number
        button1 = Button(CretAc, text="Generate Account Number", font="arial 13 bold",command=generate)
        button1.place(relx=0.50,rely=0.1)

        # Email
        label10 = Label(CretAc, text="Created on", bg="#00ffa6", font="arial 13 bold")
        entry8 = Entry(CretAc, width=30)
        label10.place(relx=0.50,rely=0.2)
        entry8.place(relx=0.60,rely=0.2)

        # Clear
        button2 = Button(CretAc, text="Clear", font="arial 13 bold",command=cl)
        button2.place(relx=0.50,rely=0.3)
        # Quit
        button3 = Button(CretAc, text="Quit", font="arial 13 bold",command=adminis)
        button3.place(relx=0.60,rely=0.3)
        # Checkbutton
        hvar=IntVar()
        check1 = Checkbutton(CretAc, text="I here by declare all these details are correct.", bg="#00ffa6", font="arial 13 bold",variable=hvar,onvalue=1,offvalue=0)
        check1.place(relx=0.50,rely=0.4)
        #submit
        Sub=Button(CretAc,text="Submit",font="arial 13 bold",command=insert)
        Sub.place(relx=0.5,rely=0.5)
    def bE(event):
        createAC["bg"]="CYAN"
        createaC.place(relx=0.42,rely=0.07)
    def Bel(event):
        createAC["bg"]="White"
        createaC.place_forget()
    def ce(event):
        balanceEQ["bg"]="CYAN"
        balanceE.place(relx=0.42,rely=0.07)
    def cel(event):
        balanceEQ["bg"]="White"
        balanceE.place_forget()  
    def dE(event):
        checkAcDe["bg"]="CYAN"
        checkAcde.place(relx=0.42,rely=0.07)
    def dele(event):
        checkAcDe["bg"]="White"
        checkAcde.place_forget()  
    def eE(event):
        balanceWD["bg"]="CYAN"
        balancewi.place(relx=0.42,rely=0.07)       
    def eel(event):
        balanceWD["bg"]="White"
        balancewi.place_forget() 
    def fE(event):
        balanceDP["bg"]="CYAN"
        balanceDe.place(relx=0.42,rely=0.07) 
    def fel(event):
        balanceDP["bg"]="White"
        balanceDe.place_forget() 
    def gE(event):
        balanceDA["bg"]="CYAN"
        deleteac.place(relx=0.42,rely=0.07) 
    def gel(event):
        balanceDA["bg"]="White"
        deleteac.place_forget() 
    def hE(event):
        balanceUA["bg"]="CYAN"
        updateac.place(relx=0.42,rely=0.07)
    def hel(event):
        balanceUA["bg"]="White"
        updateac.place_forget() 
    def iE(event):
        balanceUADM["bg"]="CYAN"
        useradmin.place(relx=0.42,rely=0.07)
    def iel(event):
        balanceUADM["bg"]="White"
        useradmin.place_forget()
    def jE(event):
        balanceACT["bg"]="CYAN"
        activty.place(relx=0.42,rely=0.07)
    def jel(event):
        balanceACT["bg"]="White"
        activty.place_forget()
    def kE(event):
        balanceTR["bg"]="CYAN"
        transactions.place(relx=0.42,rely=0.07)
    def kel(event):
        balanceTR["bg"]="White"
        transactions.place_forget()

    label0=Label(admins,image=cg)
    label0.place(relx=0,rely=0)
    label1=Label(admins, text="Administrator", bg="#00ffa6", font="arial 13 bold")  
    label1.place(relx=0.03,rely=0)
    button0=Button(admins,image=ad,command=logout)
    button0.place(relx=0,rely=0.07)
    label2=Label(admins,text="LogOut",bg="#00ffa6",font="arial 13 bold")
    label2.place(relx=0.03,rely=0.07)
    label3=Label(admins,text="Date:",font="arial 7 bold",bg="#00ffa6")
    label3.place(relx=0.42,rely=0.03)
    label4=Label(admins,text=a,bg="#00ffa6",font="arial 7 bold")
    label4.place(relx=0.44,rely=0.03)
    #Create Account
    createAC=Button(admins,text="Create Account",font=('arial', 13,'bold'),width=20 ,command=Createac)
    createAC.place(relx=0.1,rely=0.20)
    createaC=Label(admins, text="Create Account", bg="#00ffa6", font="arial 13 bold")
    createAC.bind("<Enter>",bE)
    createAC.bind("<Leave>",Bel)
    #Balance Enquiry
    balanceEQ=Button(admins,text="Balance Enquiry",font=('arial',13,'bold'),width=20,command=eQ)
    balanceEQ.place(relx=0.40,rely=0.20)
    balanceE=Label(admins, text="Balance Enquiry", bg="#00ffa6", font="arial 13 bold")
    balanceEQ.bind("<Enter>",ce)
    balanceEQ.bind("<Leave>",cel)
    #Check Account details
    checkAcDe=Button(admins,text="Check Account Details",font=('arial',13,'bold'),width=20,command=checkAc)
    checkAcDe.place(relx=0.70,rely=0.20)
    checkAcde=Label(admins, text="Account details", bg="#00ffa6", font="arial 13 bold") 
    checkAcDe.bind("<Enter>",dE)
    checkAcDe.bind("<Leave>",dele)
    #Balance Withdraw
    balanceWD=Button(admins,text="Balance Withdraw",font=('arial',13,'bold'),width=20,command=Bw)
    balanceWD.place(relx=0.1,rely=0.40)
    balancewi=Label(admins, text="Balance Withdraw", bg="#00ffa6", font="arial 13 bold")
    balanceWD.bind("<Enter>",eE)
    balanceWD.bind("<Leave>",eel)
    #Balance Deposit
    balanceDP=Button(admins,text="Balance Deposit",font=('arial',13,'bold'),width=20,command=BD)
    balanceDP.place(relx=0.40,rely=0.40)
    balanceDe=Label(admins, text="Balance Deposit", bg="#00ffa6", font="arial 13 bold")  
    balanceDP.bind("<Enter>",fE)
    balanceDP.bind("<Leave>",fel)
    #Delete Account
    balanceDA=Button(admins,text="Delete Account ",font=('arial',13,'bold'),width=20,command=delet)
    balanceDA.place(relx=0.70,rely=0.40)
    deleteac=Label(admins, text="Delete Account", bg="#00ffa6", font="arial 13 bold")
    balanceDA.bind("<Enter>",gE)
    balanceDA.bind("<Leave>",gel)
    #Update account
    balanceUA=Button(admins,text="Update Account",font=('arial',13,'bold'),width=20,command=upd)
    balanceUA.place(relx=0.1,rely=0.60)
    updateac=Label(admins, text="Update Account", bg="#00ffa6", font="arial 13 bold") 
    balanceUA.bind("<Enter>",hE)
    balanceUA.bind("<Leave>",hel)
    #User Administration
    balanceUADM=Button(admins,text="User Administration",font=('arial',13,'bold'),width=20,command=userad)
    balanceUADM.place(relx=0.40,rely=0.60)
    useradmin=Label(admins, text="User Administration", bg="#00ffa6", font="arial 13 bold")   
    balanceUADM.bind("<Enter>",iE)
    balanceUADM.bind("<Leave>",iel)
    #Activity
    balanceACT=Button(admins,text="Activity",font=('arial',13,'bold'),width=20,command=activity)
    balanceACT.place(relx=0.70,rely=0.60)
    activty=Label(admins, text="Activity", bg="#00ffa6", font="arial 13 bold")
    balanceACT.bind("<Enter>",jE)
    balanceACT.bind("<Leave>",jel)
    #Transaction
    balanceTR=Button(admins,text="Transaction",font=('arial',13,'bold'),width=20,command=tran)
    balanceTR.place(relx=0.1,rely=0.80)
    transactions=Label(admins, text="Transactions", bg="#00ffa6", font="arial 13 bold")   
    balanceTR.bind("<Enter>",kE)
    balanceTR.bind("<Leave>",kel)

#Customer
def customer(a):
    from tkinter import ttk
    import datetime
    c=[]
    for d in a:
        for e in d:
            c.append(e)
            
    def logout():
        from tkinter import messagebox
        messagebox.showinfo("Log out ","Thank you Visit again")
        main_body()
    def status():

        
        txt.insert(END,"Account Number:\t\t "+ str(c[0])+ "\n""\n")
        txt.insert(END,"Name:\t\t "+ c[1]+ "\n""\n")
        txt.insert(END,"Phone Number:\t\t "+ c[2] + "\n""\n")
        txt.insert(END,"Email:\t\t "+ c[3] + "\n""\n")
        txt.insert(END,"Address:\t\t "+ c[4] + "\n""\n")
        txt.insert(END,"DOB:\t\t "+ c[5] + "\n""\n")
        txt.insert(END,"Password:\t\t "+ c[6] + "\n""\n")
        txt.insert(END,"Sex:\t\t "+ c[7] + "\n""\n")
        txt.insert(END,"Amount:\t\t "+ str(c[8]) + "\n""\n")
    def View():

 
        import sqlite3
        for record in tree.get_children():
            tree.delete(record)
        con1 = sqlite3.connect("bank.sqlite")

        cur1 = con1.cursor()

        cur1.execute("SELECT tranid,amounttra,Fromacco,Toaccou FROM Tran WHERE Fromacco=(?) OR Toaccou=(?) ",[c[0],c[0]])

        rows = cur1.fetchall()

        for row in rows:

            tree.insert("", END, values=row)
        con1.close() 
    def fund():
        mini.place_forget()
        minist.place_forget()
        AccountSta.place_forget()
        Accountta.place_forget()
        accountn.place(relx=0.15,rely=0.30)
        accountent.place(relx=0.30,rely=0.30)
        amount.place(relx=0.15,rely=0.40)
        amounte.place(relx=0.30,rely=0.40)
        trans.place(relx=0.15,rely=0.50)
        close.place(relx=0.27,rely=0.50)
    def statement():
        mini.place_forget()
        minist.place_forget()
        accountn.place_forget()
        accountent.place_forget()
        amount.place_forget()
        amounte.place_forget()
        trans.place_forget()
        close.place_forget()
        Accountta.place_forget()
        tree.place(relx=0.1, rely=0.6)
        quit.place(relx=0.4, rely=0.5)
        View()
 
    def fu():
        accountent.delete("0","end")
        amounte.delete("0","end")
        mini.place_forget()
        minist.place_forget()
        accountn.place_forget()
        accountent.place_forget()
        amount.place_forget()
        amounte.place_forget()
        trans.place_forget()
        close.place_forget()
        AccountSta.place(relx=0.1, rely=0.40)
        Accountta.place(relx=0.3, rely=0.40)
        mini.place(relx=0.1,rely=0.60)
        minist.place(relx=0.3,rely=0.60)
    
    def ase():
        accountent.delete("0","end")
        amounte.delete("0","end")
        mini.place_forget()
        minist.place_forget()
        accountn.place_forget()
        accountent.place_forget()
        amount.place_forget()
        amounte.place_forget()
        trans.place_forget()
        close.place_forget()
        tree.place_forget()
        quit.place_forget()
        AccountSta.place(relx=0.1, rely=0.40)
        Accountta.place(relx=0.3, rely=0.40)
        mini.place(relx=0.1,rely=0.60)
        minist.place(relx=0.3,rely=0.60)

    def transferam():
        b=accountent.get()
        ca=amounte.get()
        import sqlite3 as s
        con=s.connect(database="bank.sqlite")
        cur=con.cursor() 
        de=cur.execute("Select Accno From Customer ")
        acc=de.fetchall()
        accno=[]
        for i in acc:
            for ba in i:
                accno.append(ba)
        if not(int(b) in accno):
            from tkinter import messagebox
            messagebox.showerror("Not Match","Account Number is not valid")
        else:
            from tkinter import messagebox
            import datetime 
            s = datetime.datetime.now()
            a = str(s.date())
            tim=str(s.time())
            wet=cur.execute("SELECT tranid FROM Tran")
            tew=wet.fetchall()
            traw=[]
            for iw in tew:
                for bi in iw:
                    traw.append(bi)
            d=traw[-1]+1
            cur.execute("INSERT INTO Tran VALUES(?,?,?,?,?,?)",[d,ca,c[0],b,a,tim])
            cur.execute("UPDATE Customer SET Amount=Amount-(?) where Accno=(?)",[ca,c[0]])
            cur.execute("UPDATE Customer SET Amount=Amount+(?) where Accno=(?)",[ca,b])
            wsd=cur.execute("SELECT * FROM Customer WHERE Accno=(?) ",[c[0]])
            ewd=wsd.fetchall()
            erew=[]
            for wq in ewd:
                for jh in wq:
                    erew.append(jh)
            txt.delete("1.0",END)
            txt.insert(END,"Account Number:\t\t "+ str(erew[0])+ "\n""\n")
            txt.insert(END,"Name:\t\t "+ erew[1]+ "\n""\n")
            txt.insert(END,"Phone Number:\t\t "+ c[2] + "\n""\n")
            txt.insert(END,"Email:\t\t "+ erew[3] + "\n""\n")
            txt.insert(END,"Address:\t\t "+ erew[4] + "\n""\n")
            txt.insert(END,"DOB:\t\t "+ erew[5] + "\n""\n")
            txt.insert(END,"Password:\t\t "+ erew[6] + "\n""\n")
            txt.insert(END,"Sex:\t\t "+ erew[7] + "\n""\n")
            txt.insert(END,"Amount:\t\t "+ str(erew[8]) + "\n""\n")

            con.commit()
            
            
            messagebox.showinfo("Success","Transfer Successfull")
            
    s = datetime.datetime.now()
    b = s.date()


    logoa=Frame(admin)
    logoa.configure(bg="#ebe6e6")
    logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
    label1 = Label( logoa, image = bg)
    label1.place(relx = 0.25, rely = 0.05) 
    label2 = Label( logoa, image = bg)
    label2.place(relx = 0.75, rely = 0.05) 
    label3=Label(logoa,text="Customer Panel",bg="#ebe6e6",font="Courier 25 bold")
    label3.place(relx=0.39,rely=0.2)       
                
    Cus=Frame(admin)
    Cus.configure(bg="#00ffa6")
    Cus.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
    Date= Label(Cus, text="Date :", bg="#00ffa6")
    label25 = Label(Cus, text=b,  bg="#00ffa6", font="arial 8 bold")
    Date.place(relx=0.42,rely=0.03)
    label25.place(relx=0.45,rely=0.03)
    
    

    label0=Label(Cus,image=cg)
    label0.place(relx=0,rely=0)
    label1=Label(Cus, text="Customer", bg="#00ffa6", font="arial 13 bold")  
    label1.place(relx=0.03,rely=0)
    button0=Button(Cus,image=ad,command=logout)
    button0.place(relx=0,rely=0.07)
    label2=Label(Cus,text="LogOut",bg="#00ffa6",font="arial 13 bold")
    label2.place(relx=0.03,rely=0.07)
        
    #Fund Transfer
    Fundtrans=Button(Cus, text=" Fund Transfer ", font=('arial', 13 ,'bold'), width=20, command=fund)
    Fundtrans.place(relx=0.1, rely=0.20)
    Fundtrans= Label(Cus, text="> Transfer Fund to another account", bg="#00ffa6", font="arial 13 bold")
    Fundtrans.place(relx=0.3, rely=0.20)
    accountn=Label(Cus, text="Account Number", bg="#00ffa6", font="arial 13 bold")
    accountent=Entry(Cus, width=50)
    trans=Button(Cus,text="Transfer Fund",font="arial 13 bold",command=transferam)
    close=Button(Cus,text="Close",font="arial 13 bold",command=fu)
    #Account Statment
    AccountSta= Button(Cus, text=" Account Statement ", font="arial 13 bold", width=20, command=statement)
    AccountSta.place(relx=0.1, rely=0.40)
    Accountta= Label(Cus, text="> Check Transaction", bg="#00ffa6", font="arial 13 bold")
    Accountta.place(relx=0.3, rely=0.40)
    amount=Label(Cus, text="Amount", bg="#00ffa6", font="arial 13 bold")
    amounte=Entry(Cus, width=50)
    
    tree = ttk.Treeview(Cus, column=("c1", "c2", "c3","c4"), show='headings')



    tree.column("#1", anchor=W,stretch=NO,width=70)

    tree.heading("#1", text="TransactionID",anchor=W)

    tree.column("#2", anchor=W,stretch=NO)

    tree.heading("#2", text="Amount",anchor=W)

    tree.column("#3", anchor=W,stretch=NO)

    tree.heading("#3", text="From Account",anchor=W)
    tree.column("#4", anchor=W,stretch=NO)

    tree.heading("#4", text="To Account",anchor=W)
    
    quit= Button(text="Close", font="arial 13 bold", width="7",command=ase)
    #Text Box
    txt = Text(font="arial 13 bold",width=40,height=20)
    txt.place(relx=0.7, rely=0.3)
    
        
    #MiniStatment
    mini=Button(Cus, text=" MiniStatement ", font="arial 13 bold", width=20,command=lambda:satement(a))
    mini.place(relx=0.1,rely=0.60)
    minist= Label(Cus, text="> Ministatement", bg="#00ffa6", font="arial 13 bold")
    minist.place(relx=0.3,rely=0.60)
    status()
    #Bank staff
def bankstaff():
    def logout():
        from tkinter import messagebox
        messagebox.showinfo("Log Out", "Thank you")

        main_body()
    def upde():
        def uo():
            textfield.delete("1.0","end")
            entry2.delete(0,"end")
            entry5.delete(0,"end")
            entry7.delete(0,"end")
            entry4.delete(0,"end")
            entry6.delete(0,"end")
            entry3.delete(0,"end")
            entry64.delete(0,"end")
            en4.delete(0,"end")
            
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            up=cur.execute("Select * from Customer WHERE Accno=?",[entry1.get()])
            pu=up.fetchall()
            a=[]             
            for c in pu:                 
                for b in c:                     
                    a.append(b)
            de=cur.execute("Select Accno From Customer ")
            acc=de.fetchall()
            ab=int(entry1.get())
            accno=[]
            for i in acc:
                for b in i:
                    accno.append(b)
            if not(ab in accno):
                from tkinter import messagebox
                messagebox.showerror("Not Match","Account Number is not valid")
            else:
                
                textfield.insert(END,"Account Number:\t\t "+ str(a[0])+ "\n""\n")
                textfield.insert(END,"Name:\t\t "+ a[1]+ "\n""\n")
                textfield.insert(END,"Phone Number:\t\t "+ a[2] + "\n""\n")
                textfield.insert(END,"Email:\t\t "+ a[3] + "\n""\n")
                textfield.insert(END,"Address:\t\t "+ a[4] + "\n""\n")
                textfield.insert(END,"DOB:\t\t "+ a[5] + "\n""\n")
                textfield.insert(END,"Password:\t\t "+ a[6] + "\n""\n")
                textfield.insert(END,"Sex:\t\t "+ a[7] + "\n""\n")
                textfield.insert(END,"Amount:\t\t "+ str(a[8]) + "\n""\n")
                entry2.insert(0,"")
                entry2.insert(0,a[1])
                entry5.insert(0,"")
                entry5.insert(0,a[2])
                entry7.insert(0,"")
                entry7.insert(0,a[3])
                entry4.insert(0,"")
                entry4.insert(0,a[4])
                entry6.insert(0,"")
                entry6.insert(0,a[5])
                entry3.insert(0,"")
                entry3.insert(0,a[6])
                entry64.insert(0,"")
                entry64.insert(0,a[7])
                en4.insert(0,"")
                en4.insert(0,a[8])
                con.close()
        def update():
            from tkinter import messagebox
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            cur.execute("UPDATE Customer SET Cname = (?), Phno =(?) ,Email = (?) ,address = (?),DOB = (?),passwo=(?), Sex = (?),Amount =(?) WHERE Accno =(?)",[entry2.get(),entry5.get(),entry7.get(),entry4.get(),entry6.get(),entry3.get(),entry64.get(),en4.get(),entry1.get()])
            messagebox.showinfo("Data Updated","Data Updated Successfuly")                                                                                                                     
            con.commit()
            con.close()  

        def clew():
            entry1.delete(0,"end")
            textfield.delete("1.0","end")
            entry2.delete(0,"end")
            entry5.delete(0,"end")
            entry7.delete(0,"end")
            entry4.delete(0,"end")
            entry6.delete(0,"end")
            entry3.delete(0,"end")
            entry64.delete(0,"end")
            en4.delete(0,"end")




        logoa=Frame(admin)
        logoa.configure(bg="#ebe6e6")
        logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoa, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoa, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        label3=Label(logoa,text="Update Account",bg="#ebe6e6",font="Courier 25 bold")
        label3.place(relx=0.39,rely=0.2) 
        adminwork=Frame(admin)
        adminwork.configure(bg="#00ffa6")
        adminwork.place(x=0,rely=0.15,relwidth=1,relheight=0.85)

        # Account Number
        label1 = Label(adminwork, text="Account Number", bg="#00ffa6", font="arial 13 bold")
        entry1 = Entry(adminwork, width=40)
        label1.place(relx=0.05, rely=0.1)
        entry1.place(relx=0.20, rely=0.1)

        # First Name
        label2 = Label(adminwork, text=" Name", bg="#00ffa6", font="arial 13 bold")
        entry2 = Entry(adminwork, width=40)
        label2.place(relx=0.5, rely=0.1)
        entry2.place(relx=0.60, rely=0.1)

        #Password
        label3 = Label(adminwork, text="Password", bg="#00ffa6", font="arial 13 bold")
        entry3 = Entry(adminwork, width=40)
        label3.place(relx=0.5, rely=0.2)
        entry3.place(relx=0.6,rely=0.2)

        # Amount
        label4 = Label(adminwork, text="Amount", bg="#00ffa6", font="arial 13 bold")
        en4=Entry(adminwork, width=40)
        label4.place(relx=0.5, rely=0.3)
        en4.place(relx=0.6,rely=0.3)

        # Address
        label5 = Label(adminwork, text="Address", bg="#00ffa6", font="arial 13 bold")
        entry4 = Entry(adminwork, width=40)
        label5.place(relx=0.5, rely=0.4)
        entry4.place(relx=0.6, rely=0.4)

        # Phone Number
        label6 = Label(adminwork, text="Phone Number", bg="#00ffa6", font="arial 13 bold")
        entry5 = Entry(adminwork, width=40)
        label6.place(relx=0.5, rely=0.5)
        entry5.place(relx=0.6, rely=0.5)

        # Gender
        label7 = Label(adminwork, text="Gender", bg="#00ffa6", font="arial 13 bold")
        entry64 = Entry(adminwork, width=40)
        label7.place(relx=0.5, rely=0.6)
        entry64.place(relx=0.6, rely=0.6)

        # DOB
        label8 = Label(adminwork, text="Date of Birth", bg="#00ffa6", font="arial 13 bold")
        entry6 = Entry(adminwork, width=40)
        label8.place(relx=0.5, rely=0.7)
        entry6.place(relx=0.6, rely=0.7)

        # Email
        label9 = Label(adminwork, text="Email", bg="#00ffa6", font="arial 13 bold")
        entry7 = Entry(adminwork, width=40)
        label9.place(relx=0.5, rely=0.8)
        entry7.place(relx=0.6, rely=0.8)

        # Update
        button0 = Button(adminwork, text="Update", bg="White", width=10, font="arial 13 bold",command=update)
        button0.place(relx=0.85, rely=0.1)

        # Submit
        button1 = Button(adminwork, text="Submit", bg="White", font="arial 13 bold",command=uo)
        button1.place(relx=0.2, rely=0.2)

        # Clear
        button2 = Button(adminwork, text="Clear", bg="White", font="arial 13 bold",command=clew)
        button2.place(relx=0.27, rely=0.2)

        # Quit
        button3 = Button(adminwork, text="Quit", bg="White", font="arial 13 bold",command=bankstaff)
        button3.place(relx=0.34, rely=0.2)

        #Text field
        textfield=Text(adminwork, width=40,height=20,font="arial 13")
        textfield.place(relx=0.15,rely=0.3)
    def Createace():
        def generate():

            entry1.configure(state=NORMAL)
            entry8.configure(state=NORMAL)
            entry1.delete(0,"end")
            entry8.delete(0,"end")
            import datetime 
            s = datetime.datetime.now()
            a = s.date()
            entry8.insert(0,"")
            entry8.insert(0,a)

            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            re=cur.execute("Select Accno from Customer")
                    
            fe=re.fetchall()
                    
            a=[]
            for c in fe:
                for b in c:
                    a.append(b)

                   
            d=a[-1]+1
            entry1.insert(0,"")
            entry1.insert(0,d)
            entry1.configure(state=DISABLED)
            entry8.configure(state=DISABLED)

                
        def insert():
            
            from tkinter import messagebox
            if var.get()==1:
                d="Male"
            elif var.get()==2:
                d="Female"
            elif var.get()==3:
                d="Other"
            if hvar.get()==0:
                messagebox.showwarning("Not selected", "Select the option")
            elif hvar.get()==1:
                if (len(entry2.get()) == 0 or len(entry3.get()) == 0 or len(entry4.get())==0 or len(entry5.get())==0 or  len(entry6.get())==0 or len(entry7.get())==0 or len(entry15.get())==0):
                    messagebox.showwarning("Error", "All Entry Properly")
                else:
                    

                    import sqlite3 as s
                    con=s.connect(database="bank.sqlite")
                    cur=con.cursor()
                    cur.execute("INSERT INTO Customer VALUES(?,?,?,?,?,?,?,?,?,?)",[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),d,entry15.get(),a])
                    con.commit() 
                    messagebox.showinfo("Data Inserted", "All data inserted successfully") 
                    entry2.delete(0, "end")
                    entry3.delete(0, "end")
                    entry4.delete(0, "end")
                    entry5.delete(0, "end")
                    entry6.delete(0, "end")
                    entry7.delete(0, "end")
                    entry15.delete(0,"end")
                    entry1.delete(0,"end")
                    entry8.delete(0,"end")
               

            
        def cl():
                entry2.delete(0, "end")
                entry3.delete(0, "end")
                entry4.delete(0, "end")
                entry5.delete(0, "end")
                entry6.delete(0, "end")
                entry7.delete(0, "end")
                entry15.delete(0,"end")
               


        logoa=Frame(admin)
        logoa.configure(bg="#ebe6e6")
        logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoa, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoa, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        label3=Label(logoa,text="Create Account ",bg="#ebe6e6",font="Courier 25 bold")
        label3.place(relx=0.39,rely=0.2)       




        CretAc = Frame(admin)
        CretAc.configure(bg="#00ffa6")
        CretAc.place(x=0,rely=0.15,relwidth=1,relheight=0.85)

        # Account Number
        label1 = Label(CretAc, text="Account Number", bg="#00ffa6", font="arial 13 bold")
        entry1 = Entry(CretAc, width=30)
        label1.place(relx=0.1, rely=0.1)
        entry1.place(relx=0.25, rely=0.1)
        

        # First Name
        label2 = Label(CretAc, text="Name", bg="#00ffa6", font="arial 13 bold")
        entry2 = Entry(CretAc, width=30)
        label2.place(relx=0.1,rely=0.2)
        entry2.place(relx=0.25, rely=0.2)

        # Last Name
        label3 = Label(CretAc, text=" Phone Number", bg="#00ffa6", font="arial 13 bold")
        entry3 = Entry(CretAc, width=30)
        label3.place(relx=0.1, rely=0.3)
        entry3.place(relx=0.25,rely=0.3)

        #Initial Amount
        label4 = Label(CretAc, text="Amount", bg="#00ffa6", font="arial 13 bold")
        entry15 = Entry(CretAc, width=30)
        label4.place(relx=0.1,rely=0.4)
        entry15.place(relx=0.25,rely=0.4)           

        # Initial Amount
        
        label5 = Label(CretAc, text="Email Address", bg="#00ffa6", font="arial 13 bold")
        entry4 = Entry(CretAc, width=30)
        label5.place(relx=0.1,rely=0.5)
        entry4.place(relx=0.25,rely=0.5)
        # Address
        label6 = Label(CretAc, text="Address", bg="#00ffa6", font="arial 13 bold")
        entry5 = Entry(CretAc, width=30)
        label6.place(relx=0.1,rely=0.6)
        entry5.place(relx=0.25,rely=0.6)

        # Phone Number
        label7 = Label(CretAc, text="Date Of Birth", bg="#00ffa6", font="arial 13 bold")
        entry6 = Entry(CretAc, width=30)
        label7.place(relx=0.1,rely=0.7)
        entry6.place(relx=0.25,rely=0.7)

        # Gender
        var=IntVar()
        label8 = Label(CretAc, text="Gender", bg="#00ffa6", font="arial 13 bold")
        radio3 = Radiobutton(CretAc, text="Male", bg="#00ffa6", font="arial 13 bold",variable=var,value=1)
        radio4 = Radiobutton(CretAc, text="Female", bg="#00ffa6", font="arial 13 bold",variable=var,value=2)
        radio5 = Radiobutton(CretAc, text="Other", bg="#00ffa6", font="arial 13 bold",variable=var,value=3)
        label8.place(relx=0.1,rely=0.8)
        radio3.place(relx=0.20,rely=0.8)
        radio4.place(relx=0.30,rely=0.8)
        radio5.place(relx=0.40,rely=0.8)
        # DOB
        label9 = Label(CretAc, text="Password", bg="#00ffa6", font="arial 13 bold")
        entry7 = Entry(CretAc, width=30)
        label9.place(relx=0.1,rely=0.9)
        entry7.place(relx=0.25,rely=0.9)

        # Generate Account Number
        button1 = Button(CretAc, text="Generate Account Number", font="arial 13 bold",command=generate)
        button1.place(relx=0.50,rely=0.1)

        # Email
        label10 = Label(CretAc, text="Created on", bg="#00ffa6", font="arial 13 bold")
        entry8 = Entry(CretAc, width=30)
        label10.place(relx=0.50,rely=0.2)
        entry8.place(relx=0.60,rely=0.2)

        # Clear
        button2 = Button(CretAc, text="Clear", font="arial 13 bold",command=cl)
        button2.place(relx=0.50,rely=0.3)
        # Quit
        button3 = Button(CretAc, text="Quit", font="arial 13 bold",command=bankstaff)
        button3.place(relx=0.60,rely=0.3)
        # Checkbutton
        hvar=IntVar()
        check1 = Checkbutton(CretAc, text="I here by declare all these details are correct.", bg="#00ffa6", font="arial 13 bold",variable=hvar,onvalue=1,offvalue=0)
        check1.place(relx=0.50,rely=0.4)
        #submit
        Sub=Button(CretAc,text="Submit",font="arial 13 bold",command=insert)
        Sub.place(relx=0.5,rely=0.5)
    def checkAce():
        def cleAr():
            FirstName.delete(0,"end")
            Phonenu.delete(0,"end")
            Email.delete(0,"end")
            address.delete(0,"end")
            dob.delete(0,"end")
            PassWord.delete(0,"end")
            sex.delete(0,"end")
            InAm.delete(0,"end")
            cred.delete(0,"end")
            

           
        def details():
            FirstName.delete(0,"end")
            Phonenu.delete(0,"end")
            Email.delete(0,"end")
            address.delete(0,"end")
            dob.delete(0,"end")
            PassWord.delete(0,"end")
            sex.delete(0,"end")
            InAm.delete(0,"end")
            cred.delete(0,"end")

            import sqlite3 as s
            a=int(AcnU.get())
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            de=cur.execute("Select Accno From Customer ")
            acc=de.fetchall()

            add=[]
            for i in acc:
                for sa in i:
                    add.append(sa)
            
            if not(a in add):
                from tkinter import messagebox
                messagebox.showerror("Not Match","Account Number is not valid")
            else:
                de=cur.execute("Select * from Customer WHERE Accno=?",[AcnU.get()])
                ri=de.fetchall()

                FirstName.insert(0,"")
                FirstName.insert(0,ri[0][1])
                Phonenu.insert(0,"")
                Phonenu.insert(0,ri[0][2])
                Email.insert(0,"")
                Email.insert(0,ri[0][3])
                address.insert(0,"")
                address.insert(0,ri[0][4])
                dob.insert(0,"")
                dob.insert(0,ri[0][5])
                PassWord.insert(0,"")
                PassWord.insert(0,ri[0][6])
                sex.insert(0,"")
                sex.insert(0,ri[0][7])
                InAm.insert(0,"")
                InAm.insert(0,ri[0][8])
                cred.insert(0,"")
                cred.insert(0,ri[0][9])
                con.close()  

        
        
        
        logoa=Frame(admin)
        logoa.configure(bg="#ebe6e6")
        logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoa, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoa, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        label3=Label(logoa,text="Check Account Details",bg="#ebe6e6",font="Courier 25 bold")
        label3.place(relx=0.39,rely=0.2)       
        work=Frame(admin)
        work.configure(bg="#00ffa6")
        work.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
                    

        #Account Number
        AcNu = Label(work, text="Account Number",bg="#00ffa6",font="arial 13 bold")
        AcnU = Entry(work, width=50)
        AcNu.place(relx=0.05, rely=0.1)
        AcnU.place(relx=0.15, rely=0.1)
        #Name
        Firstname = Label(work, text="Name",bg="#00ffa6",font="arial 13 bold")
        FirstName = Entry(work, width=50)
        Firstname.place(relx=0.05, rely=0.20)
        FirstName.place(relx=0.15, rely=0.20)
        #Phone Number
        Pnumber = Label(work, text="Phone Number",bg="#00ffa6",font="arial 13 bold")
        Phonenu = Entry(work, width=50)
        Pnumber.place(relx=0.05, rely=0.60)
        Phonenu.place(relx=0.15, rely=0.60)
        #Email
        email = Label(work, text="Email",bg="#00ffa6",font="arial 13 bold")
        Email = Entry(work, width=50)
        email.place(relx=0.05, rely=0.8)
        Email.place(relx=0.15, rely=0.8)
        #Address
        Address = Label(work, text="Address",bg="#00ffa6",font="arial 13 bold")
        address = Entry(work, width=50)
        Address.place(relx=0.05, rely=0.50)
        address.place(relx=0.15, rely=0.50)
        #Date of Birth
        DOB = Label(work, text="Date of Birth",bg="#00ffa6",font="arial 13 bold")
        dob = Entry(work, width=50)
        DOB.place(relx=0.05, rely=0.30)
        dob.place(relx=0.15, rely=0.30)
        #Password
        Password = Label(work, text="Password",bg="#00ffa6",font="arial 13 bold")
        PassWord = Entry(work, width=50)
        Password.place(relx=0.60, rely=0.1)
        PassWord.place(relx=0.7, rely=0.1)
        #Created On
        Cre=Label(work, text="Created-on",bg="#00ffa6",font="arial 13 bold")
        cred = Entry(work, width=50)
        Cre.place(relx=0.60, rely=0.2)
        cred.place(relx=0.7, rely=0.2)
        #Sex
        Sex = Label(work, text="Sex",bg="#00ffa6",font="arial 13 bold")
        sex = Entry(work, width=50)
        Sex.place(relx=0.05, rely=0.70)
        sex.place(relx=0.15, rely=0.70)
        #Intial Amount
        inam = Label(work, text="Intial Amount",bg="#00ffa6",font="arial 13 bold")
        InAm = Entry(work, width=50)
        inam.place(relx=0.05, rely=0.40)
        InAm.place(relx=0.15, rely=0.40)


        #Buttons
        Submit = Button(admin, text="Submit",command=details,font="arial 13 bold")
        Clear = Button(admin, text="Clear",font="arial 13 bold",command=cleAr)
        Quit = Button(admin, text="Quit",font="arial 13 bold",command=bankstaff)
        Submit.place(relx=0.6, rely=0.4)
        Clear.place(relx=0.66,rely=0.4) 
        Quit.place(relx=0.71, rely=0.4)
    def deletw():
        def deleteacno():
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()

            degf=cur.execute("Select * From Customer Where Accno=?",[entry1.get()])
            sdss=degf.fetchall()
            deleacc=[]
            for de in sdss:
                for qw in de:
                    deleacc.append(qw)
            
            
            
            import datetime
            da= datetime.datetime.now()
            a = da.date()
            cur.execute("INSERT INTO DeleteAcc VALUES(?,?,?,?,?,?,?,?,?,?,?)",[deleacc[0],deleacc[1],deleacc[2],deleacc[3],deleacc[4],deleacc[5],deleacc[6],deleacc[7],deleacc[8],deleacc[9],a])
            cur.execute("DELETE FROM Customer WHERE Accno=(?)",[entry1.get()])
            con.commit()
            messagebox.showinfo("Data deleted","Data Deleted Successfully") 
        def Detai():
            t0.delete("1.0","end")

            
            import sqlite3 as s
            con=s.connect(database="bank.sqlite")
            cur=con.cursor()
            up=cur.execute("Select * from Customer WHERE Accno=?",[entry1.get()])
            pu=up.fetchall()
            a=[]             
            for c in pu:                 
                for b in c:                     
                    a.append(b)
            de=cur.execute("Select Accno From Customer ")
            acc=de.fetchall()
            ab=int(entry1.get())
            accno=[]
            for i in acc:
                for b in i:
                    accno.append(b)
            if not(ab in accno):
                from tkinter import messagebox
                messagebox.showerror("Not Match","Account Number is not valid")
            else:
                
                t0.insert(END,"Account Number:\t\t "+ str(a[0])+ "\n""\n")
                t0.insert(END,"Name:\t\t "+ a[1]+ "\n""\n")
                t0.insert(END,"Phone Number:\t\t "+ a[2] + "\n""\n")
                t0.insert(END,"Email:\t\t "+ a[3] + "\n""\n")
                t0.insert(END,"Address:\t\t "+ a[4] + "\n""\n")
                t0.insert(END,"DOB:\t\t "+ a[5] + "\n""\n")
                t0.insert(END,"Password:\t\t "+ a[6] + "\n""\n")
                t0.insert(END,"Sex:\t\t "+ a[7] + "\n""\n")
                t0.insert(END,"Amount:\t\t "+ str(a[8]) + "\n""\n")


         

        
        logoa=Frame(admin)
        logoa.configure(bg="#ebe6e6")
        logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
        label1 = Label( logoa, image = bg)
        label1.place(relx = 0.25, rely = 0.05) 
        label2 = Label( logoa, image = bg)
        label2.place(relx = 0.75, rely = 0.05) 
        label3=Label(logoa,text="Delete Account ",bg="#ebe6e6",font="Courier 25 bold")
        label3.place(relx=0.39,rely=0.2)       
        work = Frame(admin)
        work.configure(bg="#00ffa6")
        work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)

        # Account Number
        label1 = Label(work, text="Account Number", bg="#00ffa6", font="arial 13 bold")
        entry1 = Entry(work, width=65)
        label1.place(relx=0.3, rely=0.25)
        entry1.place(relx=0.5, rely=0.25)

        label2 = Label(work, text="Details ->", bg="#00ffa6", font="arial 13 bold")
        label2.place(relx=0.3, rely=0.35)

        # Submit
        button0 = Button(work, text="Submit", bg="White", font="arial 13 bold", width=10,command=Detai)
        button0.place(relx=0.3, rely=0.45)

        # Delete
        button1 = Button(work, text="Delete", bg="White", font="arial 13 bold", width=10,command=deleteacno)
        button1.place(relx=0.3, rely=0.55)

        # Clear
        button2 = Button(work, text="Clear", bg="White", font="arial 13 bold", width=10)
        button2.place(relx=0.3, rely=0.65)

        # Quit
        button3 = Button(work, text="Quit", bg="White", font="arial 13 bold", width=10,command=bankstaff)
        button3.place(relx=0.3, rely=0.75)


        #All data contain

        t0 = Text(work, font="arial 10 bold", width=40, height=20)
        t0.place(relx=0.5, rely=0.35)
    
    logoa=Frame(admin)
    logoa.configure(bg="#ebe6e6")
    logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
    label1 = Label( logoa, image = bg)
    label1.place(relx = 0.25, rely = 0.05) 
    label2 = Label( logoa, image = bg)
    label2.place(relx = 0.75, rely = 0.05) 
    label3=Label(logoa,text="Employee panel",bg="#ebe6e6",font="Courier 25 bold")
    label3.place(relx=0.39,rely=0.2) 
        
    work = Frame(admin)
    work.configure(bg="#00ffa6")
    work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
    label0=Label(work,image=cg)
    label0.place(relx=0,rely=0)
    label1=Label(work, text="Employee", bg="#00ffa6", font="arial 13 bold")  
    label1.place(relx=0.03,rely=0)
    button0=Button(work,image=ad,command=logout)
    button0.place(relx=0,rely=0.07)
    label2=Label(work,text="LogOut",bg="#00ffa6",font="arial 13 bold",)
    label2.place(relx=0.03,rely=0.07)
       

    def button_hover1(e):
        button1["bg"] = "CYAN"
        label1.place(relx=0.30, rely=0.2)

    def button_hover_leave1(e):
        button1["bg"] = "white"
        label1.place_forget()

    def button_hover2(e):
        button2["bg"] = "CYAN"
        label2.place(relx=0.30, rely=0.3)

    def button_hover_leave2(e):
        button2["bg"] = "white"
        label2.place_forget()


    def button_hover3(e):
        button3["bg"] = "CYAN"
        label3.place(relx=0.30, rely=0.4)

    def button_hover_leave3(e):
        button3["bg"] = "white"
        label3.place_forget()

    def button_hover4(e):
        button4["bg"] = "CYAN"
        label4.place(relx=0.30, rely=0.5)

    def button_hover_leave4(e):
        button4["bg"] = "white"
        label4.place_forget()

    def button_hover5(e):
        button5["bg"] = "CYAN"
        label5.place(relx=0.30, rely=0.6)

    def button_hover_leave5(e):
        button5["bg"] = "white"
        label5.place_forget()

    def button_hover6(e):
        button6["bg"] = "CYAN"
        label6.place(relx=0.30, rely=0.7)

    def button_hover_leave6(e):
        button6["bg"] = "white"
        label6.place_forget()

    def button_hover7(e):
        button7["bg"] = "CYAN"
        label7.place(relx=0.30, rely=0.8)

    def button_hover_leave7(e):
        button7["bg"] = "white"
        label7.place_forget()


    # display Date
    label11 = Label(work, text="Date :", bg="#00ffa6", font="arial 13 bold")
    label0 = Label(work, text=a, bg="#00ffa6", font="arial 13 bold")
    label11.place(relx=0.8, rely=0.1)
    label0.place(relx=0.85, rely=0.1)
    # Create Account
    button1 = Button(work, text="Create Account", width=30, bg="White", font="arial 13 bold",command=Createace)
    button1.place(relx=0.03, rely=0.2)

    label1 = Label(work, text="> Create New Account", width=30, bg="#00ffa6", font="arial 13 bold")
    button1.bind("<Enter>", button_hover1)
    button1.bind("<Leave>", button_hover_leave1)

    # Blance Enquiry
    button2 = Button(work, text="Balance Enquiry", width=30, bg="White", font="arial 13 bold",command=eQ)
    button2.place(relx=0.03, rely=0.3)

    label2 = Label(work, text="> Balance Enquiry", width=30, bg="#00ffa6", font="arial 13 bold")
    button2.bind("<Enter>", button_hover2)
    button2.bind("<Leave>", button_hover_leave2)

    # Check Account Details
    button3 = Button(work, text="Check Account Details", width=30, bg="White", font="arial 13 bold",command=checkAce)
    button3.place(relx=0.03, rely=0.4)
    label3 = Label(work, text="> Check Account Details", width=30, bg="#00ffa6", font="arial 13 bold")
    button3.bind("<Enter>", button_hover3)
    button3.bind("<Leave>", button_hover_leave3)

    # Balance Withdraw
    button4 = Button(work, text="Balance Withdraw", width=30, bg="White", font="arial 13 bold",command=Bw)
    button4.place(relx=0.03, rely=0.5)

    label4 = Label(work, text="> Balance Withdraw", width=30, bg="#00ffa6", font="arial 13 bold")
    button4.bind("<Enter>", button_hover4)
    button4.bind("<Leave>", button_hover_leave4)

    # Balance Deposit
    button5 = Button(work, text="Balance Deposit", width=30, bg="White", font="arial 13 bold",command=BD)
    button5.place(relx=0.03, rely=0.6)

    label5 = Label(work, text="> Balance Deposit", width=30, bg="#00ffa6", font="arial 13 bold")
    button5.bind("<Enter>", button_hover5)
    button5.bind("<Leave>", button_hover_leave5)
    # Delete Account
    button6 = Button(work, text="Delete Account", width=30, bg="White", font="arial 13 bold",command=deletw)
    button6.place(relx=0.03, rely=0.7)

    label6 = Label(work, text="> Delete Account", width=30, bg="#00ffa6", font="arial 13 bold")
    button6.bind("<Enter>", button_hover6)
    button6.bind("<Leave>", button_hover_leave6)
    # Update Account
    button7 = Button(work, text="Update Account", width=30, bg="White", font="arial 13 bold",command=upde)
    button7.place(relx=0.03, rely=0.8)

    label7 = Label(work, text="> Update Account", width=30, bg="#00ffa6", font="arial 13 bold")
    button7.bind("<Enter>", button_hover7)
    button7.bind("<Leave>", button_hover_leave7)

def otp():
    def send():
        def corer():
            def calli():
                import sqlite3 as s
                con=s.connect(database="bank.sqlite")
                cur1=con.cursor()
                bsa=cur1.execute("select * from Customer where Email=(?) ",[entry10.get()])
                ba1=bsa.fetchall()
                customer(ba1)

            import sqlite3 as s
            conn=s.connect(database="bank.sqlite")
            cw=conn.cursor()
            if entry98.get()==entry20.get():
                cw.execute("UPDATE Customer SET passwo=(?) WHERE Email=(?)",[entry98.get(),entry10.get()])
                con.commit()
                con.close()
                messagebox.showinfo("Changed","Password Change Successfully")
                calli()
                
            else:
                messagebox.showwarning("Not match","Password Not Match")
            
            

        def check():
            b12.place_forget()
            checke.place_forget()
            from tkinter import messagebox
            a = entry101.get()
            if a == OTP:
                messagebox.showinfo("Verfied","Otp is successfully match")
                label54.place(relx=0.4,rely=0.45)
                entry98.place(relx=0.4,rely=0.55)
                label158.place(relx=0.4,rely=0.65)
                entry20.place(relx=0.4,rely=0.75)
                ba45=Button(Cus, text="Sumbit", font="arial 13 bold",command=corer)
                ba45.place(relx=0.5,rely=0.85)
            else:
                messagebox.showwarning("Not Verified "," Not Match")
                checke.place(relx=0.5,rely=0.85)
                b12.place(relx=0.65,rely=0.15)
            

        import math
        import random
        import smtplib
        import sqlite3 as s
        con=s.connect(database="bank.sqlite")
        cur=con.cursor()
        ef=cur.execute("SELECT Email FROM Customer")
        we=ef.fetchall()
        opt=[]
        for i in we:
            for bi in i:
                opt.append(bi)
        emailid = entry10.get()
        if not(emailid in opt):
            messagebox.showerror("Not Verified","Enter Registered Email")
        else:
            MY_EMAIL = "macvinebattleground@gmail.com"
            MY_PASSWORD = "flameboyrocke"

            # making the OTP
            digits = "0123456789"
            OTP = ""
            for i in range(6):
                OTP += digits[math.floor(random.random()*10)]
            otp = OTP + " is your OTP"
            msg = otp

            # sending the OTP
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(user=MY_EMAIL,  password=MY_PASSWORD)
            
            emailid = entry10.get()
            s.sendmail(MY_EMAIL, emailid, msg)
            entry101.place(relx=0.4,rely=0.30)
            checke=Button(Cus, text="Check",  font="arial 13 bold",command=check)
            checke.place(relx=0.5,rely=0.85)
            

    # verifying the OTP
    logoa=Frame(admin)
    logoa.configure(bg="#ebe6e6")
    logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
    label1 = Label( logoa, image = bg)
    label1.place(relx = 0.25, rely = 0.05) 
    label2 = Label( logoa, image = bg)
    label2.place(relx = 0.75, rely = 0.05) 
    label3=Label(logoa,text="Forget Password",bg="#ebe6e6",font="Courier 25 bold")
    label3.place(relx=0.39,rely=0.2)        
    Cus=Frame(admin)
    Cus.configure(bg="#00ffa6")
    Cus.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
    label11 = Label(Cus, text="Date:", bg="#00ffa6", font="arial 10 bold")
    label0 = Label(Cus, text=a,  bg="#00ffa6", font="arial 10 bold")
    label11.place(relx=0.9,rely=0.05)
    label0.place(relx=0.93,rely=0.05)
    label15 = Label(Cus, text="Registered Email", bg="#00ffa6", font="arial 13 bold")
    label15.place(relx=0.4,rely=0.1)
    entry10=Entry(Cus,width=50)
    entry10.place(relx=0.4,rely=0.15)
    label150 = Label(Cus, text="Otp", bg="#00ffa6", font="arial 13 bold")
    label150.place(relx=0.4,rely=0.25)
    entry101=Entry(Cus,width=50)
    label54=Label(Cus, text="New Password", bg="#00ffa6", font="arial 13 bold")
    entry98=Entry(Cus,width=50)
    label158=Label(Cus, text="Confirm Password", bg="#00ffa6", font="arial 13 bold")
    entry20=Entry(Cus,width=50)
    #entry101.place(relx=0.4,rely=0.30)
    b12=Button(Cus, text="Send", font="arial 13 bold",command=send)
    b12.place(relx=0.65,rely=0.15)
    b15=Button(Cus, text="Back", font="arial 13 bold",command=main_body)
    b15.place(relx=0.03,rely=0.03)
  
        #Balance Withdraw
def Bw():
    import Balancew as bW
    bW.withdrawn()
#Balance Deposit
def BD():
    import Balanced as bd
    bd.deposit()
#Balance Enquiry
def eQ():
    import Balanceeq as Bq
    Bq.enquiry()

def satement(sd):

    c=[]
    for d in sd:
        for e in d:
            c.append(e)

    def details():
        tex_t.delete("1.0", END)
        tex_t.insert(END,"\tBank Management System\t\n ")
        tex_t.insert(END, "Account Number:\t\t " + str(c[0]) + "\n""\n")
        tex_t.insert(END, "Name:\t\t " + c[1] + "\n""\n")
        tex_t.insert(END, "Phone Number:\t\t " + c[2] + "\n""\n")
        tex_t.insert(END, "Amount:\t\t " + str(c[8]) + "\n""\n")
        bua = Button(root, text="Print", command=lambda: print(tex_t.get('1.0', END)))
        bua.place(relx=0.15, rely=0.85)

    def print(txt):
        from reportlab.lib.enums import TA_JUSTIFY
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        import os
        import time

        def make_doc(name):
            global doc
            doc = SimpleDocTemplate(
                name,
                pagesize=letter,
                rightMargin=72, leftMargin=72,
                topMargin=72, bottomMargin=18)
            return name, doc

        def add_image(img, w=200, h=100, align="LEFT"):
            "Add an image to page"
            im = Image(img, w, h, hAlign=align)
            # im = Image(img, 2*inch, 2*inch)
            page.append(im)

        def add_space():
            "Add a space to page"
            page.append(Spacer(1, 12))

        def add_text(text, space=0):
            "Add a text to page followed by a space"
            if type(text) == list:
                for f in text:
                    add_text(f)
            else:
                ptext = f'<font size="12">{text}</font>'
                page.append(Paragraph(ptext, styles["Normal"]))
                if space == 1:
                    add_space()
                add_space()

        def show(text):
            "Adds images and text for each line in 'text' multiline string"

            global doc
            # using add_image and add_text and recognizing .png and ctime
            text = text.splitlines()
            for line in text:
                if ".png" in line:
                    if len(line.split()) == 4:
                        l, w, h, align = line.split()
                        add_image(l, int(w), int(h), align)
                    else:
                        add_image(line)

                elif "ctime()" in line:
                    add_text(time.ctime())
                else:
                    add_text(line)
            doc.build(page)

        # ==========style

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        page = []

        # ======= Write text and images here =======================

        text = txt

        # ===========================================================

        # put the name of the pdf file here

        name, doc = make_doc("myform.pdf")
        show(text)

        os.startfile(name)

    root = Tk()
    root.title("Ministatement")
    root.geometry("600x600")
    root.resizable(width=False, height=False)
    root.configure(bg="#ebe6e6")
    tex_t = Text(root, bg="light yellow",font="Courier 15 bold")
    tex_t.place(relx=0.15, rely=0.15, width=400, height=400)
    details()


    root.mainloop()

if __name__ == "__main__":
   main_body()
admin.mainloop()