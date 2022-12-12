from exceptions import VehicleMissingError
from storages import Storage
from vehicles import Vehicle


class RegistrySystem:
    """Class representation a basic vehicle registration system"""

    def __init__(self, storage: Storage) -> None:
        self.storage = storage
        self.vehicles = {}
        self.read_storage()

    def read_storage(self) -> None:
        data = self.storage.read()
        vehicles = {k: Vehicle.from_string(v) for k, v in data.items()}
        self.vehicles = vehicles

    def add_vehicle(self, vehicle_str: str) -> None:
        """Adds Vehicle created from given vehicle_str to the registry"""
        vehicle = Vehicle.from_string(vehicle_str)
        vehicle_id = Vehicle.vehicles_count
        self.vehicles[vehicle_id] = vehicle
        self.storage.save(vehicle_id, vehicle)
        print(f"Vehicle added: ID {vehicle_id}, {vehicle}")

    def find_vehicle(self, id: int) -> Vehicle | None:
        """Finds vehicle by id. If no vehicle can be found,
        VehicleMissingError is raised"""
        if id not in self.vehicles:
            raise VehicleMissingError

        return self.vehicles.get(id)

    def edit_vehicle(self, id: int, brand: str, model: str, status: str) -> None:
        """Edits vehicle with given id to the specified vehicle info."""
        vehicle = self.find_vehicle(id)
        vehicle.brand = brand or vehicle.brand
        vehicle.model = model or vehicle.model
        vehicle.status = status or vehicle.status

        self.vehicles[id] = vehicle
        self.storage.save(id, vehicle)
        print(f"Vehicle with id {id} has been edited")

    def delete_vehicle(self, id: int) -> None:
        """Removes vehicle with given id from registry."""
        removed_vehicle = self.vehicles.pop(id)
        self.storage.remove(id)
        print(f"Vehicle with id {id} removed")
