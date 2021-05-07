# learnTogether Week 16

class Customer:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def display(self):
        return self.firstName + " " + self.lastName + " is a customer who makes some of her purchases online."

class Employee(Customer):
    def __init__(self, firstName, lastName, companyName, job):
        super().__init__(firstName, lastName)
        self.companyName = companyName
        self.job = job
    
    def display(self):
        str1 = self.firstName + " " + self.lastName + " is an employee who works as a(n) " + \
                self.job + " for " + self.companyName + "."
        return str1

class SalaryEmployee(Employee):
    def __init__(self, firstName, lastName, companyName, job, weekly_salary):
        super().__init__(firstName, lastName, companyName, job)
        self.weekly_salary = weekly_salary

    def disply(self):
        str1 = self.firstName + " " + self.lastName + " is an employee who works as a(n) " + \
                self.job + " for " + self.companyName + ". His/Her weekly salary is $" + \
                    str(self.weekly_salary)
        return str1

class HourlyEmployee(Employee):
    def __init__(self, firstName, lastName, companyName, job, hours_worked, hour_rate):
        super().__init__(firstName, lastName, companyName, job)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def display(self):
        str1 = self.firstName + " " + self.lastName + " is an employee who works as a(n) " + \
                self.job + " for " + self.companyName + ". His/Her payroll is $" + \
                    str(self.hours_worked * self.hour_rate)
        return str1

class Orders(Customer):
    def __init__(self, firstName, lastName, orderName, orderQuantity, orderPrice):
        super().__init__(firstName, lastName)
        self.orderName = orderName
        self.orderQuantity = orderQuantity
        self.orderPrice = orderPrice
    
    def display_orders(self):
        str1 = "ordername: " + self.orderName + ", Total_Price = " + str(self.orderQuantity) + \
                " * " + str(self.orderPrice) + " = " + str(self.orderQuantity * self.orderPrice)
        return str1


print("\n=============== O U T P U T ==============")

customer = Customer("Mohsen", "Moazzami")
print(customer.display())

employee = Employee("John", "Smith", "Amazon", "engineer")
print(employee.display())

salary_employee = SalaryEmployee("Chao", "Chang", "Walmart", "Manager", 1500)
print(salary_employee.disply())

hourly_employee = HourlyEmployee("Jane", "Doe", "Costco", "Cashier", 40, 15)
print(hourly_employee.display())

order = Orders(customer.firstName, customer.lastName, "Printer", 1, 105)
print(order.display_orders())
order = Orders(customer.firstName, customer.lastName, "Labtop", 1, 1099)
print(order.display_orders())