class Notification:
    def send(self, message):
        print(f"General Notification: {message}")

class EmailNotification(Notification):
    # Override send()
    def send(self, message):
        print(f"Email Notification: {message}")

message = input().strip()

# Create both objects and call send()

notification = Notification()
notification.send(message)

email_notification = EmailNotification()
email_notification.send(message)