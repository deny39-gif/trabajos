import random, time

hp1=100
hp2=500

turnos=1

def captura():
    captu=random.randint(1,4)
    if captu==1:
        print("el pokemon lugia no capturado")
    elif captu==2:
        print("el pokemon lugia logro escapar de la ball")
    elif captu==3:
        print("el pokemon lugia acaba de romper la ball")
    else:
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

def tunolu():
    global hp1, hp2, turnos
    desicionlu=random.randint(1,4)
    if desicionlu==1:
        print("lugia a usado ", movilugia["movi1"])
        attlu=random.randint(15,50)
        hp1-=attlu
        print("charizard a recibio", attlu,"de daño")
    elif desicionlu==2:
        print("lugia usado ", movilugia["movi2"])
        curacion=random.randint(10,40)
        hp2+=curacion
    elif desicionlu==3:
        print("lugia a usado", movilugia["movi3"])
        print("lugia a aumentado su defensa")
    elif desicionlu==4:
        print("lugia a usado", movilugia["movi4"])
        attlu=random.randint(15,50)
        hp1-=attlu
        print("charizard a recibido", attlu, "de daño")

def pokedex():
    print("Lugia el pokemon legendario de los mares")
    print("tipo: volador y psiquico")

def att2():
    print("charizard ah usado ", movichar["movie2"])
    attack=random.randint(5,35)
    if attack<20:
        print("el ataque no es efetivo")
        p2-=attack
        turnos+=1
    else:
        print("ataque super efectivo")
        hp2-=attack
        turnos+=1
        print("lugia tiene ", hp2," de vida")
        if hp2>0:
            tunolu()

def menu():
    global hp1,hp2,turnos
    print("="*30)
    print("1.- luchar")
    print("2.- mochila")
    print("3.- analisas")
    print("="*30)
    op=int(input("que opcion elijes?: "))
    if op==1:
        print("movimientos de charizard:")
        print("1.-",movichar["movie1"])
        print("2.-",movichar["movie2"])
        print("3.-",movichar["movie3"])
        print("4.-",movichar["movie4"])
        att=int(input("que desea hacer??: "))
        if att==1:
            print("la defensa de charizard aumentado")
        elif att==2:
            att2()
        elif att==3:
            print("charizard ah usado ", movichar["movie3"])
            attack=random.randint(5,35)
            if attack<20:
                print("el ataque no es efetivo")
                hp2-=attack
                turnos+=1
            else:    
                print("ataque super efectivo")
                hp2-=attack
                turnos+=1
                if hp2>0:
                    tunolu()
        elif att==4:
            print("charizard ah usado ", movichar["movie3"])
            attack=random.randint(5,35)
            if attack<20:
                print("el ataque no es efetivo")
                hp2-=attack
                turnos+=1
            else:
                print("ataque super efectivo")
                hp2-=attack
                turnos+=1
                if hp2>0:
                    tunolu()
        elif op==2:
            print("="*30)
            print("="*11, "Curar", "="*12)
            print("="*30)
            print(".- Pocion:", mochi["pocion"])
            print(".- Super posion:", mochi["superpocion"])
            print(".- Restuara total:", mochi["restauratotal"])
            print("="*30)
            print("="*10, "Pokeball", "="*10)
            print("="*30)
            print(".- Poke Ball:", mochi["pokeball"])
            print(".- Super Ball:", mochi["superball"])
            print(".- Ultra Ball:", mochi["ultraball"])
            opbol=int(input("que objeto desea usar?: "))


def inicio():
    print(f"un lugia salvaje con {hp2} acaba de aparecer")
    print("Charizard yo te elijo")
    print(f"Charizard: {hp1} de hp")

inicio()
while hp1>0 and hp2>0:
    menu()
