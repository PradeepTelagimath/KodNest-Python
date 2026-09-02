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


class CardPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Card Payment: {self.amount}")


class NetBankingPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Net Banking Payment: {self.amount}")


upi_amount = int(input())
card_amount = int(input())
net_banking_amount = int(input())

# Create the three objects
payments = [
    UPIPayment(upi_amount),
    CardPayment(card_amount),
    NetBankingPayment(net_banking_amount),
]

# Process payments using one loop
for payment in payments:
    payment.process_payment()