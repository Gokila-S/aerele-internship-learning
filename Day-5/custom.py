class InvalidInvoiceException(Exception):
    pass


def submit_invoice(invoice):
    if invoice <= 0:
        raise InvalidInvoiceException("Invoice amount must be greater than zero.")
    print("Invoice submitted")


try:
    submit_invoice(100)
except InvalidInvoiceException as e:
    print(e)
