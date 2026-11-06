import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def get_external_data():
    """Consulta información de un servicio externo mediante HTTPS."""

    try:
        response = requests.get(
            API_URL,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        print("\n====================================")
        print("       NETINVENTORY - API REPORT")
        print("====================================")
        print("Servicio:", API_URL)
        print("Código HTTP:", response.status_code)
        print("Registros recibidos:", len(data))

        print("\nDETALLE DE REGISTROS")
        print("------------------------------------")

        for item in data:
            print(
                "ID: {} | Nombre: {} | Correo: {}".format(
                    item["id"],
                    item["name"],
                    item["email"]
                )
            )

        return data

    except requests.exceptions.Timeout:
        print("Error: La solicitud superó el tiempo de espera.")

    except requests.exceptions.SSLError:
        print("Error: No se pudo verificar la conexión SSL/TLS.")

    except requests.exceptions.HTTPError as error:
        print("Error HTTP:", error)

    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con el servicio externo.")

    except requests.exceptions.RequestException as error:
        print("Error en la solicitud REST:", error)

    except ValueError:
        print("Error: La respuesta no contiene JSON válido.")

    return None


if __name__ == "__main__":
    get_external_data()
