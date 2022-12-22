import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def test_employee_create(self):
        employee = Employee("first", "last", "manager", 20000)

        self.assertEqual(employee.first, "first")
        self.assertEqual(employee.last, "last")
        self.assertEqual(employee.position, "manager")
        self.assertEqual(employee.pay, 20000)

        self.assertEqual(employee.email, "first.last@company.com")
        self.assertEqual(employee.manager, None)
        self.assertEqual(Employee.nums_of_emps, 1)

    def test_employee_fullname(self):
        employee = Employee("first", "last", "employee", 16000)
        fullname = employee.fullname()
        self.assertEqual(fullname, "first last")

    def test_employee_set_manager(self):
        manager = Employee("test", "name", "manager", 35000)
        employee = Employee("first", "last", "employee", 16000)
        self.assertEqual(employee.manager, None)

        employee.set_manager(manager)
        self.assertEqual(employee.manager, manager)

    def test_employee_create_from_string(self):
        employee = Employee.from_string("first-last-position-25000")

        self.assertEqual(employee.first, "first")
        self.assertEqual(employee.last, "last")
        self.assertEqual(employee.position, "position")
        self.assertEqual(employee.pay, 25000)
        self.assertEqual(employee.email, "first.last@company.com")
