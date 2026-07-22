#ERP system 

class PrintableMixin:  #logging,exporting,saving 
    def print_details(self):
        print(f"Printing {self}")

class Invoice(PrintableMixin):
    def __str__(self):
        return "Invoice"

class Employee(PrintableMixin):
    def __str__(self):
        return "Employee"

class Customer(PrintableMixin):
    def __str__(self):
        return "Customer"

i = Invoice()
i.print_details()

e = Employee()
e.print_details()

c = Customer()
c.print_details()
