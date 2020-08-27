from tkinter import *
from tkinter import ttk, messagebox
from view import view
from qry import qry



class Payment:
    def __init__(self,Idno,name,contact,department,payment):

        self.root = Tk()
        self.root.title("Employee Management Payment ")
        self.root.geometry("770x880+600+70")

        title = Label(self.root, text="Employee Payment", bd=10, font=("new times roman", 40, "bold"),
                      bg="light blue", fg="black")
        title.pack(side=TOP, fill=X)
        self.exe = qry()





        #frame
        frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        frame.place(x=80, y=120, width=600, height=730)



        ##for identity
        lbl_idno = Label(frame, text="Idenity No.:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_idno.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txt_idno = Entry(frame, bg="light blue", fg="black",
                              font=("new times roman", 15), relief=GROOVE)
        self.txt_idno.grid(row=1, column=0, pady=10, padx=180, sticky="w")


        # for name
        lbl_name = Label(frame, text="Name:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(frame, bg="light blue", fg="black",
                              font=("new times roman", 15), relief=GROOVE)
        self.txt_name.grid(row=2, column=0, pady=10, padx=180, sticky="w")

        # for contact
        lbl_contact = Label(frame, text="Contact No.:", bg="light blue", fg="black",
                            font=("new times roman", 15))
        lbl_contact.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(frame, bg="light blue", fg="black", font=("new times roman", 15), relief=GROOVE)
        self.txt_contact.grid(row=3, column=0, pady=10, padx=180, sticky="w")


        # for department
        lbl_department = Label(frame, text="Department:", bg="light blue", fg="black",
                               font=("new times roman", 15))
        lbl_department.grid(row=4, column=0, pady=10, padx=20, sticky="w")


        self.txt_department= Entry(frame, bg="light blue", fg="black", font=("new times roman", 15), relief=GROOVE)
        self.txt_department.grid(row=4, column=0, pady=10, padx=180, sticky="w")

        # method of payment
        lbl_payment = Label(frame, text="Payment:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_payment.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.combo_payment = Entry(frame, bg="light blue", fg="black", font=("new times roman", 15), relief=GROOVE)
        self.combo_payment.grid(row=5, column=0, pady=10, padx=180, sticky="w")





        #payment
        lbl_amount= Label(frame, text="Amount:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_amount.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        self.amount= Entry(frame, bg="light blue", fg="black", font=("new times roman", 15), relief=GROOVE)
        self.amount.grid(row=6, column=0, pady=10, padx=180, sticky="w")
        self.amount.insert(0, 'NRS.')


        # for overtime
        lbl_bonus = Label(frame, text="Bonus:", bg="light blue", fg="black",
                               font=("new times roman", 15))
        lbl_bonus.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_bonus = ttk.Combobox(frame, font=("new times roman", 15),
                                           state='readonly')
        self.txt_bonus['values'] = (
         "5%", "10%", "15%", "20%", "25%", "30%","50%")
        self.txt_bonus.grid(row=7, column=0, padx=180, pady=10)






#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

        btn_Frame = Frame(frame, bd=0, bg="light blue")
        btn_Frame.place(x=10, y=500, width=500, height=200)
        Button(btn_Frame, text="Pay", font=("new times roman", 15), width=15, bg="light blue",command=self.paybox).grid(row=0, column=0, padx=10, pady=30)

        Button(btn_Frame, text="View All Payments", font=("new times roman", 15), width=15, bg="light blue",command=self.view).grid(row=1, column=0, padx=10, pady=10)
        Button(btn_Frame, text="Back", font=("new times roman", 15), width=15, bg="light blue",command=self.back).grid(row=1, column=1, padx=10, pady=10)




    #insert the data id, name, contaact, department and payment method from first.py
        self.txt_idno.insert(0, Idno)
        self.txt_idno["state"]=DISABLED
        self.txt_name.insert(0, name)
        self.txt_name["state"] = DISABLED
        self.txt_contact.insert(0,contact)
        self.txt_contact["state"] = DISABLED
        self.txt_department.insert(0,department)
        self.txt_department["state"] = DISABLED
        self.combo_payment.insert(0,payment)
        self.combo_payment["state"] = DISABLED

    def paybox(self):
        option=messagebox.askyesno("Payment","Do you really want to Pay the employee?")
        if option:
            self.payment_add()
        else:
            return

    def payment_add(self):
        self.exe.add_payment(self.txt_idno.get(), self.txt_name.get(), self.txt_contact.get(),self.txt_department.get(), self.combo_payment.get(),self.amount.get(),self.txt_bonus.get())
        self.fetch()



    def fetch(self):
        self.exe.fetch_payment()



    def view(self):
        ask = messagebox.askyesno("View", "Do you want to view payments of all Employees?")
        if ask > 0:
            self.root.destroy()
            view()



    def back(self):
        ask = messagebox.askyesno("Go Back", "Do you want to get back without paying?")
        if ask > 0:
            self.root.destroy()
            import first
            first.Employee()


        # data =self.exe.fetch_employee()
        # self.Employee_table.delete(*self.Employee_table.get_children())
        # for i in data:
        #     self.Employee_table.insert("", "end", text="", values=i)
