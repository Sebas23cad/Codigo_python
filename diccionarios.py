def run():
    dicionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    # print(dicionario['llave1'])
    # print(dicionario["llave3"])
    # print(dicionario["llave2"])

    poblacio_paises = {
        "Argentina": 44938712,
        "Brazil": 210147125,
        "Colombia": 50372424,
    }

    # for pais in poblacio_paises.keys():
    #     print(pais)

    # for pais in poblacio_paises.values():
    #     print(pais)

    for pais, poblacion in poblacio_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")



if __name__ == '__main__':
    run()