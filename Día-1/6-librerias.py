from camelcase import CamelCase

instancia = CamelCase()

texto = 'hola como estan buenas noches'
resultado = instancia.hump(texto)
print(resultado)

def sumar(num1: int, num2: int) -> int:#con los int estoy agregando tipado 
  # """"""
  # ''''''
  #Aqui se agrega descripcion de mi funcion
  """Funcion que sirve para sumar dos numeros y retorna el resultado"""
  return num1 + num2

sumar(10,5)
