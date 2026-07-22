class Student:
    def __init__(self, name):
        self.name = name

class EmailService:
    def send(self):
        print("Mail Sent")


class PDFService:
    def generate(self):
        print("PDF Generated")

email = EmailService()
email.send()