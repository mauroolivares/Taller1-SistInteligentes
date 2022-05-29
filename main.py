import time
from nreinas import NReinas

#Problema de N Reinas con Busqueda por Anchura (Breadth-first Search)
#Desarrolladores: Mauro Olivares Sierra - Agustin Figueroa Pizarro
#Asignatura: Sistemas Inteligentes - Hector Soza

def main():
    print('Problema BFS')

    #Definir el tamaño del tablero, si se escoge un tamaño menor a 4, el programa no empieza.
    size = int(input('Ingrese tamaño del tablero (mayor a 3): '))
    while(size < 4):
        print("Tamaño muy pequeño, ingrese número valido.")
        size = int(input('Ingrese tamaño del tablero (mayor a 3): '))
    
    #Se inicializa el tablero de N-reinas con el tamaño definido
    start = time.time()
    resultado = NReinas(size).ejecutarBfs()

    #Se imprime el resultado objetivo
    print('Primer resultado encontrado: '+str(resultado[0]))
    end = time.time()
    print(round(end - start,2))




if __name__ == '__main__':
    main()