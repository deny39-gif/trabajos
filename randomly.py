# uso y ejmeplos de ramdom

import random, time
# num=random.randint(1,10)
# print(num)

# for i in range(num):
#     print("hola deny")

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)

# print(f"el dado 1 dio {dado1} y el 2 dio {dado2}")

# if dado1==dado2:
#     print("se va a la carcel")
# else:
#     print("avance por favor")

# cont=5
# rnum=random.randint(1,100)
# print("adivana el numero entre 1 y 100, tines 5 intentos: ")

# while cont>0:
#     nume=int(input("adivona el numero random: "))
#     if nume==rnum:
#         print(f"felicidades adivino el numero {rnum}")
#         break
#     elif nume > rnum:
#         print("te pasate")
#         cont-=1
#         print(f"intentos restantes: {cont}")
#     else:
#         print("el numero es mayor")
#         cont-=1
#         print(f"intentos restantes: {cont}")
# if cont==0:
#     print(f"se acabaron los intentos. el numnero era: {rnum}")

# hp1=100
# hp2=100
# perj1=input("nombra al personaje1: ")
# perj2=input("nombra al personaje2: ")
# turno=1

# print("que comience la pelea")
# while hp1>0 and hp2>0:
#     print(f"turno {turno}")
#     # el jugador uno
#     daño=random.randint(7, 18)
#     hp2-=daño
#     print(f"el {perj1} hace de {daño} de daño")
#     print(f"el {perj2} tiene {hp2} de vida")

#     if hp2<=0:
#         break
#     # el jugador dos
#     daño=random.randint(7, 18)
#     hp1-=daño
#     print(F"el {perj2} hace de {daño} de daño")
#     print(f"el {perj1} tiene {hp1} de vida")

#     print("-----------------")
#     time.sleep(2)
#     turno+=1

# print("resultado de final: ")
# print(f"{perj1} tiene de vida: {hp1}")
# print(f"{perj2} tiene de vida: {hp2}")

# if hp1 > 0:
#     print(f"{perj1} ha sido el ganador")
# else:
#     print(f"{perj2} ha sido el ganador")

# vip=1.8
# genral=1.4
# tibuna=1.2
# enrada=4000
# op=0
# codigopro=random.randint(7000, 21000)
# print(f"este es su codigo postal {codigopro}")
# print("1.- Vip")
# print("2.- general")
# print("3.- tribunal")
# print("4.-salir")
# op=int(input("donde quiere su lugar?"))
# while op!=4:
#     match op:
#         case 1:
#             print(f"la entreda vip cuesta {enrada*vip}")
#             break
#         case 2:
#             print(f"la entreda general cuesta {enrada*genral}")
#             break
#         case 3:
#             print(f"la entreda tribunal cuesta {enrada*tibuna}")
#             break
#         case _:
#             print("entonces quire cancelar? entiendo, regrese pronto")
#             break

rnum1=[random.randint(1,9) for _ in range(3)]

print(f"los numeros ganadores son {rnum1}")
intentos=0
time.sleep(1)
while True:
    intentos+=1
    intento = [random.randint(1,9) for _ in range(3)]

    if intento == rnum1:
        print(f"intento: {intento}")
        print("Jackpot! ganaste")
        print(f"numeros de intentos fueron realizados: {intentos}")
        break

# n1=random.randint(1,9)
# n2=random.randint(1,9)
# n3=random.randint(1,9)
# t1=False
# t2=False
# t3=False
# intentos=0
# print(f"los numero ganadores son: [{n1},{n2},{n3}]")

# while not n1 or not n2 or not n3:
#     print(f"el numero es: {intento}")
#     intento=random.randint(1,9)
#     time.sleep(1)
#     if intento==n1:
#         t1=True
#     if intento==n2:
#         t2=True
#     if intento==n3:
#         t3=True
#     intentos+=1
# print(f"jackpot! ganaste! numeros de intentos fueron realizados: {intentos}")

'''

'''