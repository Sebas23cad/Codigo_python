from tkinter.messagebox import NO


def run():
    # for contador in range(30):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 20:
    #         break

    # texto = input("Escribe un texto: ")
    # for i in texto:
    #     if i == "o":
    #         break
    #     print(i)

    # LIMITE = 1000

    # contador = 0
    # potencia = 2**contador
    # while potencia < LIMITE:
    #     print(str(potencia))
    #     if potencia == 32:
    #         break
    #     contador += 1
    #     potencia = 2**contador

    palabra = int(input("Escribe un numero: "))
    NOMBRE = 6

    while palabra != NOMBRE:

        palabra += 1
        if palabra % 2 != 0:
            continue
        print(palabra)


if __name__ == "__main__":
    run()