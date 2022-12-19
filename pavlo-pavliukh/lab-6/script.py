class Employee:

    nums_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.nums_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print("Число працівників: ", Employee.nums_of_emps)

emp_1.apply_raise()
print("Зарплата працівника, після підвищення: ", emp_1.pay)

emp_1.raise_amt = 1.05
print("Процент підвищення першого: ", emp_1.raise_amt)
print("Процент підвищення другого: ", emp_2.raise_amt)
