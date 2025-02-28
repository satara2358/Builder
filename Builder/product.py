class Vehiculo:
    def __init__(self, tipo, ruedas, motor, color):
        self.tipo = tipo
        self.ruedas = ruedas
        self.motor = motor
        self.color = color

    def mostrar_info(self):
        return f"{self.tipo} con {self.ruedas} ruedas, motor {self.motor} y color {self.color}"