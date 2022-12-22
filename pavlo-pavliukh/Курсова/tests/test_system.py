import unittest
from unittest.mock import patch

from employee import Employee
from system import ControlSystem


class ControlSystemTestCase(unittest.TestCase):
    def test_control_system_create(self):
        system = ControlSystem()
        self.assertEqual(system.employees, {})

    def test_control_system_create_with_arguments(self):
        system = ControlSystem({1: "test"})
        self.assertEqual(system.employees, {1: "test"})

    @patch("system.ControlSystem.input_employee")
    def test_control_system_add_employee(self, mock):
        employee = Employee("first", "last", "position", 10000)
        mock.return_value = employee

        system = ControlSystem()
        system.add_employee()
        self.assertEqual(len(system.employees), 1)
        self.assertEqual(system.employees, {6: employee})

    @patch("system.ControlSystem.input_employee")
    def test_control_system_find_employee(self, mock):
        emp = Employee("first", "last", "position", 10000)
        mock.return_value = emp

        system = ControlSystem()
        system.add_employee()
        finded_employee = system.find_employee(Employee.nums_of_emps)
        self.assertNotEqual(finded_employee, None)
        self.assertEqual(finded_employee, emp)

    def test_control_system_find_employee_not_exist(self):
        system = ControlSystem()
        employee = system.find_employee(1)
        self.assertNotIsInstance(employee, Employee)
        self.assertEqual(employee, None)
