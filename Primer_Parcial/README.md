# Aplicaciones Distribuidas — Primer Parcial
Implementación de tres ejercicios en Python para demostrar distintos modelos de ejecución: procesamiento secuencial, concurrencia asíncrona y sincronización de hilos. Todos los ejercicios se ejecutan dentro de Docker para mantener un entorno reproducible.

## Repositorio público
https://github.com/kjgavilanez/Aplicaciones_Distribuidas

## Requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.
- Git, para clonar el repositorio.
- Docker Compose, incluido en las versiones actuales de Docker Desktop.

No es necesario instalar Python localmente. La imagen `python:3.11-alpine` se descarga automáticamente al ejecutar los comandos.

## Ejecución con Docker

### 1. Clonar el repositorio
```bash
git clone https://github.com/kjgavilanez/Aplicaciones_Distribuidas.git
cd Aplicaciones_Distribuidas/Primer_Parcial
```

### 2. Ejecutar los ejercicios
Cada comando crea un contenedor temporal, ejecuta el script indicado y lo elimina al finalizar:
Ejecutarlos en el orden que se encuantran

```bash
# Ejercicio 1: ejecución secuencial
docker compose run --rm python-app python Ej1_Secuencial/secuencial_platillo.py

# Ejercicio 2: concurrencia asíncrona
docker compose run --rm python-app python Ej2_Concurrente/concurrente_verificar_documento.py

# Ejercicio 3: hilos con Lock
docker compose run --rm python-app python Ej3_Hilos_lock/hilo_con_lock_cine.py
```

También se puede ejecutar el comando predeterminado del servicio, que corresponde al ejercicio secuencial:

```bash
docker compose up
```

### 3. Detener y limpiar los recursos
```bash
docker compose down
```

## Estructura del proyecto
```text
Primer_Parcial/
├── docker-compose.yml
├── README.md
├── Ej1_Secuencial/
│   └── secuencial_platillo.py
├── Ej2_Concurrente/
│   └── concurrente_verificar_documento.py
└── Ej3_Hilos_lock/
    └── hilo_con_lock_cine.py
```

## Resultados esperados
- **Ejercicio 1:** prepara una entrada, un plato principal y un postre de forma secuencial; el tiempo total aproximado es de 6 segundos.
- **Ejercicio 2:** valida tres documentos simultáneamente; el tiempo total aproximado corresponde a la operación más lenta, 3 segundos.
- **Ejercicio 3:** dos clientes intentan reservar un único asiento VIP, pero el `Lock` garantiza que solo uno obtenga la reserva.

## Autor
**Kenny Gavilánez**  
Ingeniería de Software — Aplicaciones Distribuidas
