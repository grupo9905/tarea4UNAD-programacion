# ==========================================================
# PROYECTO SOFTWARE FJ
# Sistema de gestion de clientes y reservas
# ==========================================================

# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# Importamos datetime para manejar fechas
from datetime import datetime


# Clase abstracta general
class Persona(ABC):

    # Constructor de la clase
    def __init__(self, nombre):

        # Guardamos el nombre
        self.nombre = nombre

    # Metodo abstracto
    @abstractmethod
    def mostrar_datos(self):
        pass


# Mensaje inicial
print("===================================")
print("SISTEMA SOFTWARE FJ")
print("===================================")