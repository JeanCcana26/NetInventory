import csv
from pathlib import Path


def load_csv_inventory():
    """Carga los dispositivos desde un archivo CSV."""

    file_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "inventory.csv"
    )

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            devices = list(reader)

        return devices

    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV.")
    except OSError as error:
        print("Error al leer el archivo:", error)

    return None


def analyze_csv_inventory(devices):
    """Analiza la información del inventario CSV."""

    if not devices:
        print("No hay dispositivos registrados.")
        return

    total = len(devices)
    active = sum(1 for d in devices if d["status"] == "active")
    inactive = sum(1 for d in devices if d["status"] == "inactive")
    maintenance = sum(
        1 for d in devices if d["status"] == "maintenance"
    )

    print("\n====================================")
    print("      NETINVENTORY - CSV REPORT")
    print("====================================")
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
    devices = load_csv_inventory()

    if devices is not None:
        analyze_csv_inventory(devices)


if __name__ == "__main__":
    main()
