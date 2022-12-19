from dataclasses import dataclass
from enum import Enum


class VehicleStatus(Enum):
    """Possible statuses for the vehicle registry system"""

    AVAILABLE = "available"
    IN_USE = "in use"
    UNDER_REPAIR = "under repair"
    NOT_AVAILABLE = "not available"


class Vehicle:
    """Class representation a vehicle"""

    vehicles_count: int = 0

    def __init__(
        self, brand: str, model: str, status: VehicleStatus = VehicleStatus.AVAILABLE
    ) -> None:
        self.brand = brand
        self.model = model
        self._status = status

        Vehicle.vehicles_count += 1

    @property
    def status(self) -> VehicleStatus:
        return self._status

    @status.setter
    def status(self, value: VehicleStatus | str) -> None:
        if isinstance(value, str):
            value = VehicleStatus(value)

        self._status = value

    @classmethod
    def from_string(cls, vehicle_str: str):
        brand, model, status_value = vehicle_str.split(", ")
        status = VehicleStatus(status_value)
        return cls(brand, model, status)

    def __str__(self) -> str:
        return f"{self.brand}, {self.model}, {self.status.value}"
