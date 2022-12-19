import unittest

from vehicles import Vehicle, VehicleStatus


class VehiclesTestCase(unittest.TestCase):
    def test_vehicle_status(self):
        available_status = VehicleStatus("available")
        in_use_status = VehicleStatus("in use")
        under_repair_status = VehicleStatus("under repair")
        not_available_status = VehicleStatus("not available")
        self.assertEqual(available_status, VehicleStatus.AVAILABLE)
        self.assertEqual(in_use_status, VehicleStatus.IN_USE)
        self.assertEqual(under_repair_status, VehicleStatus.UNDER_REPAIR)
        self.assertEqual(not_available_status, VehicleStatus.NOT_AVAILABLE)

    def test_vehicle_creation(self):
        vehicle = Vehicle("test brand", "test model", VehicleStatus.AVAILABLE)
        self.assertEqual(vehicle.brand, "test brand")
        self.assertEqual(vehicle.model, "test model")
        self.assertEqual(vehicle.status, VehicleStatus.AVAILABLE)

    def test_vehicle_creation_from_string(self):
        vehicle = Vehicle.from_string("brand, model, in use")
        self.assertEqual(vehicle.brand, "brand")
        self.assertEqual(vehicle.model, "model")
        self.assertEqual(vehicle.status, VehicleStatus.IN_USE)

    def test_vehicle_set_status(self):
        vehicle = Vehicle("brand", "model")
        vehicle.status = VehicleStatus.UNDER_REPAIR
        self.assertEqual(vehicle.status, VehicleStatus.UNDER_REPAIR)
        vehicle.status = "not available"
        self.assertEqual(vehicle.status, VehicleStatus.NOT_AVAILABLE)
