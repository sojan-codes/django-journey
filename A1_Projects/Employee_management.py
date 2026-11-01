from abc import ABC, abstractmethod

def salary_logger(fnc):
    def wrapper(self):
        print("Calculating salary...")
        val = fnc(self)
        print("Salary calculation completed!")
        return val
    return wrapper

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.calculate_salary()}")
       
    
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary
        
    @salary_logger
    def calculate_salary(self):
        return self.monthly_salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    @salary_logger
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Freelancer(Employee):
    def __init__(self, name, employee_id, project_payment):
        super().__init__(name, employee_id)
        self.project_payment = project_payment
        
    @salary_logger
    def calculate_salary(self):
        return self.project_payment
    
e1 = FullTimeEmployee("Sojan", "EMP001", 50000)
e1.display_details()

e2 = PartTimeEmployee("Ram", "EMP002", 200, 210)
e2.display_details()
        