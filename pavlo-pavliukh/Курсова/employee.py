class Employee:
    nums_of_emps = 0

    def __init__(self, first, last, position, pay):
        self.first = first
        self.last = last
        self.position = position
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        self.manager = None

        Employee.nums_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def get_manager(self):
        return self.manager

    def set_manager(self, manager):
        self.manager = manager

    @classmethod
    def from_string(cls, employee_str):
        first, last, position, pay = employee_str.split("-")
        return cls(first, last, position, int(pay))

    def __str__(self):
        string = f"{self.fullname()}, {self.position}, {self.pay}"
        if self.manager:
            string += f", Керівник: {self.manager.fullname()}"
        return string
