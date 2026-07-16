# Using a RELATIVE IMPORT (.) to talk to a neighbor file in the same folder
from .employee import get_name

print("[SYSTEM] salary.py is being executed!")

def calculate_pay():
    worker_name = get_name()
    base_salary = 50000
    return f"{worker_name} earns ${base_salary} per month."