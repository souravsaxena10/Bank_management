from tkinter import *
def userac():
    from tkinter import ttk
    

    import sqlite3

    root = Tk()
    root.title("Active Users")
    root.geometry("600x600")
    root.resizable(width=FALSE,height=FALSE)
    logoa=Frame(root)
    logoa.configure(bg="#ebe6e6")
    logoa.place(x=0,y=0,relwidth=1,relheight=0.15)
    work = Frame(root)
    work.configure(bg="#00ffa6")
    work.place(x=0, rely=0.15, relwidth=1, relheight=0.85)
    heading= Label(logoa,text="Active User", font="Courier 18 bold", bg="#ebe6e6")
    heading.place(relx=0.40, rely=0.1)

    # connect to the database




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


    tree = ttk.Treeview(work, column=("c1", "c2", "c3","c4"), show='headings', xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

    scroll_x.configure(command=tree.xview)
    scroll_y.configure(command=tree.yview)

    tree.column("#1", anchor=CENTER)

    tree.heading("#1", text="Accno")

    tree.column("#2", anchor=CENTER)

    tree.heading("#2", text="Name")

    tree.column("#3", anchor=CENTER)

    tree.heading("#3", text="Phone No")
    tree.column("#4", anchor=CENTER)

    tree.heading("#4", text="Email")




    tree.place(relx=0, rely=0.15, height=420, width=600)


    View()


    root.mainloop()
if __name__ == "__main__":
    userac()
