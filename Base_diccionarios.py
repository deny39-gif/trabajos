#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}

operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}


# def buscaauto(lista,busca):
#     if busca in lista:
#         print(lista[busca])
#     else:
#         print("codigo de vehiculo no existe")
# op=input("que auto desea buscar???: ")
# buscaauto(autos,op)

def ingresar(dic):
    ingre=input("que vehiculo desea ingresar?: ")
    model=input("que tipo es?: ")
    anio=int(input("que año lo obtuvo: "))
    ranking=int(input("de cual es el ranking: "))
    codigo=input("ingresar el codigo")
    dic[codigo]=[ingre, model, anio, ranking]



def mostrar(dic):
    for codigo, value in dic.items():
        print(f"{codigo}.- {value}")
 
    
def vendidos(dic, marca):
    for codigo, value in dic.items():
        if marca==value["marca"]

ingresar(autos)
print("="*40)
mostrar(autos)