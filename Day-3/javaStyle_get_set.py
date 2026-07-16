class Employee:

    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):

        if salary < 0:
            raise ValueError("Invalid Salary")

        self._salary = salary


emp = Employee(50000)

print(emp.get_salary())

emp.set_salary(60000)

print(emp.get_salary())