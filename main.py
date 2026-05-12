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

    # ==========================================================
# CLASES DE SERVICIOS
# APORTE: integrante 2
# ==========================================================


# Clase abstracta servicio
class Servicio(ABC):

    # Constructor
    def __init__(self, nombre_servicio):

        # Guardamos nombre
        self.nombre_servicio = nombre_servicio

    # Metodo abstracto
    @abstractmethod
    def calcular_costo(self):
        pass

    # Metodo abstracto
    @abstractmethod
    def descripcion(self):
        pass


# Servicio de reserva de salas
class ReservaSala(Servicio):

    # Constructor
    def __init__(self, horas):

        # Llamamos constructor padre
        super().__init__("Reserva de sala")

        # Validamos horas
        if horas <= 0:

            # Generamos error
            raise ValueError("Las horas deben ser mayores a cero")

        # Guardamos horas
        self.horas = horas

    # Metodo para calcular costo
    def calcular_costo(self):

        # Retornamos costo
        return self.horas * 50

    # Metodo descripcion
    def descripcion(self):

        # Mostramos descripcion
        print("Servicio de reserva de salas")


# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    # Constructor
    def __init__(self, dias):

        # Llamamos constructor padre
        super().__init__("Alquiler de equipos")

        # Validamos dias
        if dias <= 0:

            # Generamos error
            raise ValueError("Los dias deben ser mayores a cero")

        # Guardamos dias
        self.dias = dias

    # Metodo calcular costo
    def calcular_costo(self):

        # Retornamos costo
        return self.dias * 80

    # Metodo descripcion
    def descripcion(self):

        # Mostramos descripcion
        print("Servicio de alquiler de equipos")


# Servicio de asesorias
class Asesoria(Servicio):

    # Constructor
    def __init__(self, horas):

        # Llamamos constructor padre
        super().__init__("Asesoria especializada")

        # Validamos horas
        if horas <= 0:

            # Generamos error
            raise ValueError("Las horas deben ser mayores a cero")

        # Guardamos horas
        self.horas = horas

    # Metodo calcular costo
    def calcular_costo(self):

        # Retornamos costo
        return self.horas * 100

    # Metodo descripcion
    def descripcion(self):

        # Mostramos descripcion
        print("Servicio de asesorias especializadas")


# Bloque de pruebas
try:

    # Creamos servicio
    servicio1 = ReservaSala(2)

    # Mostramos descripcion
    servicio1.descripcion()

    # Mostramos costo
    print("Costo:", servicio1.calcular_costo())

# Capturamos errores
except ValueError as error:

    # Mostramos error
    print("Error:", error)

    # ==========================================================
# CLASE RESERVA
# APORTE: integrante 3
# ==========================================================


# Clase reserva
class Reserva:

    # Constructor
    def __init__(self, cliente, servicio, duracion):

        # Validamos duracion
        if duracion <= 0:

            # Generamos error
            raise ValueError("La duracion debe ser mayor a cero")

        # Guardamos cliente
        self.cliente = cliente

        # Guardamos servicio
        self.servicio = servicio

        # Guardamos duracion
        self.duracion = duracion

        # Estado inicial
        self.estado = "Pendiente"

    # Metodo para confirmar reserva
    def confirmar_reserva(self):

        # Cambiamos estado
        self.estado = "Confirmada"

        # Mensaje
        print("Reserva confirmada")

    # Metodo para cancelar reserva
    def cancelar_reserva(self):

        # Cambiamos estado
        self.estado = "Cancelada"

        # Mensaje
        print("Reserva cancelada")

    # Metodo para mostrar reserva
    def mostrar_reserva(self):

        # Mostramos informacion
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre_servicio)
        print("Duracion:", self.duracion)
        print("Estado:", self.estado)


# Bloque de pruebas
try:

    # Creamos cliente
    cliente2 = Cliente("Ana Torres", "55555", "301999888")

    # Creamos servicio
    servicio2 = Asesoria(3)

    # Creamos reserva
    reserva1 = Reserva(cliente2, servicio2, 3)

    # Confirmamos reserva
    reserva1.confirmar_reserva()

    # Mostramos datos
    reserva1.mostrar_reserva()

# Capturamos errores
except ValueError as error:

    # Mostramos error
    print("Error:", error)