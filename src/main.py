import argparse

from inventory import load_inventory
from csv_inventory import load_csv_inventory
from xml_inventory import load_xml_inventory
from yaml_inventory import load_yaml_inventory


def load_data(file_format):
    """Carga el inventario según el formato seleccionado."""

    if file_format == "json":
        data = load_inventory()

        if data is None:
            return None, None

        return data.get("organization"), data.get("devices")

    elif file_format == "csv":
        devices = load_csv_inventory()
        return "NetInventory", devices

    elif file_format == "xml":
        return load_xml_inventory()

    elif file_format == "yaml":
        data = load_yaml_inventory()

        if data is None:
            return None, None

        return data.get("organization"), data.get("devices")


def generate_report(organization, devices, file_format):
    """Genera un reporte general del inventario."""

    if not isinstance(devices, list) or not devices:
        print("No hay dispositivos disponibles.")
        return

    active = sum(1 for d in devices if d["status"] == "active")
    inactive = sum(1 for d in devices if d["status"] == "inactive")
    maintenance = sum(
        1 for d in devices if d["status"] == "maintenance"
    )

    print("\n====================================")
    print("       NETINVENTORY - REPORT")
    print("====================================")

    print("Organización:", organization)
    print("Formato utilizado:", file_format.upper())
    print("Total de dispositivos:", len(devices))
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
    parser = argparse.ArgumentParser(
        description="Sistema de gestión de inventario NetInventory"
    )

    parser.add_argument(
        "--format",
        required=True,
        choices=["json", "csv", "xml", "yaml"],
        help="Formato del inventario que se desea procesar"
    )

    args = parser.parse_args()

    organization, devices = load_data(args.format)

    if devices is not None:
        generate_report(organization, devices, args.format)
    else:
        print("No fue posible cargar el inventario.")


if __name__ == "__main__":
    main()
