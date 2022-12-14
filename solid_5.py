from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, order):
        pass

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def auth_sms(self, code):
        raise Exception("Credit card payments don't suport SMS code authorization.")

    def pay(self, order):
        print("Processing credit payment type.")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized.")
        print("Processing debit payment type.")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized.")
        print("Processing PayPol payment type.")
        print(f"Verifying e-mail address: {self.email_address}")
        order.status = "paid"




order = Order()
order.add_item("manga", 1, 50)
order.add_item("cebola", 10, 20)
order.add_item("ovos", 12, 15)

print(f"Pre??o total: R$ {order.total_price()}")
processor = PayPalPaymentProcessor("test@gmail.com")
processor.auth_sms(123)
processor.pay(order)