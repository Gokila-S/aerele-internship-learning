class Invoice:
    def print_details(self):
        print("Printing Invoice")

class Employee:
    def print_details(self):
        print("Printing Employee")

class Customer:
    def print_details(self):
        print("Printing Customer")

invoice = Invoice()
invoice.print_details()

emp = Employee()
emp.print_details()

customer = Customer()
customer.print_details()