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

# ==========================================================
# CLASE CLIENTE
# APORTE: integrante 1
# ==========================================================


# Clase cliente que hereda de persona
class Cliente(Persona):

    # Constructor
    def __init__(self, nombre, cedula, telefono):

        # Llamamos el constructor padre
        super().__init__(nombre)

        # Validamos el nombre
        if not nombre.replace(" ", "").isalpha():

            # Generamos error
            raise ValueError("El nombre solo debe tener letras")

        # Validamos cedula
        if not cedula.isdigit():

            # Generamos error
            raise ValueError("La cedula solo debe tener numeros")

        # Validamos telefono
        if not telefono.isdigit():

            # Generamos error
            raise ValueError("El telefono solo debe tener numeros")

        # Guardamos datos
        self.__cedula = cedula
        self.__telefono = telefono

    # Metodo para mostrar datos
    def mostrar_datos(self):

        # Mostramos informacion
        print("Cliente:", self.nombre)
        print("Cedula:", self.__cedula)
        print("Telefono:", self.__telefono)


# Bloque principal de pruebas
try:

    # Creamos cliente correcto
    cliente1 = Cliente("Carlos Perez", "12345", "300123456")

    # Mostramos datos
    cliente1.mostrar_datos()

# Capturamos errores
except ValueError as error:

    # Mostramos error
    print("Error:", error)