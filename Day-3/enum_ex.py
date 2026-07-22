from enum import Enum

class Status(Enum):
    PENDING = 1
    PAID = 2
    CANCELLED = 3

print(f"Value of PAID: {Status.PAID.value}") 
print(f"Name of PAID: {Status.PAID.name}")    

status_by_value = Status(2)             
status_by_name = Status["CANCELLED"]     

print(f"Found by value 2: {status_by_value}")     
print(f"Found by name string: {status_by_name}")

current_status = Status.PENDING

if current_status == Status.PENDING:
    print("Payment is still pending.")

print("All available statuses:")
for status in Status:
    print(f"- {status.name} (Code: {status.value})")
