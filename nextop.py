class Car:
    def __init__(self,id,brand):
        self.id = id
        self.type = "A"
        self.brand = brand
        self.is_manual = False

    def better(self,other):
        if self.type > other.type:
            return True
        if self.type == other.type and not self.is_manual and other.is_manual:
            return True
        return False

class Rent:
    def __init__(self,name,):
       self.name = name

