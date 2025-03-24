from abc import ABC, abstractmethod

class Employee(ABC):  
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass  

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)  
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
# Salary calculation for hourly employee
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked  

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, monthly_salary)
        self.monthly_salary = monthly_salary
# Salary calculation for salaried employee
    def calculate_salary(self):
        return self.monthly_salary  


hourly_emp = HourlyEmployee(101, "Joshua", 100, 200)
salaried_emp = SalariedEmployee(102, "peter", 50000)

print(f"Hourly Employee Salary: {hourly_emp.calculate_salary()}")
print(f"Salaried Employee Salary: {salaried_emp.calculate_salary()}")


    