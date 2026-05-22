import time
import numpy as np


def primos_optimizado_numpy(limit=100000):
    # Criba de Eratóstenes con NumPy (muy rápida)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False

    # Solo iterar hasta raíz cuadrada de n
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False

    # List comprehension para crear la lista final
    primos = np.array([i for i, es_primo in enumerate(sieve) if es_primo], dtype=np.int32)
    return primos


if __name__ == "__main__":
    inicio = time.perf_counter()
    primos = primos_optimizado_numpy(100000)
    fin = time.perf_counter()

    print("Cantidad de números primos:", len(primos))
    print("Tiempo de ejecución:", fin - inicio, "segundos")