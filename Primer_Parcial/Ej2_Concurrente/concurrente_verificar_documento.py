import asyncio
import time

async def verificar_documento(tipo_doc, tiempo_espera):
    print(f" Solicitando validacion remota de: {tipo_doc}.")
    await asyncio.sleep(tiempo_espera)
    print(f" Validacion aprobada para: {tipo_doc} (Respuesta recibida en {tiempo_espera}s)")

async def main():
    print("*** SISTEMA DE MATRICULA UNIVERSITARIA (VERIFICACION ASINCRONA) ***")
    inicio = time.perf_counter()

    await asyncio.gather(
        verificar_documento("Titulo de Bachiller (Servidor Central)", 3),
        verificar_documento("Pago de Inscripcion (Pasarela Bancaria)", 1),
        verificar_documento("Historial Medico (Servicio de Salud)", 2)
    )

    fin = time.perf_counter()
    print("\n---  Proceso de validacion finalizado ---")
    print(f" Tiempo total transcurrido: {fin - inicio:.2f} segundos")

if __name__ == "__main__":
    asyncio.run(main())