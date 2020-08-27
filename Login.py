from tkinter import*
from tkinter import messagebox



class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Management System")
        self.root.geometry("515x360+600+100")

        F1=Frame(self.root,bg="light blue")
        F1.place(x=0,y=0,height=360)

        self.user=StringVar()
        self.password=StringVar()


        title=Label(F1,text="Login System",font=("times new roman",31,"bold"),fg="black",bg="light blue").grid(row=0,columnspan=2,pady=20)

        lblusername=Label(F1,text="Username",font=("times new roman",20,"bold"),fg="black",bg="light blue").grid(row=1,column=0,pady=10,padx=10)

        txtuer=Entry(F1,textvariable=self.user,width=25,font=("arial", 15," bold")).grid(row=1,column=1,padx=10,pady=10)

        lblpass=Label(F1,text="Password",font=("times new roman",20,"bold"),fg="black",bg="light blue").grid(row=2,column=0,pady=10,padx=10)

        txtpass=Entry(F1,show="*",textvariable=self.password,width=25,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        btnlogin=Button(F1,text="Login",font=("times new roman", 15, "bold" ),bd=7,width=10,command=self.log_fun).place(x=10,y=270)
        btnreser=Button(F1,text="Reset",font=("times new roman", 15, "bold" ),bd=7,width=10,command=self.reset).place(x=169,y=270)
        btnexit=Button(F1,text="Exit",font=("times new roman", 15, "bold" ),bd=7,width=10,command=self.exit_fun).place(x=329,y=270)
    def log_fun(self):
        if self.user.get()=="softwarica" and self.password.get()=="coventry":
            self.root.destroy()
            import first
            first.Employee()
        else:
            messagebox.showerror("Error","invalid username or password")
    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit_fun(self):
        option=messagebox.askyesno("Exit","Do you really want to exit?")
        if option:
            self.root.destroy()
        else:
            return



root=Tk()
ob=login(root)
root.mainloop()