import random


def run():
    numero_aleatoria = random.randint(1, 100)
    numero_elegido = int(input("Eligue un numero: "))
    while numero_elegido != numero_aleatoria:
        if numero_elegido < numero_aleatoria:
            print("busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_elegido = int(input("Elige otro número: "))
    print("Ganaste felicidades!")


if __name__ == "__main__":
    run()