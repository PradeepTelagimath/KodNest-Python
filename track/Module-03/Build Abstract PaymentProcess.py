from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class UPIPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"UPI Payment: {self.amount}")


amount = int(input())

# Create the object and process the payment
payment = UPIPayment(amount)
payment.process_payment()