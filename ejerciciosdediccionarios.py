# pokemon={
#     1:{"nombre": "ekans", "nivel": 19},
#     2:{"nombre": "gastly", "nivel": 18},
#     3:{"nombre": "eevee", "nivel": 17}
# }

# def monstar():
#     print("="*30)
#     for p, z in pokemon.items():
#         print(f"{p}.-{z}")

# def eliminar():
#     print("="*30)
#     monstar()
#     borrarpoke=int(input("cual pokemon desea eliminar: "))
#     del pokemon[borrarpoke]

# def agregar():
#     print("="*30)
#     pkm=input("ingrese el nuevo pokemon: ")
#     nvl=input("ingrese el nivel del pokemon: ")
#     pokemon[list(pokemon.keys())[-1]+1]={"nombre": pkm, "nivel": nvl}

# def actulizar():
#     print("="*30)
#     monstar()
#     actualizar=int(input("Que pokemon desea actualizar: "))
#     nameP=input("ingresar el nombre del pokemon: ")
#     LvlP=input("ingrese el nivel del pokemon: ")
#     pokemon[actualizar]={"nombre": nameP, "nivel": LvlP}
#     print("actualizacion con exito")
# def Menupokemon():
#     while True:
#         try:
#             print("="*30)
#             print("1.-agregar pokemon")
#             print("2.-eliminar pokemon")
#             print("3.-actualizar pokemon")
#             print("4.-Mostrar pokemon")
#             print("5.-salir")
#             op=int(input("selecione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actulizar()
#                 case 4:
#                     monstar()
#                 case 5:
#                     print("saliendo")
#                     break
#         except ValueError as e:
#             print("solo nuneros enteros, error:",e)

# Menupokemon()

# produc={
#     1:{"producto": "Uva", "precio": 2000},
#     2:{"producto": "palta", "precio": 4000},
#     3:{"producto": "pera", "precio": 1500}
# }

# def mostr():
#     print("="*30)
#     for P, d in produc.items():
#         print(f"{P}.-{d}")

# def camb():
#     print("="*30)
#     mostr()
#     actualizar=int(input("Que producto desea actualizar: "))
#     nameP=input("ingresa el producto: ")
#     Precio=input("cuanto cuasta ese producro: ")
#     produc[actualizar]={"nombre": nameP, "nivel": Precio}
#     print("actualizacion con exito")

# def elimi():
#     print("="*30)
#     mostr()
#     borrarpro=int(input("cual pokemon desea eliminar: "))
#     del produc[borrarpro]

# def agre():
#     print("="*30)
#     pro=input("ingrese el producto al carrito: ")
#     pre=input("cuanrp cuesta este prodcuto: ")
#     produc[list(produc.keys())[-1]+1]={"producto": pro, "nivel": pre}

# def comp():
#     mostr()
#     compra=int(input("que producto desea comnprar)"))
#     for compra in produc:
#         print(f"usted a comprado {pro}")

# while True:
#     try:
#         print("1.-agregar porducto")
#         print("2.-cambiar producto")
#         print("3.-eliminar producto")
#         print("4.-mostar productos")
#         print("5.- comprar")
#         print("6.- Salir")
#         print("="*30)
#         op=int(input("que quiere hacer: "))
#         if op==1:
#             agre()
#         elif op==2:
#             camb()
#         elif op==3:
#             elimi()
#         elif op==4:
#             mostr()
#         elif op==5:

parking={
    1:[2000,3500,2000,2000,3500,2000,2000,3500,2000],
    2:[],
    3:[],
    4:[]
}

tarifa={
    "ligero": 2000,
    "mediano": 3000,
    "pesado": 3500,
}

Lig=0
pes=0
med=0

ganacias=0

def ingre():
    global ganacias, Lig, pes, med

    tipo=input("Tipo de vehiculo (ligero, mediano, pesado)").lower()
    if tipo=="ligero":
        Lig+=1
    elif tipo=="mediano":
        med+=1
    elif tipo=="pesado":
        pes+=1
    elif tipo not in tarifa:
        print("Tipo de vehiculo invalido")
        return
    for piso in parking:
        if len(parking[piso])<10:
            parking[piso].append(tarifa[tipo])
            ganacias+=tarifa[tipo]
            print(f"vehiculos estacionados en {piso}")
            print(f"espacios ocupados:{len(parking[piso])}/10")
            return

while True:
    try:
        print("="*30)
        print("1.- Ingresar vehiculos")
        print("2.- Contar ganancias")
        print("3.- Contar vehiculos")
        print("4.- Mostrar parking")
        print("5.- Salir")
        print("="*30)
        op=int(input("seleciona una opcion: "))

        if op==1:
            ingre()
        elif op==2:
            print("las ganancias son:", ganacias)
        elif op==3:
            total=0
            for piso in parking:
                total+=len(parking[piso])
            print("vehiculos en total:", total)
            print("ligeros:", Lig)
            print("medianos:", med)
            print("Pesados:", pes)
        elif op==4:
            for piso in parking:
                print(f"piso {piso}:{parking[piso]}")
        elif op==5:
            print("se termino")
            break
        else:
            print("opcion invalida")
    except ValueError:
        print("solamente numeros por favor")