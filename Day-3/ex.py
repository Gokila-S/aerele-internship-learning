from dataclasses import dataclass

@dataclass
class InvoiceData:
    invoice_no: str
    customer: str
    amount: float
    status: str

class InvoiceController:
    def validate(self, invoice):
        if invoice.amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        print("Invoice is valid.")

invoice = InvoiceData(
    "INV-101",
    "Alice",
    -500,
    "Draft"
)

print(invoice)

controller = InvoiceController()
controller.validate(invoice)