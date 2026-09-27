class EmailNotification:

  def __init__(self, message):
    self.message = message

  def send(self):
    return f"Email: {self.message}"


class SMSNotification:

  def __init__(self, message):
    self.message = message

  def send(self):
    return f"SMS: {self.message}"


class PushNotification:

  def __init__(self, message):
    self.message = message

  def send(self):
    return f"Push: {self.message}"


def send_notifications(notifications):
  for notification in notifications:
    print(notification.send())


message = input()

notifications = [
    EmailNotification(message),
    SMSNotification(message),
    PushNotification(message),
]

send_notifications(notifications)