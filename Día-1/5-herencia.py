class Persona:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
  
  def saludar(self):
    # print('Buenos dias!')
    return 'Buenos dias!'
class Beneficio:
  def __init__(self,detalle):
    self.detalle = detalle

  def mostrar_beneficios(self):
    return {
      'detalle': self.detalle
    }

# class Alumno:
class Alumno(Persona):
  def __init__(self,nombre,apellido,grado):
    # self.nombre = nombre
    # self.apellido = apellido
    self.grado = grado
    #llamando al constructor de la clase que estoy heredando
    super().__init__(nombre,apellido)#manda a llamar de la clase que se hereda
  
  # def saludar(self):
  #   print('Buenos dias!')
  
  def saludar(self):
    # Polimorfismo > poli (muchas) morfa (formas) > dependiendo de donde se mande a llamar al metodo este tendra un  comportamiento u otro, en este caso estamos modificando el comportamiento del metodo de la clase padre 'saludar'
    saludo_padre = super().saludar()
    print(saludo_padre + 'Yo soy un alumno')

  def dar_vueltas(self):
    print('Dando vueltas...')

# class Docente:
class Docente(Persona, Beneficio):

  def __init__(self,nombre,apellido,seguro_social,detalle):
    # self.nombre = nombre
    # self.apellido = apellido
    self.seguro_social = seguro_social
    #En el caso de utilizar herencia multiple el uso del comodin super() queda bsoletoya que no se puede indicar a cual de las dos clases estamos haciendo referencia, para ello, se utiliza el nombre de la clase directamente y con ello se indica el metodo a utilizar
    # Se le pase el 'self' para indicar tbn lo que seria la misma instancia para evitar cruce de informacion
    # super(self, Persona).__init__(self,nombre,apellido)
    Persona.__init__(self,nombre,apellido)
    Beneficio.__init__(self,detalle)

  # def saludar(self):
  #   print('Buenos dias!')
  
  def evaluar(self):
    print('Evaluando...')

eduardo = Alumno('eduardo','de rivero','quinto')
paolo = Docente('paolo','soncco','1596485','Pizza 15% dscto')

eduardo.saludar()
# paolo.saludar()
print(paolo.saludar())

print(eduardo.nombre)
