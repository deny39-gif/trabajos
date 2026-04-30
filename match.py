# op=0
# total=0
# while op!=4:
#     print("1.- Pc $500.000")
#     print("2.- LGTV Pulgadas $450.000")
#     print("3.- Microondas Madesa $100.000")
#     print("4.- salir")
#     op=int(input())
#     match op:
#         case 1:
#             print("el total a pagar es ", 500000*1.19)
#             total+=500000*1.19
#         case 2:
#             print("el total a pagar es ", 450000*1.19)
#             total+=450000*1.19
#         case 3:
#             print("el total a pagar es ", 100000*1.19)
#             total+=100000*1.19
#         case 4:
#             print("salida")
#             print("el total a pagar es ", total)
#         case _:
#             print("opcion invalidad")

# a==B
# a!=b
# a>=b
# a<=b

# num1=int(input("ingresar un numero: "))
# num2=int(input("ingresar un numero: "))
# print(f"{num1} + {num2} = {num1+num2}")
# print(f"{num1} / {num2} = {num1/num2}")
# print(f"{num1} * {num2} = {num1*num2}")
# print(f"{num1} - {num2} = {num1-num2}")

# def suma():
#     num1=int(input("ingresar un numero: "))
#     num2=int(input("ingresar un numero: "))
#     print(f"{num1} + {num2} = {num1+num2}")

# def dividir():
#     num1=int(input("ingresar un numero: "))
#     num2=int(input("ingresar un numero: "))
#     print(f"{num1} / {num2} = {num1/num2}")

# def multi():
#     num1=int(input("ingresar un numero: "))
#     num2=int(input("ingresar un numero: "))
#     print(f"{num1} * {num2} = {num1*num2}")

# def resta():
#     num1=int(input("ingresar un numero: "))
#     num2=int(input("ingresar un numero: "))
#     print(f"{num1} - {num2} = {num1-num2}")
# op=0
# while op!=5:
    # print("1.- sumar")
    # print("2.- dividir")
    # print("3.- multiplicar")
    # print("4.- restar")
    # print("5.- salir")
    # op=int(input())
    # match op:
    #     case 1:
    #         suma()
    #     case 2:
    #         dividir()
    #     case 3:
    #         multi()
    #     case 4:
    #         resta()
    #     case 5:
    #         print("salida")
    #     case _:
            # print("opcion invalidad")


# def niños():
#        total+=total+kids

# def adultos():
#        total+=total+adults

# def mayores():
    #    total+=total+oldmans


# c=0
# op=0
# cantPer=0
# total=0
# while op!=4:
#     print('''
#           1.- Niños(1-17) $1.000
#           2.- adultos (18-64) $3.000
#           3.- adulto mayor (64 o mas) $1.500
#           4.- salir
#           ''')
#     op=int(input("eliga una opcion por favor: "))
#     match op:
#         case 1:
#             print("comprando la entrada del niño: ")
#             c=int(input("cuentos niños son? "))
#             while c<1 or c>10:
#                 print("lo siento,s solo se permiten entre 1 a 10 personas")
#                 c=int(input("cuentos niños son? "))
#             total+=+1000*c
#             cantPer+=c
#         case 2:
#             print("comprando la entrada del adulto: ")
#             c=int(input("cuentos son? "))
#             while c<1 or c>10:
#                 print("lo siento, solo se permiten entre 1 a 10 personas")
#                 c=int(input("cuentos son? "))
#             total+=3000*c
#             cantPer+=c
#         case 3:
#             print("comprando la entrada de la persona mayor: ")
#             c=int(input("cuentos son? "))
#             while c<1 or c>10:
#                 print("lo siento,s solo se permiten entre 1 a 10 personas")
#                 c=int(input("cuentos son? "))
#             total+=1500
#             cantPer+=c
#         case _:
#             print(f"seria en total, {total} a pagar")
#             print(f"estas son la persona que van: {cantPer}")

