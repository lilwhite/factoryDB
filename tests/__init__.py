# Inicialización de tests

# Este archivo es necesario para que Python trate el directorio como un paquete.
# Aquí se pueden incluir configuraciones o imports comunes para todos los tests.

import sys
import os

# Añadir la ruta del proyecto para importar el conector
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar el conector para verificar que está disponible en los tests
from factorydb.core import DBConnector

# También se pueden importar aquí las configuraciones específicas de testing,
# como bases de datos en memoria, mocks, etc.

# Ejemplo: configuración de una base de datos SQLite en memoria para pruebas
TEST_DATABASE_URL = "sqlite:///:memory:"

def pytest_configure():
    """Configuración inicial para pytest."""
    # Aquí se puede inicializar la base de datos de pruebas, crear esquemas, etc.
    pass

def pytest_unconfigure():
    """Limpieza final para pytest."""
    # Cerrar conexiones, eliminar datos de prueba, etc.
    pass