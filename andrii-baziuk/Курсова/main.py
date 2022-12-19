from pathlib import Path

from interfaces import UserInputInterface
from registry_system import RegistrySystem
from storages import JsonStorage, PlainTextStorage


def main() -> None:
    json_storage = JsonStorage(Path.cwd() / "data.json")
    # txt_storage = PlainTextStorage(Path.cwd() / 'data.txt')
    registry = RegistrySystem(json_storage)
    ui = UserInputInterface(registry)
    ui.mainloop()


if __name__ == "__main__":
    main()
