# Sistema de Preparación de Café Multi-hilo

Este programa simula un sistema donde varios trabajadores (hilos) procesan órdenes de café de manera concurrente, gestionando la sincronización para evitar conflictos y asegurar el flujo correcto de cada orden.

## Descripción del Código

- **Variables Globales**:
  - `cola_pedidos`: Cola de pedidos (`queue.Queue`) para gestionar las órdenes en orden de llegada.
  - `cafetera`: Candado (`threading.Lock`) para sincronizar el acceso a la cafetera y evitar conflictos entre hilos.

- **Funciones Principales**:
  - `trabajador(num)`: Función que toma órdenes de la cola, prepara el café (asegurando que solo un trabajador use la cafetera a la vez), y luego sirve el pedido.
  - `main()`: Crea varios hilos de trabajadores usando `ThreadPoolExecutor`. Genera órdenes continuamente y las añade a `cola_pedidos`.

## Sincronización y Concurrencia

- **Asignación de Hilos**: Cada trabajador se ejecuta en un hilo independiente, permitiendo la concurrencia.
- **Sincronización**: La cafetera utiliza un candado (`Lock`) para evitar que dos hilos preparen café al mismo tiempo.
- **Flujo de Trabajo**: Los trabajadores deben tomar la orden antes de prepararla y servirla, manteniendo el orden y sincronización adecuados.

Ejecuta el script con:

```bash
python nombre_del_archivo.py

