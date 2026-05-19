# saldo=100000

# while True:
#     print("---CAJERO AUTOMATICO---")
#     print("1.- consultar saldo")
#     print("2.- retirar dinero")
#     print("3.- depositar dinero")
#     print("4.- salir")
#     print("---CAJERO AUTOMATICO---")
#     try:
#         op=int(input("selecione una opcion: "))
#         if op==1:
#             print(f"su saldo es de ${saldo}")
#         elif op==2:
#             try:
#                 retiro=int(input("ingrese el monto que desea retirar: "))
#                 if retiro<=5000:
#                     print("el monto debe ser mayor que 0")
#                 elif retiro%5000!=0:
#                     print("solo se permiten montos de $5000")
#                 elif retiro>saldo:
#                     print("saldo insuficiente")
#                 else:
#                     saldo-=retiro
#                     print(f"retiro aprovado, su saldo es: {saldo}")
#             except ValueError:
#                 print("debe ingresar un valor numerico valido")
#         elif op==3:
#             try:
#                 deposito=int(input("ingresar el monto a depositar: "))
#                 if deposito<=5000:
#                     print("el monto debe ser mayor a 0")
#                 elif deposito%5000!=0:
#                     print("solo se permiten montos multiple de $5000")
#                 else:
#                     saldo+=deposito
#                     print(f"deposito aprovado, su saldo es: ${saldo}")
#             except ValueError:
#                 print("debe ingresar un valor numerico valido")
#         elif op==4:
#             print("que tenga un buen dia caballero o dama")
#             break
#         else:
#             print("opcion invalida, por favor vuelva a intentarlo")
#     except ValueError:
#         print("por favor vuelva intentarlo")

