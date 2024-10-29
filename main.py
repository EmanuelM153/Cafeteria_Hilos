import random
import time
import queue
import concurrent.futures
import threading

cola_pedidos = queue.Queue()
cafetera = threading.Lock()

def trabajador(num):
    while True:
        orden_id = cola_pedidos.get()
        if orden_id is None:
            print("No hay ordenes")
            break

        print(f"Trabajador {num}: Tomando la orden: {orden_id}")
        time.sleep(random.randint(1, 3))

        cafetera.acquire()
        print(f"Trabajador {num}: Preparando el café para la orden: {orden_id}")
        time.sleep(random.randint(2, 4))
        cafetera.release()

        print(f"Trabajador {num}: Sirviendo la orden: {orden_id}")
        time.sleep(random.randint(1, 2))

        print(f"Trabajador {num}: Orden {orden_id} completada y servida.")
        cola_pedidos.task_done()

def main():
    num_trabajadores = 5

    with concurrent.futures.ThreadPoolExecutor(max_workers = num_trabajadores) as executor:
        executor.map(trabajador, range(num_trabajadores))

        orden_id = 0
        while True:
            print(f"Agregando la orden {orden_id} a la cola de pedidos.")
            cola_pedidos.put(orden_id)
            time.sleep(random.uniform(2, 3))
            orden_id += 1

if __name__ == "__main__":
    main()
