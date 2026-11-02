from abc import ABC, abstractmethod

def salary_logger(fnc):
    def wrapper(self):
        print("Calculating Salary...")
        val = fnc(self)
        print("Salary calculation completed!")
        return val
    return wrapper

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self._employee_id = employee_id
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def _validate_salary(self, salary):
        try:
            if salary > 0:
                return True
            else:
                return False 
        except TypeError:
            return False
    
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Id: {self._employee_id}")
        print(f"Calculated Salary: Rs. {self.calculate_salary()}\n")
        
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.__monthly_salary = monthly_salary
    
    @salary_logger
    def calculate_salary(self):
        if self._validate_salary(self.__monthly_salary):
            return self.__monthly_salary
        else:
            return f"Invalid Salary Amount."
        
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked
    
    @salary_logger
    def calculate_salary(self):
        try: 
            if self.__hourly_rate > 0 and self.__hours_worked > 0:
                __salary =  self.__hourly_rate * self.__hours_worked
                return __salary
            else: 
                return "Invalid Salary Amount"
        except TypeError as e:
            return f"Error : {e}"
        
class Freelancer(Employee):
    def __init__(self, name, employee_id, project_payment):
        super().__init__(name, employee_id)
        self.__project_payment = project_payment
    
    @salary_logger
    def calculate_salary(self):
        if self._validate_salary(self.__project_payment):
            return self.__project_payment
        else:
            return f"Invalid Salary Amount."
    

e1 = FullTimeEmployee("Sojan", "EMP001", 50000)
e2 = PartTimeEmployee("Ram", "EMP002", 400, 100)
e3 = Freelancer("Hari", "EMP003", 25000)

employee_list = [e1, e2, e3]

for employee in employee_list:
    employee.display_details()

def calculate_total_payroll(employee_list):
    total_payroll = 0
    for employee in employee_list:
        val = employee.calculate_salary()
        if isinstance(val, (int, float)):
            total_payroll += val
    return total_payroll

print(f"Total Payroll: Rs. {calculate_total_payroll(employee_list)}")