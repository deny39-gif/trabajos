import random, time

attack=random.randint(5,35)
attlu=random.randint(15,50)
captu=random.randint(1,4)
hp1=100
hp2=500

turnos=1

def captura():
    if captu==1:
        print("el pokemon lugia no capturado")
    elif captu==2:
        print("el pokemon lugia logro escapar de la ball")
    elif captu==3:
        print("el pokemon lugia acaba de romper la ball")
    elif captu==4:
        print("pokemon lugia a sido capturado")

movilugia={
    "movi1": "Aeroblast",
    "movi2": "Recuperacion",
    "movi3": "Paz mental",
    "movi4": "Rayo hielo"
}

movichar={
    "movie1": "Danza dragon",
    "movie2": "Puño trueno",
    "movie3": "Garra dragon",
    "movie4": "Lanzallamas"
}

mochi={
    "pocion": 64,
    "superpocion": 32,
    "restauratotal": 6,
    "pokeball": 16,
    "superball": 32,
    "ultraball": 64,
}

def pokedex():
    print("Lugia el pokemon legendario de los mares")
    print("tipo: volador y psiquico")

def menu():
    while True:
        print("="*30)
        print("1.- luchar")
        print("2.- mochila")
        print("3.- analisas")
        print("="*30)
        op=int(input("que opcion elijes?: "))
        if op==1:
            print("movimientos de charizard:")
            for clave, movimientos in movichar.items():
                print("1.-",movichar["movie1"])
                print("2.-",movichar["movie2"])
                print("3.-",movichar["movie3"])
                print("4.-",movichar["movie4"])
                att=int(input("que desea hacer??: "))
                if att==1:
                    print("la defensa de charizard aumentado")
                elif att==2:
                    print("charizard ah usado ", movichar["movie2"])
                    if attack<20:
                        print("el ataque no es efetivo")
                        hp2-=attack
                        turnos+=1
                    elif attack>20:
                        print("ataque super efectivo")
                        hp2-=attack
                        turnos+=1
                elif att==3:
                    print("charizard ah usado ", movichar["movie3"])
                    if attack<20:
                        print("el ataque no es efetivo")
                        hp2-=attack
                        turnos+=1
                    elif attack>20:
                        print("ataque super efectivo")
                        hp2-=attack
                        turnos+=1
                elif att==4:
                    print("charizard ah usado ", movichar["movie3"])
                    if attack<20:
                        print("el ataque no es efetivo")
                        hp2-=attack
                        turnos+=1
                    elif attack>20:
                        print("ataque super efectivo")
                        hp2-=attack
                        turnos+=1


def inicio():
    print(f"un lugia salvaje con {hp2} acaba de aparecer")
    print("Charizard yo te elijo")
    print(f"Charizard: {hp1} de hp")

inicio()
menu()
