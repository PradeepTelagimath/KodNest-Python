from abc import ABC, abstractmethod


class NotificationService(ABC):

  @abstractmethod
  def notify(self):
    pass


class EmailNotificationService(NotificationService):

  def __init__(self, message):
    self.message = message

  def notify(self):
    return f"Email: {self.message}"


class SMSNotificationService(NotificationService):

  def __init__(self, message):
    self.message = message

  def notify(self):
    return f"SMS: {self.message}"


def run_notifications(services):
  for service in services:
    print(service.notify())


# Driver Code
message = input()

email_service = EmailNotificationService(message)
sms_service = SMSNotificationService(message)

services = [email_service, sms_service]
run_notifications(services)