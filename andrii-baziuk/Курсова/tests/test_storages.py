import os
import unittest
from pathlib import Path

from storages import JsonStorage, PlainTextStorage, Storage
from vehicles import Vehicle


class JsonStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.jsonfile = Path("test_data.json")

    def tearDown(self):
        os.remove(self.jsonfile)

    def test_storage_creation(self):
        storage = JsonStorage(self.jsonfile)
        self.assertEqual(storage._jsonfile, self.jsonfile)

    def test_storage_read(self):
        storage = JsonStorage(self.jsonfile)
        data = storage.read()
        self.assertEqual(data, {})

    def test_storage_write(self):
        storage = JsonStorage(self.jsonfile)
        storage._write({1: "test", 2: "some text"})
        data = storage.read()
        self.assertDictEqual(data, {1: "test", 2: "some text"})

    def test_storage_save(self):
        storage = JsonStorage(self.jsonfile)
        vehicle = Vehicle.from_string("test, test, in use")
        storage.save(1, vehicle)
        data = storage.read()
        self.assertIn(1, data)
        self.assertDictEqual(data, {1: "test, test, in use"})

    def test_storage_remove(self):
        storage = JsonStorage(self.jsonfile)
        vehicle = Vehicle.from_string("test, test, in use")
        storage.save(1, vehicle)
        storage.remove(1)
        data = storage.read()
        self.assertNotIn(1, data)
        self.assertDictEqual(data, {})


class PlainTextStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.file = Path("test_data.txt")
        with open(self.file, "x") as f:
            f.write("")

    def tearDown(self):
        os.remove(self.file)

    def test_storage_read(self):
        storage = PlainTextStorage(self.file)
        data = storage.read()
        self.assertEqual(data, {})

    def test_storage_save(self):
        storage = PlainTextStorage(self.file)
        vehicle = Vehicle.from_string("test, test, in use")
        storage.save(1, vehicle)
        data = storage.read()
        self.assertDictEqual(data, {1: "test, test, in use"})

    def test_storage_remove(self):
        storage = PlainTextStorage(self.file)
        vehicle = Vehicle.from_string("test, test, in use")
        storage.save(1, vehicle)
        storage.remove(1)
        data = storage.read()
        self.assertNotIn(1, data)
        self.assertEqual(data, {})
