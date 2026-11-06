import time

def preparar_platillo(nombre_platillo, tiempo_coccion):
    print(f" Chef inicia la preparacion de: {nombre_platillo}.")
    time.sleep(tiempo_coccion)  
    print(f" {nombre_platillo} finalizado y listo para servir.")

def main():
    print("*** ORDEN DE ALMUERZO COMPLETO EN RESTAURANTE ***")
    inicio = time.perf_counter()

    preparar_platillo("Entrada: Sopa de Verduras", 2)
    preparar_platillo("Plato Principal: Lomo Salteado", 3)
    preparar_platillo("Postre: Pie de Limon", 1)

    fin = time.perf_counter()
    print("\n--- Menu completo entregado al cliente ---")
    print(f" Tiempo total de preparación: {fin - inicio:.2f} segundos")

if __name__ == "__main__":
    main()