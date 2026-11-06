# NetInventory

Sistema de automatización para la consulta, procesamiento y análisis de inventarios de red mediante Python y servicios REST API.

## 1. Objetivo

Desarrollar una herramienta que permita procesar información de dispositivos de red desde diferentes formatos de datos, generar reportes de inventario y consultar servicios externos mediante conexiones HTTPS.

## 2. Tecnologías utilizadas

- Linux (DEVASC VM - Ubuntu).
- Python 3.8.2.
- Git.
- Requests.
- PyYAML.
- REST API.
- HTTPS.
- JSON.
- CSV.
- XML.
- YAML.

## 3. Funcionalidades

- Lectura y procesamiento de inventarios JSON.
- Lectura y procesamiento de archivos CSV.
- Lectura y procesamiento de archivos XML.
- Lectura y procesamiento de archivos YAML.
- Análisis de dispositivos activos, inactivos y en mantenimiento.
- Generación de reportes de inventario desde una aplicación centralizada.
- Consumo de servicios REST API mediante HTTPS.
- Manejo de errores HTTP y excepciones de conexión.
- Diagnóstico de respuestas HTTP: 200, 400, 401, 403, 404 y 500.
- Administración de permisos de archivos y directorios en Linux.

## 4. Estructura del proyecto

```text
netinventory/
├── src/
│   ├── main.py
│   ├── inventory.py
│   ├── csv_inventory.py
│   ├── xml_inventory.py
│   ├── yaml_inventory.py
│   ├── api_inventory.py
│   └── api_diagnostics.py
├── data/
│   ├── inventory.json
│   ├── inventory.csv
│   ├── inventory.xml
│   └── inventory.yaml
├── docs/
├── reports/
├── tests/
├── evidence/
│   └── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## 5. Instalación

Clonar el repositorio:

```bash
git clone https://github.com/JeanCcana26/NetInventory.git
cd NetInventory
```

Crear entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

## 6. Ejecución

Ejecutar el sistema seleccionando el formato de inventario:

```bash
python src/main.py --format json
python src/main.py --format csv
python src/main.py --format xml
python src/main.py --format yaml
```

## 7. Integración REST API

Consultar el servicio externo:

```bash
python src/api_inventory.py
```

El proyecto utiliza JSONPlaceholder como servicio público de demostración para comprobar el consumo de una API REST mediante HTTPS.

Ejecutar el diagnóstico de respuestas HTTP:

```bash
python src/api_diagnostics.py
```

## 8. Administración de permisos Linux

Ejemplos utilizados durante el desarrollo:

```bash
chmod 640 docs/prueba_permisos.txt
chmod 750 docs/directorio_seguro
chmod u+x docs/prueba_ejecucion.py
```

## 9. Dependencias

Las dependencias y sus versiones están especificadas en `requirements.txt`:

- requests==2.32.4
- PyYAML==6.0.2

## 10. Entorno de desarrollo

Proyecto desarrollado y probado en DEVASC VM con Ubuntu, utilizando Python 3.8.2 y Git.

## 11. Evidencias

Las capturas de pantalla de las pruebas y ejecuciones se encuentran en:

`evidence/screenshots/`

## 12. Autoría

Proyecto académico desarrollado individualmente para la unidad didáctica DevOps: Fundamentos.
