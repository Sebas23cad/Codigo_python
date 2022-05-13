def conversor(tipo_moneda, valor_dolar):
    pesoscol = float(input("¿Cuantos pesos tienes ? "))
    dolares= pesoscol / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " " + tipo_moneda)


menu = """"
Bienvenido al conversor de monedas 😊

1 - Dolar
2 - Euro
3 - Cake
4 - Bitcoin

Elige una opcion: """

opcion = input(menu)

if opcion == "1":
    conversor("Dolar", 3679)
elif opcion == "2":
    conversor("Euros", 4383)
elif opcion == "3":
    conversor("Cake", 58800)
elif opcion == '4':
    conversor("Bitcoin", 136134100)
else:
    print("Ingresa una opcion correcta profavor 🤬")