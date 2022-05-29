from queue import Queue

class NReinas:
    #Inicializado de tablero con su tamaño.
    def __init__(self, size):
        self.size = size

    '''
    Explicación de la función "ejecutarBfs":
        Para trabajar usando BFS es necesario navegar por cada una de las columnas de la fila actual del tablero desde el inicio, no se puede buscar la
        solución y comprobar validez si no se ha navegado por cada nodo de la fila (se registra en la pila "queue").
        - queue = La pila fundamental en que se registra las coordenadas navegadas, para su futuro análisis.
        - solucion = Toma las primeras cordenadas insertadas en la pila "queue", si las reinas colocadas en las coordenadas presentan conflicto, se
            avanza al siguiente valor del la pila "queue", en el caso opuesto, se cuenta si el tablero tiene n-reinas, si faltan se continúa la busqueda.
        - row = Representa la fila actual en base a la cantidad de coordenadas que posee "solucion", fundamental para añadir nuevas coordenadas a la pila.
        - reina = Coordenadas de la reina del ciclo actual.
        - queens = Copia el valor de firstResult para añadirle las coordenadas de "reina", y este conjunto de nodos se añade a la pila "queue".
        - firstResult = Representa el primer resultado donde las n-reinas no chocan.
    '''

    #Ejecución de busqueda por anchura:
    def ejecutarBfs(self):
        firstResult = []
        queue = Queue()
        queue.put([])
        while not queue.empty():
            solucion = queue.get()
            if self.noValido(solucion):
                continue
            row = len(solucion)
            if row == self.size:
                firstResult.append(solucion)
                break
            for col in range(self.size):
                reina = (row, col)
                queens = solucion.copy()
                queens.append(reina)
                queue.put(queens)
        return firstResult

    def noValido(self, queens):
        #Se analiza en base a la cantidad de reinas puestas en el tablero.
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                #Forma optima de comprobar si existen reinas en la columna actual, o en posiciones diagonales.
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        #Si no existe ninguna interferencia, entonces es Valido.
        return False