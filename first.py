from tkinter import *
from tkinter import ttk, messagebox
from qry import qry
from payment import Payment

class Employee:
    def __init__(self):

        self.root = Tk()
        self.root.title("Employee management system")
        self.root.geometry("2000x2000+0+0")
        #self.pay = payment.Payment()

        title = Label(self.root, text="Employee Management System", bd=10, font=("new times roman", 40, "bold"),
                      bg="light blue", fg="black")
        title.pack(side=TOP, fill=X)

#############################
        self.exe=qry()
#############################

        #search variables:
        self.search_by=StringVar()
        self.search_txt=StringVar()

#########################################################################################################################################################################


        # manage ko frame......
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        Manage_Frame.place(x=30, y=120, width=530, height=730)

        m_title = Label(Manage_Frame, text="Details", font=("new times roman", 20), fg="black", bg="light blue")
        m_title.grid(row=0, columnspan=1, pady=1)

        ##for identity
        lbl_idno = Label(Manage_Frame, text="Idenity No.:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_idno.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txt_idno = Entry(Manage_Frame, bg="light blue", fg="black",
                              font=("new times roman", 15), relief=GROOVE)
        self.txt_idno.grid(row=1, column=0, pady=10, padx=180, sticky="w")
        # for name
        lbl_name = Label(Manage_Frame, text="Name:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(Manage_Frame, bg="light blue", fg="black",
                              font=("new times roman", 15), relief=GROOVE)
        self.txt_name.grid(row=2, column=0, pady=10, padx=180, sticky="w")
        # for email
        lbl_email = Label(Manage_Frame, text="Email id.:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_email = Entry(Manage_Frame, bg="light blue", fg="black",
                               font=("new times roman", 15), relief=GROOVE)
        self.txt_email.grid(row=3, column=0, pady=10, padx=180, sticky="w")
        # for gender
        lbl_gender = Label(Manage_Frame, text="Gender:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.combo_gender = ttk.Combobox(Manage_Frame, font=("new times roman", 15),
                                         state='readonly')  # state readonly only allows u to select the options given not input anything u want!
        self.combo_gender['values'] = ("Male", "Female")
        self.combo_gender.grid(row=4, column=0, padx=180, pady=10)
        # for contact
        lbl_contact = Label(Manage_Frame, text="Contact No.:", bg="light blue", fg="black",
                            font=("new times roman", 15))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(Manage_Frame, bg="light blue", fg="black", font=("new times roman", 15), relief=GROOVE)
        self.txt_contact.grid(row=5, column=0, pady=10, padx=180, sticky="w")
        # for date of birth
        lbl_dob = Label(Manage_Frame, text="D.O.B.:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_dob = Entry(Manage_Frame, bg="light blue", fg="black", font=("new times roman", 15), relief=GROOVE)
        self.txt_dob.grid(row=6, column=0, pady=10, padx=180, sticky="w")
        self.txt_dob.insert(0, 'dd/mm/yyyy')
        # for address
        lbl_address = Label(Manage_Frame, text="Address:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Manage_Frame, bg="light blue", fg="black", font=("new times roman", 15), relief=GROOVE,
                                width=20, height=4)
        self.txt_address.grid(row=7, column=0, pady=10, padx=180, sticky="w")

        # for department
        lbl_department = Label(Manage_Frame, text="Department:", bg="light blue", fg="black",
                               font=("new times roman", 15))
        lbl_department.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.txt_department = ttk.Combobox(Manage_Frame, font=("new times roman", 15),
                                           state='readonly')  # state readonly only allows u to select the options given not input anything u want!
        self.txt_department['values'] = (
        "-", "Administration", "Management", "Information Technology", "Reception", "Sales", "Marketting",)
        self.txt_department.grid(row=8, column=0, padx=180, pady=10)

        # for status
        lbl_status = Label(Manage_Frame, text="Status:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_status.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.combo_status = ttk.Combobox(Manage_Frame, font=("new times roman", 15),
                                         state='readonly')  # state readonly only allows u to select the options given not input anything u want!
        self.combo_status['values'] = ("Present", "Absent", "Busy", "Free")
        self.combo_status.grid(row=9, column=0, padx=180, pady=10)

        # method of payment
        lbl_payment = Label(Manage_Frame, text="Payment:", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_payment.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        self.combo_payment = ttk.Combobox(Manage_Frame, font=("new times roman", 15),
                                          state='readonly')  # state readonly only allows u to select the options given not input anything u want!
        self.combo_payment['values'] = ("Cash", "Bank", "Cheque","E-Sewa","Master Card")
        self.combo_payment.grid(row=10, column=0, padx=180, pady=10)
##############################################################################################################################################################################
##############################################################################################################################################################################
        # button frame,,,.....
        btn_Frame = Frame(Manage_Frame, bd=4, bg="light blue")
        btn_Frame.place(x=10, y=670, width=450, height=40)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_employee).grid(row=0, column=0, padx=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear_employee).grid(row=0, column=2, padx=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=3, padx=10)

#################################################################################################################################################################################
#                                                                                                                                                                               #
#################################################################################################################################################################################

        # detail ko frame......
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        Detail_Frame.place(x=600, y=120, width=1280, height=840)

        # search ko lagi:.....
        lbl_search = Label(Detail_Frame, text="Search By : ", bg="light blue", fg="black", font=("new times roman", 15))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, font=("new times roman", 15), state='readonly')
        combo_search['values'] = ("-", "name", "Idno", "contact", "department", "status")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, bg="light blue",textvariable=self.search_txt, fg="black", font=("new times roman", 15), relief=GROOVE)
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")


