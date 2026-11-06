import requests


TESTS = [
    {
        "name": "Solicitud exitosa",
        "url": "https://jsonplaceholder.typicode.com/users",
        "expected": 200
    },
    {
        "name": "Solicitud incorrecta",
        "url": "https://httpbin.org/status/400",
        "expected": 400
    },
    {
        "name": "Sin autenticación",
        "url": "https://httpbin.org/status/401",
        "expected": 401
    },
    {
        "name": "Acceso prohibido",
        "url": "https://httpbin.org/status/403",
        "expected": 403
    },
    {
        "name": "Recurso inexistente",
        "url": "https://httpbin.org/status/404",
        "expected": 404
    },
    {
        "name": "Error interno del servidor",
        "url": "https://httpbin.org/status/500",
        "expected": 500
    }
]


SOLUTIONS = {
    200: "La solicitud se proceso correctamente.",
    400: "Revisar parametros, URL y formato de la solicitud.",
    401: "Verificar credenciales y token de autenticacion.",
    403: "Comprobar permisos y autorizaciones.",
    404: "Verificar la URL y la existencia del recurso.",
    500: "Revisar el servidor y sus registros internos."
}


def diagnose_api():
    """Ejecuta pruebas controladas de respuestas HTTP."""

    print("\n====================================")
    print("    NETINVENTORY - API DIAGNOSTICS")
    print("====================================")

    for test in TESTS:
        print("\nPrueba:", test["name"])

        try:
            response = requests.get(
                test["url"],
                timeout=10
            )

            status = response.status_code

            print("Codigo HTTP:", status)
            print("Diagnostico:", SOLUTIONS.get(
                status,
                "Consultar documentacion HTTP."
            ))

            if status == test["expected"]:
                print("Resultado: PRUEBA CORRECTA")
            else:
                print("Resultado: RESPUESTA INESPERADA")

        except requests.exceptions.Timeout:
            print("Error: Tiempo de espera agotado.")

        except requests.exceptions.SSLError:
            print("Error: Problema de certificado SSL/TLS.")

        except requests.exceptions.ConnectionError:
            print("Error: Problema de conexion.")

        except requests.exceptions.RequestException as error:
            print("Error REST:", error)


if __name__ == "__main__":
    diagnose_api()
