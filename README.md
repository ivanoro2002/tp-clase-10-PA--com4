# tp-clase-10-PA--com4
integrantes: Aldana Ibarra, Ivan Valicenti, politi Alexis

1)Críticas a los patrones de diseño:
Los patrones de diseño son respuestas que se pueden reutilizar para resolver problemas comunes en el desarrollo de software. Sin embargo, a pesar de su utilidad, también enfrentan críticas, ya que un mal uso podría causar inconvenientes en los proyectos.

1. Complicación innecesaria
Una de las críticas más comunes es que los patrones de diseño pueden incrementar la complejidad de un sistema si se emplean para solucionarsituaciones simples.
Ejemplo: 
Un programador aplica el patrón Factory Method para crear objetos en una aplicación pequeña donde simplemente sería suficiente usar un constructor directo. Esto resulta en más clases, más líneas de código y una mayor dificultad para entender el proyecto.
Ejemplo en codigo solucion simple
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

usuario = Usuario("Juan")

ejemplo en codigo Usando Factory Method innecesariamente:

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class UsuarioFactory:
    @staticmethod
    def crear_usuario(nombre):
        return Usuario(nombre)

usuario = UsuarioFactory.crear_usuario("Juan")
