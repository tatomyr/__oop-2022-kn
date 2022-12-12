from formatter import print_vehicles

from registry_system import RegistrySystem
from vehicles import Vehicle, VehicleStatus


class UserInputInterface:
    def __init__(self, registry: RegistrySystem) -> None:
        self.registry = registry

    def get_input_vehilce_info(self) -> tuple[str, str, str]:
        """Return input vehicle info"""
        statuses = tuple(e.value for e in VehicleStatus)
        brand = input("Enter vehicle brand: ").strip()
        model = input("Enter vehicle model: ").strip()
        status = input(f"Enter vehicle status {statuses}: ").strip()

        return brand, model, status

    def get_input_vehicle_id(self) -> int:
        vehicle_id = input("Enter vehicle ID: ").strip()
        if not vehicle_id.isdigit():
            raise ValueError("ID must be a number")

        return int(vehicle_id)

    def add_vehicle(self) -> None:
        brand, model, status = self.get_input_vehilce_info()
        vehicle_str = f"{brand}, {model}, {status}"
        self.registry.add_vehicle(vehicle_str)

    def edit_vehicle(self) -> None:
        vehicle_id = self.get_input_vehicle_id()
        print("New vehicle info, leave empty to use old values:")
        brand, model, status = self.get_input_vehilce_info()
        self.registry.edit_vehicle(vehicle_id, brand, model, status)

    def delete_vehicle(self) -> None:
        vehicle_id = self.get_input_vehicle_id()
        self.registry.delete_vehicle(vehicle_id)

    def show_vehicles(self) -> None:
        print_vehicles(self.registry.vehicles)

    def mainloop(self) -> None:
        try:
            actions = {
                "add": self.add_vehicle,
                "edit": self.edit_vehicle,
                "delete": self.delete_vehicle,
                "show": self.show_vehicles,
                "exit": exit,
            }
            while True:
                action = input("Choose action (add, edit, delete, show, exit): ")
                if action not in actions:
                    print("Wrong action")
                    continue

                actions[action]()

        except KeyboardInterrupt:
            exit()
