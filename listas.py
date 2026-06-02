# #     -5  -4  -3  -2  -1
# lista=[10, 6, 20, 4, 16]
# #      0   1   2  3  4

# print(lista)
# print(lista[2])
# print(lista[-5])
# print("-"*30)

# for i in lista:
#     print(i)

# print("-"*30)
# lista.append(64)
# for i in lista:
#     print(i)

# fruta=["Frutilla", "Pera", "Manzana", "Naraja"]

# print("="*30)
# for f in fruta:
#     print(f)
# print("="*30)

pokemon=["ekans", "gastly"]
def monstar():
    c=1
    print("="*30)
    for p in pokemon:
        print(c,".- ", p)
        c+=1
def eliminar():
    print("="*30)
    monstar()
    # borrarpoke=input("cual pokemon desea eliminar")
    # pokemon.remove(borrarpoke)
    borrarpoke=int(input("cual pokemon desea eliminar: "))
    pokemon.pop(borrarpoke-1)
def agregar():
    print("="*30)
    pkm=input("ingrese el nuevo pokemon: ")
    pokemon.append(pkm)
def actulizar():
    print("="*30)
    monstar()
    actualizar=int(input("Que pokemon desea actualizar: "))
    pokemon[actualizar-1]=input("cual sera nuevo nombre?: ")
    print("actualizacion con exito")
def Menupokemon():
    while True:
        try:
            print("="*30)
            print("1.-agregar pokemon")
            print("2.-eliminar pokemon")
            print("3.-actualizar pokemon")
            print("4.-Mostrar pokemon")
            print("5.-salir")
            op=int(input("selecione una opcion: "))
            match op:
                case 1:
                    agregar()
                case 2:
                    eliminar()
                case 3:
                    actulizar()
                case 4:
                    monstar()
                case 5:
                    print("saliendo")
                    break
        except ValueError as e:
            print("solo nuneros enteros, error:",e)

Menupokemon()