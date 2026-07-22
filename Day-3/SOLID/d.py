class EmailService:
    def send(self, message):
        print(f"Email: {message}")


class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send(message)


email = EmailService()
notification = Notification(email)
notification.notify("Invoice Created")