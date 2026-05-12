# while True:
#     try:
#         num=int(input("ingrese un numero: "))
#         break
#     except:
#         print("solamente ingresra numero enteros, no ingresar palabras")

# op=0
# total=0
# while op!=4:
#     try:
#         print("1.- Pc $500.000")
#         print("2.-  LGTV 55 pulgadas $450.000")
#         print("3.- Micri")
#         print("4.- salir")
#         print("eliga que comprar")
#         op=int(input())
#     except ValueError as e:
#         print("error", e)
#         print("solo se ha acepentan numeros enteros")
#         match op:
#             case 1:
#                 print("el total a pagar es ", 500000*1.19)
#                 total+=500000*1.19
#             case 2:
#                 print("el total a pagar es ", 450000*1.19)
#                 total+=450000*1.19
#             case 3:
#                 print("el total a pagar es ", 100000*1.19)
#                 total+=100000*1.19
#             case 4:
#                 print("salida")
#                 print("el total a pagar es ", total)
#             case _:
#                 print("opcion invalidad")

cantidad=int(input("cuantos pasajes desas vender?: "))
total=0
for i in range(cantidad):
    while True:
        try:
            precio=input(f"ingresa el precio del pasaje {i+1}: ")
            precio=float(precio)
            total+=precio
        except ValueError:
            print("debes ingresar un valor numerico")
        break
print(f"el total de ingresor del pasaje es: {total} ") 