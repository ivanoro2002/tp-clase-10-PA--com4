"1. Patrón Creacional: Singleton"

# Se utiliza para que haya una única versión de una clase.

class Configuracion:
    _instancia = None

    def _new_(cls):
        if cls._instancia is None:
            cls.instancia = super().new_(cls)
        return cls._instancia

config1 = Configuracion()
config2 = Configuracion()

print(config1 == config2)

Resultado: True

# Explicación: ambas variables apuntan al mismo objeto.

"2. Patrón Estructural: Adapter "

#Sirve para adaptar una clase a otra interfaz.

class ImpresoraVieja:
    def imprimir_texto(self):
        return "Imprimiendo..."

class Adaptador:
    def _init_(self, impresora):
        self.impresora = impresora

    def imprimir(self):
        return self.impresora.imprimir_texto()

impresora = ImpresoraVieja()
adaptador = Adaptador(impresora)

print(adaptador.imprimir())

#Explicación: el adaptador permite usar una impresora vieja con una interfaz nueva.

"3. Patrón de Comportamiento: Observer"

#Sirve para notificar cambios a varios objetos.

class Observador:
    def actualizar(self, mensaje):
        print("Mensaje recibido:", mensaje)

class Notificador:
    def _init_(self):
        self.observadores = []

    def agregar(self, observador):
        self.observadores.append(observador)

    def notificar(self, mensaje):
        for obs in self.observadores:
            obs.actualizar(mensaje)

usuario = Observador()

sistema = Notificador()
sistema.agregar(usuario)

sistema.notificar("Nueva tarea disponible")

#Explicación: cuando el sistema envía un mensaje, todos los observadores lo reciben.
