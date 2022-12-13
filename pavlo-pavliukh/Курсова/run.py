from system import ControlSystem


system = ControlSystem()
try:
    while True:
        controls = {
            "1": system.add_employee,
            "2": system.show_personnel,
            "3": system.edit_employee,
            "4": system.delete_employee,
            "5": exit,
        }
        print("Введіть цифру для виконання дії")
        action = input(
            "1 - додати, 2 - вивести персонал, 3 - редагувати, 4 - видалити, 5 - вийти: "
        )
        controls[action]()

except KeyboardInterrupt:
    exit()
