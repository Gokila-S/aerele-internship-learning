#ERP system 

class PrintableMixin:  #logging,exporting,saving 
    def print_details(self):
        print("Printing Object")

class Invoice(PrintableMixin):
    pass

class Employee(PrintableMixin):
    pass

class Customer(PrintableMixin):
    pass

i = Invoice()
i.print_details()

e = Employee()
e.print_details()

c = Customer()
c.print_details()
