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
git clone https://github.com/tu_org/db_connector.git
cd db_connector
pip install .
```

## Uso básico

```python
from db_connector.core import DBConnector

# Configurar conexión (ejemplo MySQL)
config = {
    "engine": "mysql",
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "secret",
    "database": "test_db"
}

# Instanciar conector
db = DBConnector(config)

# Crear un registro
db.create(table="users", data={"name": "Alice", "email": "alice@example.com"})

# Leer registros
users = db.read(table="users", filters={"active": True})

# Actualizar un registro
db.update(table="users", filters={"id": 1}, data={"email": "alice@new.com"})

# Eliminar un registro
db.delete(table="users", filters={"id": 1})
```

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
