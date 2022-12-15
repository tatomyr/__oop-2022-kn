import os
import unittest
from unittest.mock import patch
from pathlib import Path

from registry_system import RegistrySystem
from storages import JsonStorage, Storage
from vehicles import Vehicle, VehicleStatus
from exceptions import VehicleMissingError


class RegistrySystemTestCase(unittest.TestCase):
    def setUp(self):
        self.file = Path("test_data.json")
        self.storage = JsonStorage(self.file)

    def tearDown(self):
        os.remove(self.file)

    def test_registry_system_creation(self):
        system = RegistrySystem(self.storage)
        self.assertIsInstance(system.storage, Storage)
        self.assertEqual(system.vehicles, {})

    def test_registry_system_read_storage(self):
        system = RegistrySystem(self.storage)
        self.storage._write({1: "brand, model, in use", 2: "brand, model, available"})
        system.read_storage()
        self.assertEqual(len(system.vehicles), 2)
        self.assertIn(1, system.vehicles)
        self.assertIn(2, system.vehicles)
        self.assertIsInstance(system.vehicles[1], Vehicle)
        self.assertIsInstance(system.vehicles[2], Vehicle)

    def test_registry_system_add_vehicle(self):
        system = RegistrySystem(self.storage)
        system.add_vehicle("brand, model, available")
        id = Vehicle.vehicles_count
        self.assertEqual(len(system.vehicles), 1)
        self.assertIn(id, system.vehicles)
        self.assertIsInstance(system.vehicles[id], Vehicle)
        self.assertEqual(system.vehicles[id].brand, "brand")
        self.assertEqual(system.vehicles[id].model, "model")
        self.assertEqual(system.vehicles[id].status, VehicleStatus.AVAILABLE)

    def test_registry_system_find_vehicle_existed(self):
        system = RegistrySystem(self.storage)
        system.add_vehicle("test brand, test model, available")
        id = Vehicle.vehicles_count
        vehicle = system.find_vehicle(id)
        self.assertIsInstance(vehicle, Vehicle)

    def test_registry_system_find_vehicle_not_existed(self):
        system = RegistrySystem(self.storage)
        self.assertRaises(VehicleMissingError, system.find_vehicle, 1)

    def test_registry_system_edit_vehicle(self):
        system = RegistrySystem(self.storage)
        system.add_vehicle("test brand, test model, available")
        id = Vehicle.vehicles_count
        system.edit_vehicle(id, "", "", "in use")
        self.assertEqual(len(system.vehicles), 1)
        self.assertIn(id, system.vehicles)
        self.assertIsInstance(system.vehicles[id], Vehicle)
        self.assertEqual(system.vehicles[id].brand, "test brand")
        self.assertEqual(system.vehicles[id].model, "test model")
        self.assertEqual(system.vehicles[id].status, VehicleStatus.IN_USE)

    def test_registry_system_delete_vehicle(self):
        system = RegistrySystem(self.storage)
        system.add_vehicle("test brand, test model, available")
        id = Vehicle.vehicles_count
        system.delete_vehicle(id)
        self.assertEqual(len(system.vehicles), 0)
        self.assertNotIn(id, system.vehicles)

    @patch("registry_system.RegistrySystem.show_vehicles")
    def test_registry_system_show_vehicles(self, mock):
        system = RegistrySystem(self.storage)
        system.show_vehicles()
        self.assertEqual(mock.call_count, 1)
        mock.assert_called_once()
