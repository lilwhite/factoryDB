# Factory DB

Conector genérico de bases de datos para Python, que ofrece una API unificada para trabajar con **MySQL**, **PostgreSQL** y **MongoDB** de forma transparente.

## Características

* **Unificación de conexiones**: abstracción de diferentes motores en una sola interfaz.
* **Operaciones CRUD**: funciones comunes para crear, leer, actualizar y eliminar registros.
* **Configuración flexible**: carga de parámetros vía fichero o variables de entorno.
* **Extensible**: diseño modular para añadir nuevos gestores de BD.
* **Logging y manejo de errores**: registro centralizado y excepciones propias.

## Requisitos

* Python 3.8 o superior
* MySQL
* PostgreSQL
* MongoDB

## Instalación

```bash
pip install db_connector
```

O desde el repositorio:

```bash
git clone https://github.com/lilwhite/factortdb.git
cd factorydb
pip install .
```

## Casos de Uso

### UC1 – Configurar y abrir conexión  
Actor: Usuario  
Precondición: El usuario dispone de los datos de acceso (host, puerto, usuario, contraseña, BBDD) y especifica el tipo de motor de base de datos: **MongoDB**, **MySQL** o **PostgreSQL**.  
Flujo principal:  
  1. El usuario crea un diccionario `config` con los parámetros de conexión e incluye la clave `engine` con el valor del motor elegido.  
  2. Llama a `DBConnector(config)`.  
  3. El sistema valida parámetros y abre la conexión al motor indicado.  
Postcondición: Conector listo para recibir consultas.  
Flujos alternativos:  
  • Parámetros inválidos → lanza excepción de validación.  
  • Error de red o credenciales → lanza excepción de conexión.
  
### UC2 – Ejecutar consulta genérica  
Actor: Usuario  
Precondición: La conexión está abierta (UC1).  
Flujo principal:  
  1. El usuario invoca `db.read(table, filters)` o `db.execute(query, params)`.  
  2. El sistema traduce la petición al dialecto adecuado para el motor configurado.  
  3. Se ejecuta la consulta en la BBDD y se devuelven resultados.  
Postcondición: Datos obtenidos en forma de lista de diccionarios (o cursor).  
Flujos alternativos:  
  • Sintaxis inválida → lanza excepción de ejecución.  
  • La tabla/colección no existe → lanza excepción de recurso no encontrado.
  
### UC3 – Operaciones CRUD de conveniencia  
(extendiendo UC2)  
- **Crear**: `db.create(table, data)`  
- **Leer**:  `db.read(table, filters)`  
- **Actualizar**: `db.update(table, filters, data)`  
- **Eliminar**: `db.delete(table, filters)`  

Cada método implementa internamente UC2 adaptando la consulta

Para más ejemplos y configuración avanzada, consulta `docs/usage.md`.

## Estructura del Proyecto

A continuación se propone la estructura inicial de carpetas y archivos para el conector genérico de bases de datos (MySQL, PostgreSQL, MongoDB). Esta organización sigue buenas prácticas de Python y permite escalabilidad, modularidad y facilidad de pruebas.

```bash
db_connector/                  # Raíz del proyecto
├── README.md                  # Descripción general y guía rápida de uso
├── LICENSE                    # Licencia del proyecto (MIT)
├── setup.py                   # Script de instalación
├── requirements.txt           # Dependencias principales
├── pyproject.toml             # Metadatos del proyecto (poetry, flit, etc.)
├── src/                       # Código fuente del paquete
│   └── db_connector/          # Módulo principal
│       ├── __init__.py
│       ├── config.py          # Carga y validación de configuración
│       ├── core.py            # Lógica unificada de operaciones CRUD
│       ├── exceptions.py      # Definición de excepciones propias
│       ├── logger.py          # Configuración de logging
│       ├── utils.py           # Funciones auxiliares comunes
│       └── connection/        # Implementaciones específicas por motor
│           ├── __init__.py
│           ├── base.py        # Clase abstracta `Connector`
│           ├── mysql.py       # Conector para MySQL
│           ├── postgresql.py  # Conector para PostgreSQL
│           └── mongodb.py     # Conector para MongoDB
├── tests/                     # Pruebas unitarias y de integración
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_mysql.py
│   ├── test_postgresql.py
│   └── test_mongodb.py
└── docs/                      # Documentación adicional
    ├── architecture.md        # Diagrama y explicación de arquitectura
    └── usage.md               # Guía de uso y ejemplos de código
```

**Descripción de carpetas clave:**

* **src/db\_connector/connection/**: Contiene la definición de la clase base y las implementaciones concretas para cada sistema de gestión de bases de datos.
* **src/db\_connector/core.py**: Punto central donde se abstraen las operaciones CRUD comunes y se elige el conector adecuado en tiempo de ejecución.
* **tests/**: Estructura de pruebas por conector y para la lógica unificada.
* **docs/**: Material complementario para desarrolladores y usuarios finales.
