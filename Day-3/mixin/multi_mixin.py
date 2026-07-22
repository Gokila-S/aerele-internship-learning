# A mixin usually
#     has no constructor (__init__)
#     stores no data
#     only provides methods
#     have one responsibility

class PrintableMixin:

    def print_data(self):
        print("Printing...")


class LoggerMixin:

    def log(self):
        print("Logging...")


class Invoice(PrintableMixin, LoggerMixin):
    pass


invoice = Invoice()

invoice.print_data()
invoice.log()

