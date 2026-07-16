class PrintableMixin:

    def print_data(self):
        print("Printing")


class ScanMixin:

    def scan(self):
        print("Scanning")

p = PrintableMixin()
p.print_data()

s = ScanMixin()
s.scan()