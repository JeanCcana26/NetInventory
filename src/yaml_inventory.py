import yaml
from pathlib import Path


def load_yaml_inventory():
    """Carga los dispositivos desde un archivo YAML."""

    file_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "inventory.yaml"
    )

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return data

    except FileNotFoundError:
        print("Error: No se encontró el archivo YAML.")
    except yaml.YAMLError as error:
        print("Error en el formato YAML:", error)
    except OSError as error:
        print("Error al leer el archivo:", error)

    return None


def analyze_yaml_inventory(data):
    """Analiza la información del inventario YAML."""

    if not data or not isinstance(data.get("devices"), list):
        print("No hay información válida de inventario.")
        return

    devices = data["devices"]

    total = len(devices)
    active = sum(1 for d in devices if d["status"] == "active")
    inactive = sum(1 for d in devices if d["status"] == "inactive")
    maintenance = sum(
        1 for d in devices if d["status"] == "maintenance"
    )

    print("\n====================================")
    print("      NETINVENTORY - YAML REPORT")
    print("====================================")

    print("Organización:", data.get("organization", "No definida"))
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
    inventory = load_yaml_inventory()

    if inventory is not None:
        analyze_yaml_inventory(inventory)


if __name__ == "__main__":
    main()
