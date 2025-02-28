from builder import CarroBuilder, MotoBuilder
from arquitecto import Arquitecto

def main():
  car_builder = CarroBuilder()
  arquitecto = Arquitecto(car_builder)
  vehiculo = arquitecto.crear_vehiculo()
  print(vehiculo.mostrar_info())

  moto_builder = MotoBuilder()
  arquitecto = Arquitecto(moto_builder)
  vehiculo = arquitecto.crear_vehiculo()
  print(vehiculo.mostrar_info())

# if __name__ == "__main__": se ejecuta cuando se ejecuta el archivo principal del programa 
if __name__ == "__main__":
  main()