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

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):
    def verify_code(self, code):
        print(f"Verifing code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class NotARobot(Authorizer):
    def not_a_robot(self):
        print(f"Are you a robot? Ok, you are not.")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type.")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.authorized:
            raise Exception("Not authorized.")
        print("Processing debit payment type.")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order):
        if not self.authorizer.authorized:
            raise Exception("Not authorized.")
        print("Processing PayPol payment type.")
        print(f"Verifying e-mail address: {self.email_address}")
        order.status = "paid"




order = Order()
order.add_item("manga", 1, 50)
order.add_item("cebola", 10, 20)
order.add_item("ovos", 12, 15)

print(f"Preço total: R$ {order.total_price()}")
authorizer = NotARobot()
processor = DebitPaymentProcessor("dasd1q34", authorizer)
processor.authorizer.not_a_robot()
processor.pay(order)