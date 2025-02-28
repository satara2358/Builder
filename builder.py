# Se define el onjeto Vehiculo
class Vehiculo:
    def __init__(self, tipo, ruedas, motor, color):
        self.tipo = tipo
        self.ruedas = ruedas
        self.motor = motor
        self.color = color

    def mostrar_info(self):
        return f"{self.tipo} con {self.ruedas} ruedas, motor {self.motor} y color {self.color}"

# Se define el objeto VehiculoBuilder que se encarga de construir un vehiculo con los datos que se le pasan al constructor del objeto Vehiculo y retorna el objeto Vehiculo construido con los datos que se le pasaron.
class VehiculoBuilder:
    def __init__(self):
        self.tipo = None
        self.ruedas = 0
        self.motor = None
        self.color = None

    def set_tipo(self, tipo):
        self.tipo = tipo
        return self

    def set_ruedas(self, ruedas):
        self.ruedas = ruedas
        return self

    def set_motor(self, motor):
        self.motor = motor
        return self

    def set_color(self, color):
        self.color = color
        return self

    def build(self):
        return Vehiculo(self.tipo, self.ruedas, self.motor, self.color)

# Uso del patrón Builder para construir objetos Vehiculo
builder = VehiculoBuilder()
carro = builder.set_tipo("Carro").set_ruedas(4).set_motor("Gasolina").set_color("Rojo").build()
moto = builder.set_tipo("Moto").set_ruedas(2).set_motor("Eléctrico").set_color("Negro").build()

# Se imprimen los datos del objeto Vehiculo construido con los datos que se le pasaron al constructor del objeto Vehiculo
print(carro.mostrar_info())  # Carro con 4 ruedas, motor Gasolina y color Rojo
print(moto.mostrar_info())   # Moto con 2 ruedas, motor Eléctrico y color Negro