###################################################################################################################################################################
        searchbtn = Button(Detail_Frame, text="Search", width=10,command=self.search_data).grid(row=0, column=4, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,command=self.fetch_data).grid(row=0, column=5, padx=10, pady=10)
###################################################################################################################################################################


        # table Frame:......
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="light blue")
        Table_Frame.place(x=10, y=70, width=1245, height=750)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Employee_table = ttk.Treeview(Table_Frame, columns=(
            "Identity Number", "Name", "Email", "Gender", "Contact", "D.O.B", "Address", "Department", "Status",
            "Payment"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)  # yaa scroll garna milne banako
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Employee_table.xview)
        scroll_y.config(command=self.Employee_table.yview)
        # yaa dekhaune banako!
        self.Employee_table.heading("Identity Number", text="Identity Number")
        self.Employee_table.heading("Name", text="Name")
        self.Employee_table.heading("Gender", text="Gender")
        self.Employee_table.heading("Email", text="Email")
        self.Employee_table.heading("Contact", text="Contact")
        self.Employee_table.heading("Department", text="Department")
        self.Employee_table.heading("D.O.B", text="Date of birth")
        self.Employee_table.heading("Address", text="Address")
        self.Employee_table.heading("Status", text="Status")
        self.Employee_table.heading("Payment", text="Payment")

        self.Employee_table['show'] = 'headings'

        # tyo mathi vako jati ko length for heading adjust gareko:
        self.Employee_table.column("Identity Number", width=150)
        self.Employee_table.column("Name", width=250)
        self.Employee_table.column("Email", width=400)
        self.Employee_table.column("Gender", width=150)
        self.Employee_table.column("Contact", width=250)
        self.Employee_table.column("Department", width=150)
        self.Employee_table.column("D.O.B", width=180)
        self.Employee_table.column("Address", width=300)
        self.Employee_table.column("Status", width=150)
        self.Employee_table.column("Payment", width=150)

        self.Employee_table.pack(fill=BOTH,
                                 expand=1)  # to adjust the table in frame for full size keep fill as both  and expand as 1
        self.Employee_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

