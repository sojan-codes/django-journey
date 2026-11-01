from abc import ABC, abstractmethod


def payment_logger(fn):
    def wrapper(self, amount):
        print("Initiating payment...")
        val = fn(self, amount)
        print("Payment successful!")
        return val
    return wrapper


class Payment(ABC):
    def __init__(self, customer_name):
        self.customer_name = customer_name

    @abstractmethod
    def process_payment(self, amount):
        pass


class EsewaPayment(Payment):
    def __init__(self, customer_name):
        super().__init__(customer_name)

    @payment_logger
    def process_payment(self, amount):
        return f"Payment of Rs. {amount} completed through eSewa."


class KhaltiPayment(Payment):
    def __init__(self, customer_name):
        super().__init__(customer_name)

    @payment_logger
    def process_payment(self, amount):
        return f"Payment of Rs. {amount} completed through Khalti."


class CardPayment(Payment):
    def __init__(self, customer_name):
        super().__init__(customer_name)

    @payment_logger
    def process_payment(self, amount):
        return f"Payment of Rs. {amount} completed through Card."


p1 = EsewaPayment("Sojan")
result = p1.process_payment(50000)
print(result)

p2 = KhaltiPayment("Hair")
result2 = p2.process_payment(60000)
print(result2)

p3 = CardPayment("Ram")
result3 = p3.process_payment(80000)
print(result3)


