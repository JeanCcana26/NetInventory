import xml.etree.ElementTree as ET
from pathlib import Path


def load_xml_inventory():
    """Carga los dispositivos desde un archivo XML."""

    file_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "inventory.xml"
    )

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        organization = root.findtext("organization")
        devices = []

        for device in root.findall("./devices/device"):
            devices.append({
                "hostname": device.findtext("hostname"),
                "type": device.findtext("type"),
                "ip_address": device.findtext("ip_address"),
                "location": device.findtext("location"),
                "status": device.findtext("status")
            })

        return organization, devices

    except FileNotFoundError:
        print("Error: No se encontró el archivo XML.")
    except ET.ParseError:
        print("Error: El archivo XML tiene un formato incorrecto.")
    except OSError as error:
        print("Error al leer el archivo:", error)

    return None, None


def analyze_xml_inventory(organization, devices):
    """Analiza y muestra los dispositivos del inventario."""

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
    print("      NETINVENTORY - XML REPORT")
    print("====================================")

    print("Organización:", organization)
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
    organization, devices = load_xml_inventory()

    if devices is not None:
        analyze_xml_inventory(organization, devices)


if __name__ == "__main__":
    main()
