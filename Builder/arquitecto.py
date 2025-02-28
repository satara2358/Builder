class Arquitecto:
  def __init__(self, builder):
    self.builder = builder

  def crear_vehiculo(self):
    self.builder.new_vehiculo()
    self.builder.set_tipo()
    self.builder.set_ruedas()
    self.builder.set_motor()
    self.builder.set_color()
    return self.builder.get_vehiculo()
  