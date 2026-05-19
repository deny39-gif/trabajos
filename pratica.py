# ''' praticar los videas del ava de python'''

# nombre=input("ponga su nombre por favor: ")
# edad=int(input("su edad por favor: "))
# print(f"hola, su nombre es {nombre} y su edad es {edad}")


# indie=0
# estudio=0

# cantjue=int(input("cuantos juegos desea registrar?: "))

# for i in range(cantjue):
#     print(f"--- Game {i+1} ---")
#     while True:
#         nombre=input("ingresar el nombre del juego:").upper()
#         if len(nombre)<5:
#             print("el nombre debe tener 5 caracteres")
#         elif " " in nombre:
#             print("no tener espacio")
#         elif nombre:
#             print("juego ingresado")
#             while True:
#                     calificacion=input("ingresar calificacion del juego: [E / +12 / M] ").upper()
#                     if calificacion=="E":
#                         pubilco="Para todo"
#                     elif calificacion=="+12":
#                         pubilco="Adolecentes (12 a 17)"
#                     elif calificacion=="M":
#                             pubilco="para mayores de 18 (+18)"
#                     else:
#                         print("calificacion invalida")
#                         continue
#                     break
#         while True:
#                 try:
#                     precio=int(input("a cuanto esta el juego?: "))
#                     if precio<=0:
#                         print("precio no es positivo o numero no requirido")
#                     if precio >=20000 and precio<40000:
#                         categoria="indie"
#                         indie+=1
#                         break
#                     elif precio>=40000:
#                         categoria="estudio"
#                         estudio+=1
#                         break
#                     else:
#                         categoria="economico" 
#                         break
#                 except ValueError:
#                     print("debe ingresar numeros")

#         print("===== Resumen =====")
#         print(f"cantidad de juegos indie:{indie}")
#         print(f"cantidad de juegos de estudio:{estudio}")
#         break

deuda=100000
op=0
while True:
    print('''
===== Menu =====
1.- tarjeta de credito
2.- simulaciom de compras
3.- salir
''')
    op=int(input("eliga una opcion: "))
    if op==1:
        try:
            print(f"su deuda es de ${deuda} pesos")
            monto=float(input("ingresa el monto a pagar: $"))
            if monto<=0:
                print("error, monto no puede ser negativo o 0")
            elif monto>deuda:
                print("error, monto no puede superar la deuda actual")
            else: 
                deuda-=monto
                print("pago realizado con exito")
                print(f"su deuda restante es: ${deuda}")
        except ValueError:
            print("error, ingresar un numero valido por favor")
    if op==2:
        try:
            canti=int(input("cunatas compreas desar realizar??"))
            totaldecom=0
            for i in range(canti):
                montocom=float(input(f"ingresa el monto de la compra{i+1}: $"))
                if montocom<0:
                    print("error, monto no puede ser negativo o 0")
                else:
                    totaldecom+=montocom
                    deuda+=montocom
                    print("compra hecha de forma exitosa")
                    print(f"su deuda es de ahora: ${deuda}")
                    print(f"total gastado en compras: ${totaldecom}")
        except ValueError:
            print("error: se debe ingresar valores numeros validos, por favor")
    if op==3:
        print("saliendo, que tenga una buena tarde")
        break
    else:
        print("opcion invalida")