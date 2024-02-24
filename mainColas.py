
# Online Python - IDE, Editor, Compiler, Interpreter


import heapq

class ColaPrioridad:
    def __init__(self):
        self.cola = []
        self.contador = 0  # Utilizado para manejar el orden de llegada de los elementos con la misma prioridad
    
    def agregar_elemento(self, elemento, prioridad):
        heapq.heappush(self.cola, (prioridad, self.contador, elemento))
        self.contador += 1
    
    def eliminar_elemento(self):
        if self.cola:
            return heapq.heappop(self.cola)[2]
        else:
            return None
    
    def esta_vacia(self):
        return len(self.cola) == 0

# Ejemplo de uso
cola_prioridad = ColaPrioridad()

cola_prioridad.agregar_elemento('Tarea 1', 3)
cola_prioridad.agregar_elemento('Tarea 2', 1)
cola_prioridad.agregar_elemento('Tarea 3', 2)

while not cola_prioridad.esta_vacia():
    print(cola_prioridad.eliminar_elemento())
