# sim argumento y sin retorno

# def saludo():
#     print("hola lucas")
# saludo()


# n="nano"
# def chao():
#     print("nos vemos", n)
# chao()

# def suma():
#     num1=int(input("ingresar un numero: "))
#     num2=int(input("ingresar un numero: "))
#     print(f"{num1} + {num2} = {num1+num2}")

# suma()

# def saludame(name):
#     print(f"hola {name}")
# saludame("deny")

# def resta(n1,n2):
#     print(f"el resultao de la resta es:{n1-n2}")
# resta(10,5)

# def multi():
#     num1=8
#     num2=23
#     return num1+num2
# vari=multi()*4
# print(vari)

# def restaCrest(n1,n2):
#     return n1-n2
# print(restaCrest(9,3))

# crear una calculadora, para ejecutar
# las operaciones bacisas
# ddebe usar argumntos y retorno

# def sumarcr(n1,n2):
#     return n1+n2

# def restcre(r1,r2):
#     return r1-r2

# def multicre(m1,m2):
#     return m1*m2

# def dividecre(d1,d2):
#     return d1/d2

# op=0
# def calculadora():
#     while True:
#         try:
#             print("="*30)
#             print("1.- Sumar ")
#             print("2.- restar ")
#             print("3.- multi ")
#             print("4.- dividir ")
#             print("5.- salir")
#             print("="*30)
#             op=int(input("eliga que operacion desea hacer: "))

#             if op==1:
#                 nu1=int(input("ingresa el primer numero: "))
#                 nu2=int(input("ingresa el segundo numero: "))
#                 print(f"el resultado es: {sumarcr(nu1,nu2)}")
#             elif op==2:
#                 re1=int(input("ingresa el primer numero: "))
#                 re2=int(input("ingresa el segundo numero: "))
#                 print(f"el resultado es: {restcre(re1,re2)}")
#             elif op==3:
#                 mu1=int(input("ingresa el primer numero: "))
#                 mu2=int(input("ingresa el segundo numero: "))
#                 print(f"el resultado es: {multicre(mu1,mu2)}")
#             elif op==4:
#                 di1=int(input("ingresa el primer numero: "))
#                 di2=int(input("ingresa el segundo numero: "))
#                 print(f"el resultado es: {dividecre(di1,di2)}")
#             elif op==5:
#                 print("calculadora sin bateria")
#                 break
#             else:
#                 print("opcion invalida, eliga una de las opciones")
#         except Exception as e:
#             print("error:", e)

# calculadora()

# def Caliva(precio, iva):
#     total=precio+(precio*iva/100)
#     return total

# precio=int(input("ingrese el precio del producto: "))
# iva=int(input("ingrese el porcentaje de iva: "))
# resultado=Caliva(precio, iva)
# print("el precio con el iva incluido es:", resultado)


