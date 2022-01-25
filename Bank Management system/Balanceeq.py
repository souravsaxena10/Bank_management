from tkinter import *


def enquiry():
    enquiry=Tk()
    enquiry.title("Balance Enquiry")
    enquiry.geometry("700x400")
    enquiry.resizable(width=FALSE,height=FALSE)
    
    logoa=Frame(enquiry)
    logoa.configure(bg="#ebe6e6")
    logoa.place(x=0,y=0,relwidth=1,relheight=0.15)

    baleq=Frame(enquiry)
    baleq.configure(bg="#00ffa6")
    baleq.place(x=0,rely=0.15,relwidth=1,relheight=0.85)

    heading= Label(logoa,text="Balance Enquiry", font="Courier 18 bold", bg="#ebe6e6")
    heading.place(relx=0.40, rely=0.1)
    def veri():
        lb.configure(state=NORMAL)
        lb.delete(0,"end")
        
        import sqlite3 as s
        
        
        a=int(acc_n.get())
        con=s.connect(database="bank.sqlite")
        cur=con.cursor()
        de=cur.execute("Select Accno From Customer ")
        acc=de.fetchall()
        accno=[]
        for i in acc:
            for b in i:
                accno.append(b)
                
        
        if not(a in accno):
            from tkinter import messagebox
            messagebox.showerror("Not Match","Account Number is not valid")

            
        else:
            fe=cur.execute("Select Amount from Customer WHERE Accno=?",[a])
            ef=fe.fetchone()
        
            lb.insert(0,"")
            lb.insert(0,ef)
        
            con.close()
            lb.configure(state=DISABLED)

    
    #Account number button and lable
    acc_no = Label(baleq,text="Account number ", font="arial 13 bold", bg="#00ffa6")
    acc_no.place(relx=0.10, rely=0.10)
    acc_n= Entry(baleq,width= "60", textvariable=acc_no)
    acc_n.place(relx=0.40, rely=0.10)

    #Detail button and label
    detail = Label(baleq,text="Details -> ", font="arial 13 bold", bg="#00ffa6")
    detail.place(relx= 0.10, rely=0.30)
    lb= Entry(baleq,width="60" )
    lb.place(relx=0.40 , rely=0.30)


    #submit
    submit= Button(baleq,text=" Submit ", font="arial 15 bold", width="52",command=veri)
    submit.place(relx=0.05 , rely=0.50)
    enquiry.mainloop()



if __name__ == "__main__":
    enquiry()

