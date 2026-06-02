# tp-clase-10-PA--com4
integrantes: Aldana Ibarra, Ivan Valicenti, politi Alexis

1) Críticas a los patrones de diseño:
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

En esta situación, el patrón incluye una categoría adicional sin ofrecer un beneficio real.

En esta situación, el patrón incluye una categoría adicional sin ofrecer un beneficio real.

2. Sobrecarga de diseño

A veces los programadores usan patrones porque están familiarizados con ellos, aunque la situación no lo demande.

Ejemplo

Desarrollar una aplicación básica de notas utilizando varios patrones como Singleton, Factory y Observer puede transformar un proyecto simple en algo innecesariamente complicado.

3. Mayor número de clases y archivos

Algunos patrones exigen la creación de interfaces, clases abstractas y clases concretas adicionales.

Ejemplo:
El patrón Strategy a menudo requiere:

Una interfaz Strategy.
Diversas estrategias concretas.
Una clase Context.

Para funciones simples, esto puede resultar en un exceso de archivos y prolongar el tiempo de mantenimiento.

4. Efecto en el rendimiento

Algunos patrones incorporan capas de abstracción que pueden tener un ligero impacto en el rendimiento del sistema.

Ejemplo:
El patrón Decorator permite añadir funcionalidades de forma dinámica a los objetos, pero cada decorador introduce una llamada adicional a métodos, lo que incrementa el uso de memoria y el procesamiento.

Aunque el impacto suele ser menor, en sistemas de tiempo real o con recursos escasos, puede ser significativo.

5. Obstaculizan el aprendizaje de principiantes

Los patrones de diseño pueden presentar conceptos complejos de orientación a objetos que resultan difíciles para programadores con poca experiencia.

Ejemplo:
Un estudiante que empieza a programar puede entender fácilmente una clase básica, pero puede tener problemas para captar cómo las clases interactúan en un patrón como Observer o Abstract Factory.

Esto puede dificultar que el código sea más accesible para los nuevos miembros del equipo.

6. Pueden enmascarar soluciones más sencillas

A veces, la aplicación de patrones puede dificultar la identificación de una solución más inmediata y fácil de llevar a cabo.

Ejemplo:
Emplear el patrón Singleton para compartir una configuración global en lugar de simplemente pasar un objeto de configuración como argumento entre las clases que lo requieran.

Además, el patrón Singleton es comúnmente cuestionado porque complica las pruebas unitarias y crea dependencias globales.

2) el ejercicio 2 esta hecho en el .py.

3) 1-Notificaciones y contextos familiares (Patrón Observer)

Dentro de un hogar, si se presenta una situación relevante, como una actualización en el horario o la convocatoria a una reunión, un individuo tiene la capacidad de informar a todos los demás miembros. Cada persona recibe el aviso y responde adecuadamente.

Patrón relacionado: Observer.

Razón: Un emisor transmite una alerta a múltiples destinatarios simultáneamente.

2-Control de gastos del hogar (Patrón Singleton)

Para administrar los gastos familiares conviene tener un único registro de ingresos y egresos. De esta manera todos consultan la misma información y se evita tener datos diferentes en distintos lugares.

Patrón asociado: Singleton.

Justificación: Existe una única instancia de información compartida por todos.

3-Uso de electrodomésticos con distintos enchufes (Patrón Adapter)

Cuando un electrodoméstico tiene un enchufe incompatible con el tomacorriente disponible, se utiliza un adaptador para conectarlo sin modificar el aparato.

Patrón asociado: Adapter.

Justificación: El adaptador permite que dos elementos incompatibles funcionen juntos.

4) En la literatura y la documentación sobre software, se pueden hallar ciertos patrones de diseño que tienen nombres distintos, traducciones o denominaciones diversas dependiendo del idioma, el autor o el marco utilizado. A continuación, se muestra una tabla con algunos ejemplos.


| Nombre Principal        | Otros nombres o denominaciones                        |
| ----------------------- | ----------------------------------------------------- |
| Singleton               | Instancia Única, Single Instance                      |
| Factory Method          | Método Fábrica, Virtual Constructor                   |
| Abstract Factory        | Fábrica Abstracta, Kit de Herramientas (Toolkit)      |
| Builder                 | Constructor, Generador                                |
| Prototype               | Prototipo, Clonador                                   |
| Adapter                 | Adaptador, Wrapper                                    |
| Bridge                  | Puente, Handle/Body                                   |
| Composite               | Composición, Árbol de Objetos                         |
| Decorator               | Decorador, Wrapper Dinámico                           |
| Facade                  | Fachada, Interfaz Simplificada                        |
| Flyweight               | Peso Ligero, Caché de Objetos                         |
| Proxy                   | Representante, Sustituto                              |
| Chain of Responsibility | Cadena de Responsabilidad, Cadena de Mando            |
| Command                 | Comando, Acción                                       |
| Interpreter             | Intérprete, Analizador                                |
| Iterator                | Iterador, Cursor                                      |
| Mediator                | Mediador, Coordinador                                 |
| Memento                 | Memento, Snapshot (Instantánea)                       |
| Observer                | Observador, Publicador-Suscriptor (Publish-Subscribe) |
| State                   | Estado, Objeto Estado                                 |
| Strategy                | Estrategia, Política (Policy)                         |
| Template Method         | Método Plantilla, Template                            |
| Visitor                 | Visitante, Recorrido Externo                          |


5)  Los antipatrones de diseño son enfoques que aparentan solucionar un problema de programación, pero en realidad crean más dificultades en el tiempo. A menudo resultan en código que es complicado de comprender, mantener y ajustar.

Ejemplos de antipatrones.

Ocurre cuando el código es confuso, con muchas interdependencias y carece de una organización clara. 
Ejemplo: Un programa en el que todas las funciones y variables están combinadas en un solo archivo, lo que hace complicado su entendimiento y mantenimiento. 
Consecuencia: El código se torna complicado de modificar y expandir. 

Clase Dios (God Object) 
Sucede cuando una única clase acumula demasiadas funciones dentro del sistema. 
Ejemplo: Una clase que se encarga de gestionar usuarios, crear informes, supervisar pagos y administrar la base de datos simultáneamente. 
Consecuencia: La clase se vuelve demasiado extensa y complicada, lo que impide su reutilización y mantenimiento.

Reproducción y Transcripción de Código 
Se trata de duplicar el mismo código en varias secciones del programa en vez de usar funciones o métodos ya existentes. 
Caso práctico: Duplicar diversas veces el mismo conjunto de reglas para validar datos en diferentes documentos. 
Resultado: Si se requiere hacer una modificación, hay que cambiarlo en cada lugar donde fue copiado, lo que eleva el riesgo de cometer errores.