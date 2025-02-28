from abc import ABC, abstractmethod
from product import Vehiculo

class VehiculoBuilder(ABC):
  def __init__(self):
    self.vehiculo = None

  def new_vehiculo(self):
    self.vehiculo = Vehiculo(None, 0, None, None)
  
  @abstractmethod
  def set_tipo(self, tipo):
    pass
  
  @abstractmethod
  def set_ruedas(self, ruedas):
    pass
  
  @abstractmethod
  def set_motor(self, motor):
    pass
  
  @abstractmethod
  def set_color(self, color):
    pass

  def get_vehiculo(self):
    return self.vehiculo
  
class CarroBuilder(VehiculoBuilder):
  def set_tipo(self):
    self.vehiculo.tipo = "Carro Marca Mazda"
    
  def set_ruedas(self):
    self.vehiculo.ruedas = 4
    
  def set_motor(self):
    self.vehiculo.motor = "Gasolina"
    
  def set_color(self):
    self.vehiculo.color = "Blanco"

class MotoBuilder(VehiculoBuilder):
  def set_tipo(self):
    self.vehiculo.tipo = "Moto"
    
  def set_ruedas(self):
    self.vehiculo.ruedas = 2
    
  def set_motor(self):
    self.vehiculo.motor = "Eléctrico"
    
  def set_color(self):
    self.vehiculo.color = "Negro"
