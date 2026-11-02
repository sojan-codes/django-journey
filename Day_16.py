# Encapsulation

class Student:
    def __init__(self, name, roll_no, marks = []):
        self.name = name
        self.__marks = marks
        self._roll_no = roll_no
    
    def add_mark(self, mark):
        if mark >= 0 and mark <= 100:
            self.__marks.append(mark)
        else:
            print("Invalid mark")
    
    def average(self):
        sum = 0
        for i in self.__marks:
            sum += i
        avg = sum / len(self.__marks)
        return avg
    
s = Student("sojan", 21)
s.add_mark(85)
s.add_mark(92)
s.add_mark(120)

print(s.average())

# print(s.__marks)
            
# Classwork 2
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError
        else:
            self.__price = value
    
    @property
    def __price_with_vat(self):
        return round(self.price * 1.13, 2)
    
p = Product("Laptop", 80000)
p.price = 90000
print(p.price)

# print(p.__price_with_vat)

# p.price = -10
# p.price_with_vat = 5


# Inheritance
class Vechicle:
    def __init__(self, brand, wheels = 4):
        self.brand = brand
        self.wheels = wheels

    def info(self):
        return f"{self.brand} has {self.wheels} wheels"

class Car(Vechicle):
    def __init__(self, brand, wheels = 4):
        super().__init__(brand, wheels)

        
class Bike(Vechicle):
    def __init__(self, brand, wheels, has_carrier):
        super().__init__(brand, wheels)
        self.has_carrier = has_carrier
        
        
    def info(self):
        if self.has_carrier:
            return (f"{self.brand} has {self.wheels} wheels (Carrier: Yes)")
        else:
            return (f"{self.brand} has {self.wheels} wheels (Carrier: No)")
        
class ElectricCar(Car):
    def __init__(self, brand, wheels, battery_kwh):
        super().__init__(brand, wheels = 4)
        self.battery_kwh = battery_kwh
    
    def info(self):
        return f"{self.brand} has {self.wheels} wheels and Battery Kwh : {self.battery_kwh}"
            
c = Car("Toyota")
b = Bike("Yamaha", 2, True)
e = ElectricCar("Tesla", 4, battery_kwh=200)

print(c.info())
print(b.info())
print(e.info())
        

        
        
    
        