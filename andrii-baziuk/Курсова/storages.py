import json
from abc import ABC, abstractmethod
from pathlib import Path

from vehicles import Vehicle


class Storage(ABC):
    """Abstract class that represent a basic registry system storage"""

    @abstractmethod
    def save(self, id: int, vehicle: Vehicle) -> None:
        ...

    @abstractmethod
    def remove(self, id: int) -> None:
        ...

    @abstractmethod
    def read(self) -> dict[int, str]:
        ...


class JsonStorage(Storage):
    """Store vehicles in JSON file"""

    def __init__(self, jsonfile: Path) -> None:
        self._jsonfile = jsonfile
        self._init_storage()

    def save(self, id: int, vehicle: Vehicle) -> None:
        history = self.read()
        history[id] = str(vehicle)
        self._write(history)

    def remove(self, id: int) -> None:
        history = self.read()
        history.pop(id)
        self._write(history)

    def read(self) -> dict[int, str]:
        with open(self._jsonfile, "r", encoding="utf-8") as f:
            return json.load(f, object_hook=self.__json_keys_to_int)

    def _write(self, history: dict[int, str]) -> None:
        with open(self._jsonfile, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)

    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text("{}")

    def __json_keys_to_int(self, x):
        if isinstance(x, dict):
            return {int(k): v for k, v in x.items()}
        return x


class PlainTextStorage(Storage):
    """Store vehicles in plain text file"""

    def __init__(self, file: Path) -> None:
        self._file = file

    def save(self, id: int, vehicle: Vehicle) -> None:
        data = self.read()
        data[id] = vehicle
        self._write(data)

    def remove(self, id: int) -> None:
        data = self.read()
        data.pop(id)
        self._write(data)

    def read(self) -> dict[int, str]:
        with open(self._file, "r", encoding="utf-8") as f:
            history = f.read().splitlines()

        data = {}
        for record in history:
            id, vehicle = record.split(": ", 1)
            data[int(id)] = vehicle

        return data

    def _write(self, history: dict[int, str]) -> None:
        with open(self._file, "w", encoding="utf-8") as f:
            for id, vehicle in history.items():
                f.write(self._format(id, vehicle))

    def _format(self, id: int | str, vehicle: Vehicle | str) -> str:
        return f"{id}: {str(vehicle)}\n"
