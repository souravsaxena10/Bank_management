from tkinter import *


def withdrawn():

        
    
    bwithdrawn=Tk()
    bwithdrawn.title("Balance Withdraw")
    bwithdrawn.geometry("700x500")
    bwithdrawn.resizable(width=FALSE,height=FALSE)
    
    logoa=Frame(bwithdrawn)
    logoa.configure(bg="#ebe6e6")
    logoa.place(x=0,y=0,relwidth=1,relheight=0.15)

    balwi=Frame(bwithdrawn)
    balwi.configure(bg="#00ffa6")
    balwi.place(x=0,rely=0.15,relwidth=1,relheight=0.85)
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
            ef=fe.fetchall()
        
            lb.insert(0,"")
            lb.insert(0,ef)
            lb.configure(state=DISABLED)
        con.close()
    def upda():
        samt1.delete(0,"end")
        import sqlite3 as s
        a=acc_n.get()
        b=amt1.get()
        con=s.connect(database="bank.sqlite")
        cur=con.cursor()
        cur.execute("UPDATE Customer SET Amount=Amount-(?) where Accno=(?)",[b,a])
        ffee=cur.execute("Select Amount from Customer WHERE Accno=?",[a])
        re=ffee.fetchall()
        samt1.insert(0,"")
        samt1.insert(0,re)
        con.commit()
        con.close()
        #fe.fetchall()
        


        
    #Heading
    heading= Label(logoa,text="Balance Withdrawn", font="Courier 18 bold", bg="#ebe6e6")
    heading.place(relx=0.40, rely=0.1)

 
    #Account number button and lable
    acc_no = Label(balwi,text="Account number ", font="arial 13 bold", bg="#00ffa6")
    acc_no.place(relx=0.1, rely=0.05)

    acc_n= Entry(balwi,width=60)
    acc_n.place(relx=0.4, rely=0.05)
    

    #Current Balance button and lable
    detail = Label(balwi,text="Current Balance ", font="arial 13 bold", bg="#00ffa6")
    detail.place(relx=0.1, rely=0.15)
    
    lb= Entry( balwi,width=60 )
    lb.place(relx=0.4 , rely= 0.15)
 


    #Amount button and lable
    amt = Label(balwi,text="Amount ", font="arial 13 bold", bg="#00ffa6")
    amt.place(relx=0.1, rely=0.25)
    
    amt1= Entry( balwi,width=60 )
    amt1.place(relx=0.4 , rely= 0.25)

    #Update Balance button and lable
    upb = Label(balwi,text="Updated Balance ", font="arial 13 bold", bg="#00ffa6")
    upb.place(relx=0.1, rely=0.35)
    samt1= Entry( balwi,width=60 )
    samt1.place(relx=0.4 , rely= 0.35)

 
    #submit button
    submit= Button(balwi,text=" Submit ", font="arial 15 bold", width="52",command=veri)
    submit.place(relx=0.05 , rely=0.55)

    #withdrawn button
    wit= Button(balwi,text=" Withdraw ", font="arial 15 bold", width="52",command=upda)
    wit.place(relx=0.05 , rely=0.70)

    bwithdrawn.mainloop()



if __name__ == "__main__":
    withdrawn()

