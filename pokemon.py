import random

attack=random.randint(5,35)
captu=random.randint(1,4)
hp1=100
hp2=500

def captura():
    if captu==1:
        print("el pokemon lugia no capturado")
    elif captu==2:
        print("el pokemon lugia logro escapar de la ball")
    elif captu==3:
        print("el pokemon lugia acaba de romper la ball")
    elif captu==4:
        print("pokemon lugia a sido capturado")
        break

movilugia={
    "movi1": "Aeroblast",
    "movi2": "Recuperacion",
    "movi3": "Paz mental",
    "movi4": "Rayo hielo"
}

movichar={
    "movi1": "Danza dragon",
    "movi2": "Puño trueno",
    "movi3": "Garra dragon",
    "movi4": "Lanzallamas"
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
    print("="*30)
    print(".-")
    print(".-")
    print(".-")

print(f"un lugia salvaje con {hp2} acaba de aparecer")
print("Charizard yo te elijo")
print(f"Charizard: {hp1} de hp")