###############################################################################################################################################################
###############################################################################################################################################################

        # report frame
        report_Frame = Frame(self.root)
        report_Frame.place(x=50, y=850, width=530, height=140)

        Button(report_Frame, text="Payment", font=("new times roman", 15), width=15, bg="light blue",command=self.payment).grid(
            row=50, column=0, padx=10, pady=30)

        Button(report_Frame, text="Logout", font=("new times roman", 15), width=15, bg="light blue",
                           command=self.logout).grid(row=50, column=1, padx=10)


##############################################################################################################################################################
##############################################################################################################################################################



#            FUNTION ASSIGNED             #

    #  logout

    def logout(self):
        ask = messagebox.askyesno("Logout", "Do you want to logout?")
        if ask > 0:
            self.root.destroy()
            import Login
            Login.login(self)


    #Payment file connector
    def payment(self):
        self.root.destroy()
        Payment(self.row[0],self.row[1],self.row[4],self.row[7],self.row[9])




    # defining add employee:
    def add_employee(self):

        self.exe.add_employee(self.txt_idno.get(), self.txt_name.get(), self.combo_status.get(), self.txt_email.get(),
                  self.combo_gender.get(), self.txt_contact.get(), self.txt_dob.get(), self.txt_address.get("1.0", END),
                  self.txt_department.get(), self.combo_payment.get())
        self.fetch_data()
        return True


    #Fetch data
    def fetch_data(self):
        data =self.exe.fetch_employee()
        self.Employee_table.delete(*self.Employee_table.get_children())
        for i in data:
            self.Employee_table.insert("", "end", text="", values=i)


    #Get cursor form 1 table to another
    def get_cursor(self, ev):
        self.clear_employee()
        cursor_row = self.Employee_table.focus()
        contents = self.Employee_table.item(cursor_row)
        self.row = contents['values']
        self.txt_idno.insert(0,self.row[0])
        self.txt_name.insert(0, self.row[1])
        self.txt_email.insert(0,self.row[2])
        self.combo_gender.set(self.row[3])
        self.txt_contact.insert(0,self.row[4])
        self.txt_dob.insert(0,self.row[5])
        self.txt_address.insert(END, self.row[6])
        self.txt_department.set(self.row[7])
        self.combo_status.set(self.row[8])
        self.combo_payment.set(self.row[9])



    #Update Table
    def update_data(self):

        self.exe.update_employee (self.txt_idno.get(), self.txt_name.get(), self.combo_status.get(), self.txt_email.get(),
                  self.combo_gender.get(), self.txt_contact.get(), self.txt_dob.get(), self.txt_address.get("1.0", END),
                  self.txt_department.get(), self.combo_payment.get(),)

        self.fetch_data()
        return True


    #Delete Data
    def delete_data(self):

        self.exe.delete_employee(self.txt_idno.get())
        self.fetch_data()
        self.clear_employee()
        return True



    # defining clear
    def clear_employee(self):
        self.txt_idno.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_dob.delete(0, END)
        self.combo_status.set('')
        self.combo_gender.set('')
        self.combo_payment.set('')
        self.txt_address.delete("1.0", END)
        self.txt_department.delete(0, END)

        self.txt_idno.insert(0, '')
        self.txt_name.insert(0, '')
        self.txt_email.insert(0, '')
        self.txt_contact.insert(0, '')
        self.txt_dob.insert(0, '')
        self.txt_department.insert(0, '')



#################################################################################################
#################################################################################################
#################################################################################################

#searching:
    def search_data(self):
        values=(self.search_by.get(),self.search_txt.get())
        # values=(self.search_txt.get(),)
        data = self.exe.search_employee(values)
        self.Employee_table.delete(*self.Employee_table.get_children())
        for i in data:
            self.Employee_table.insert("", END, text="", value=i)
        self.Employee_table.bind("<ButtonRelease-1>", self.get_cursor)



if __name__ == '__main__':
    ob = Employee()
    mainloop()
