import time
import matplotlib.pyplot as plt
import numpy as np


def primos_original(limit=100000):
    primos = []
    for num in range(2, limit + 1):
        es_primo = True
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos


def primos_optimizado_numpy(limit=100000):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    primos = np.array([i for i, es_primo in enumerate(sieve) if es_primo], dtype=np.int32)
    return primos


def medir_tiempo(func, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        func(100000)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos


if __name__ == "__main__":
    tiempos_original = medir_tiempo(primos_original, repeticiones=3)
    tiempos_optimizado = medir_tiempo(primos_optimizado_numpy, repeticiones=5)

    # 1) Distribución de tiempos
    plt.figure(figsize=(8, 5))
    plt.hist(tiempos_original, alpha=0.6, label="Original")
    plt.hist(tiempos_optimizado, alpha=0.6, label="Optimizado")
    plt.title("Distribución de tiempos de ejecución")
    plt.xlabel("Segundos")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.tight_layout()
    plt.savefig("distribucion_tiempos.png", dpi=120)

    # 2) Comparativa de promedios
    prom_original = np.mean(tiempos_original)
    prom_optimizado = np.mean(tiempos_optimizado)

    plt.figure(figsize=(6, 4))
    plt.bar(["Original", "Optimizado"], [prom_original, prom_optimizado], color=["tomato", "seagreen"])
    plt.title("Comparativa de tiempos promedio")
    plt.ylabel("Segundos")
    plt.tight_layout()
    plt.savefig("comparativa_tiempos.png", dpi=120)

    print("Promedio original:", prom_original)
    print("Promedio optimizado:", prom_optimizado)