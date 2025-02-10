from abc import ABC, abstractmethod
import math
import random
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def color(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def color(self):
        colors = "yellow","blue","orange"
        return random.choice(colors)


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def color(self):
        colors = "yellow","blue","orange"
        return random.choice(colors)



class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self,payment_sum):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self,payment_sum):
        print(f"Payment of {payment_sum} was made using a credit card")

class PayPallProcessor(PaymentProcessor):
    def process_payment(self,payment_sum):
        print(f"Payment of {payment_sum} was made using PayPall")



