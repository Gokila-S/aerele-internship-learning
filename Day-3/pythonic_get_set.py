# Use a property when you need to:
#     Validate data before assigning it (e.g., salary cannot be negative).
#     Make an attribute read-only.
#     Compute a value dynamically
# If an attribute doesn't need any special behavior, Python developers often expose it directly.

class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


emp = Employee(50000)

print(emp.salary)

emp.salary = -200

print(emp.salary)