import datetime


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

    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_str: str) -> object:
        first, last, pay = employee_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        return day.weekday() not in (5, 6)


emp_1 = Employee("Corey", "Schafer", 50_000)
emp_2 = Employee("Test", "User", 60_000)

emp_1.set_raise_amount(1.05)
print("First employee raise amount:", emp_1.raise_amount)
print("Second employee raise amount:", emp_2.raise_amount)

emp_str = "John-Doe-70000"
emp_3 = Employee.from_string(emp_str)
print("\nEmployee created from string:", emp_3.email, emp_3.pay)

my_date = datetime.date(2022, 12, 7)
print(
    f"\nCheck if {my_date} is workday using staticmethod:",
    Employee.is_workday(my_date),
)
