import json
from pathlib import Path


def load_inventory():
    """Carga los dispositivos desde el archivo JSON."""

    file_path = Path(__file__).resolve().parent.parent / "data" / "inventory.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("Error: No se encontró el archivo de inventario.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato incorrecto.")
    except OSError as error:
        print("Error al leer el archivo:", error)

    return None


def analyze_inventory(data):
    """Analiza y muestra información de los dispositivos."""

    if not data or "devices" not in data:
        print("No hay información de inventario disponible.")
        return

    devices = data["devices"]

    total = len(devices)
    active = sum(1 for device in devices if device["status"] == "active")
    inactive = sum(1 for device in devices if device["status"] == "inactive")
    maintenance = sum(
        1 for device in devices if device["status"] == "maintenance"
    )

    print("\n====================================")
    print("       NETINVENTORY - REPORTE")
    print("====================================")

    print("Organización:", data["organization"])
    print("Total de dispositivos:", total)
    print("Activos:", active)
    print("Inactivos:", inactive)
    print("En mantenimiento:", maintenance)

    print("\nDETALLE DE DISPOSITIVOS")
    print("------------------------------------")

    for device in devices:
        print(
            "{} | {} | {} | {}".format(
                device["hostname"],
                device["ip_address"],
                device["type"],
                device["status"]
            )
        )


def main():
    inventory = load_inventory()

    if inventory:
        analyze_inventory(inventory)


if __name__ == "__main__":
    main()
