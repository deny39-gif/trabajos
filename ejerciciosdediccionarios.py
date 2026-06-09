pokemon={
    1:{"nombre": "ekans", "nivel": 19},
    2:{"nombre": "gastly", "nivel": 18},
    3:{"nombre": "eevee", "nivel": 17}
}

def monstar():
    print("="*30)
    for p, z in pokemon.items():
        print(f"{p}.-{z}")

def eliminar():
    print("="*30)
    monstar()
    borrarpoke=int(input("cual pokemon desea eliminar: "))
    del pokemon[borrarpoke]

def agregar():
    print("="*30)
    pkm=input("ingrese el nuevo pokemon: ")
    nvl=input("ingrese el nivel del pokemon: ")
    pokemon[list(pokemon.keys())[-1]+1]={"nombre": pkm, "nivel": nvl}


def actulizar():
    print("="*30)
    monstar()
    actualizar=int(input("Que pokemon desea actualizar: "))
    nameP=input("ingresar el nombre del pokemon: ")
    LvlP=input("ingrese el nivel del pokemon: ")
    pokemon[actualizar]={"nombre": nameP, "nivel": LvlP}
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