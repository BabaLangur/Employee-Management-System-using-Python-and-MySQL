from connector import connection



class qry():
    def __init__(self):
        self.exe = connection()

    def add_employee(self,Idno,name,status,email,gender,contact,dob,address,department,payment):

        qry="INSERT INTO employee(Idno,name,status,email,gender,contact,dob,address,department,payment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values =Idno,name,status,email,gender,contact,dob,address,department,payment

        return self.exe.iud(qry,values)

    def delete_employee(self,values):
        qry = "DELETE  from employee WHERE Idno =%s"
        values=(values,)
        return self.exe.iud(qry, values)


    def update_employee(self,Idno,name,status,email,gender,contact,dob,address,department,payment):
        qry = "UPDATE employee SET Idno =%s, name = %s, status = %s, email = %s, gender = %s, contact = %s, dob = %s, address = %s, department = %s, payment = %s WHERE Idno =%s "
        values=Idno,name,status,email,gender,contact,dob,address,department,payment,Idno
        return self.exe.iud(qry,values)

    def fetch_employee(self):
        qry = "SELECT * from employee"

        return self.exe.show(qry)

    def search_employee(self,values):
        qry = ("SELECT * from employee WHERE {} LIKE '{}%'".format(values[0],values[1]))
        # values=(self.search_by.get(),self.search_txt.get(),)
        # values=(self.search_txt.get(),)
        return self.exe.search(qry)

    def add_payment(self,Idno,name,contact,department,payment,amount,overtime):
        qry="INSERT INTO total_payment(Idno,name,contact,department,payment,amount,overtime,total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(Idno,name, contact,department,payment,amount,overtime,(int(amount)*int(overtime[:-1])/100)+int(amount))
        return self.exe.pay(qry,values)


    def fetch_payment(self):
        qry="SELECT * from total_payment"
        return self.exe.show(qry)





