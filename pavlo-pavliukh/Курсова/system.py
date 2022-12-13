from employee import Employee


class ControlSystem:
    def __init__(self, employees=None):
        self.employees = employees or {}

    def input_employee(self):
        last = input("Прізвище: ")
        first = input("Ім'я: ")
        position = input("Посада: ")
        pay = input("Зарплата: ")
        employee = Employee(first, last, position, int(pay))
        self.input_manager(employee)

        return employee

    def input_manager(self, employee):
        manager_id = input("Id керівника? (залишіть пустим, якщо немає): ")
        if manager_id:
            manager = self.find_employee(int(manager_id))
            employee.set_manager(manager)

    def add_employee(self):
        employee = self.input_employee()
        self.employees[employee.nums_of_emps] = employee

    def find_employee(self, id):
        return self.employees.get(id)

    def show_personnel(self):
        for id, emp in self.employees.items():
            print(f"Id: {id}, {emp}")

    def edit_employee(self):
        employee_id = int(input("Id працівника, якого треба редагувати: "))
        if employee_id in self.employees:
            employee = self.find_employee(employee_id)
            print("Працівник:", employee)
            employee.last = input("Прізвище: ") or employee.last
            employee.first = input("Ім'я: ") or employee.first
            employee.position = input("Посада: ") or employee.position
            employee.pay = input("Зарплата: ") or employee.pay
            self.input_manager(employee)
            self.employees[employee_id] = employee
            print(f"Працівника з id {employee_id} редаговано")

    def delete_employee(self):
        employee_id = int(input("Id працівника, якого треба видалити: "))
        if employee_id in self.employees:
            del self.employees[employee_id]
            print(f"Працівника з id {employee_id} видалено")
