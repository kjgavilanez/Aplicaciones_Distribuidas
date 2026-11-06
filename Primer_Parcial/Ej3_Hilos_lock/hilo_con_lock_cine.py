import threading
import time

asientos_disponibles = 1

candado_asiento = threading.Lock()

def intentar_reserva_cine(usuario):
    global asientos_disponibles
    print(f" [{usuario}] entra al sistema para reservar el ultimo asiento VIP.")

    with candado_asiento:
        print(f" [{usuario}] bloqueo la sala. Comprobando disponibilidad. (Asientos actuales: {asientos_disponibles})")
        
        if asientos_disponibles > 0:
            print(f" [{usuario}] procesando cobro con la tarjeta de credito.")
            time.sleep(1)  
            
            asientos_disponibles -= 1
            print(f" [{usuario}] ¡RESERVA EXITOSA! Se le ha asignado el boleto. (Asientos restantes: {asientos_disponibles})")
        else:
            print(f" [{usuario}] RESERVA FALLIDA: Lo sentimos, el asiento ya fue vendido a otro usuario.")

def main():
    print(f"*** SISTEMA DE BOLETERIA CINE: ASIENTOS VIP DISPONIBLES: {asientos_disponibles} ***\n")

    cliente_a = threading.Thread(target=intentar_reserva_cine, args=("Cliente Carlos",))
    cliente_b = threading.Thread(target=intentar_reserva_cine, args=("Cliente Ana",))

    cliente_a.start()
    cliente_b.start()

    cliente_a.join()
    cliente_b.join()

    print(f"\n*** ESTADO FINAL DEL INVENTARIO DE ASIENTOS: {asientos_disponibles} ***")

if __name__ == "__main__":
    main()