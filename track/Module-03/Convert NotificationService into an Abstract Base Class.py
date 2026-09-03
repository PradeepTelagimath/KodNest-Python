from abc import ABC, abstractmethod


class NotificationService(ABC):

  @abstractmethod
  def notify(self):
    pass


class EmailNotificationService(NotificationService):

  def __init__(self, message):
    self.message = message

  def send_email(self):
    return f"Email: {self.message}"

  def notify(self):
    return self.send_email()


class SMSNotificationService(NotificationService):

  def __init__(self, message):
    self.message = message

  def send_sms(self):
    return f"SMS: {self.message}"

  def notify(self):
    return self.send_sms()


if __name__ == "__main__":
  message = input().strip()

  email_service = EmailNotificationService(message)
  sms_service = SMSNotificationService(message)

  print(email_service.notify())
  print(sms_service.notify())