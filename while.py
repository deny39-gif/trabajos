# cont=1
# while cont<=3:
#     print(f"el contador es {cont}")
#     cont+=1

# num=int(input("ingrese un numero por favor: "))
# cont=1
# while cont<=10:
#     print(num, " X ", cont, " = ", num*cont)
#     cont+=1

# code=4545
# while True:
#     pasw=int(input("ingresar su codigo de 4 digitos: "))
#     if pasw==code:
#         print("codigo aceptado")
#         break
#     else:
#         print("codigo incorrecto")

while True:
    sex=input("ingrese su sexo (F/M):").lower()
    if sex =="m":
        print("no se puede acceder aqui")
    else:
        print("adelante")
        break