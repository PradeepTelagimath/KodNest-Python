class Notification:
    def send(self, message):
        return f"Message: {message}"


class EmailNotification(Notification):
    def send(self, message):
        # Call super().send() to get the base message and append email channel
        return f"{super().send(message)} | Sent by Email"


class SMSNotification(Notification):
    def send(self, message):
        # Call super().send() to get the base message and append SMS channel
        return f"{super().send(message)} | Sent by SMS"


message = input()
email = EmailNotification()
sms = SMSNotification()
print(email.send(message))
print(sms.send(message))