class Employee:

    number_of_employees: int = 0
    raise_amount: float = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.number_of_employees += 1

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amount)


print("Number of employees before creating employees:", Employee.number_of_employees)

emp_1 = Employee("Corey", "Schafer", 50_000)
emp_2 = Employee("Test", "User", 60_000)

print("Number of employees after creating:", Employee.number_of_employees)

print("\nFirst employee pay before raising:", emp_1.pay)
emp_1.apply_raise()
print("First employee pay after raising:", emp_1.pay)

emp_1.raise_amount = 1.05

print("\nFirst employee raise amount:", emp_1.raise_amount)
print("Second employee raise amount:", emp_2.raise_amount)
