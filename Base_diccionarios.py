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

def ingresar(dic):
    ingre=input("que vehiculo desea ingresar?: ")
    if not validemarc(ingre):
        print("dato invalido")
        return False
    model=input("que tipo es?: ")
    if not validemarc(model):
        print("dato invalido")
        return False
    anio=int(input("que año lo obtuvo: "))
    if not valianio(anio):
        print("dato invalido")
        return False
    ranking=int(input("de cual es el ranking: "))
    if not valirang(ranking):
        print("dato invalido")
        return False
    codigo=input("ingresar el codigo")
    if not validemarc(codigo):
        print("dato invalido")
        return False
    dic[codigo]=[ingre, model, anio, ranking]
    operaciones[codigo]=["02-07-2026", "pendiente"]

def mostrar(dic):
    for codigo, value in dic.items():
        print(f"{codigo}.- {value}")

def validemarc(m):
    if m==None or m==" ":
        return False
    else:
        return True

def validartex(tex):
    if tex.strip()=="":
        return False
    else:
        return True

def valianio(ani):
    if ani<1900:
        return False
    else:
        return True

def valirang(dic):
    if 1<=dic<=5:
        return True
    else:
        return False

def valife(dic):
    if dic.strip()=="":
        return True
    return False

    
# def vendidos(dic, marca):
#     for codigo, value in dic.items():
#         if marca==value["marca"]


def busqueda_por_anio(anio_min, anio_max):
    resultados = []
    for vehiculo in autos:
        dentro_de_rango = anio_min <= vehiculo["anio"] <= anio_max
        esta_pendiente = vehiculo["fecha_venta"] == "Pendiente"
        if dentro_de_rango and esta_pendiente:
            autos = f"{vehiculo['marca']} {vehiculo['modelo']}--{vehiculo['id']}"
            resultados.append(autos)
        if not resultados:
            print(f"\nNo se encontraron vehículos disponibles entre los años {anio_min} y {anio_max}.")
    else:
        resultados.sort()
        print(f"\n--- Vehículos encontrados ({anio_min} - {anio_max}) ---")
        for item in resultados:
            print(item)

# def vendidos(dic, marca):
#     print()

# def eliminar(id_auto):
#     mostrar(autos)
#     borr=input("que auto desea eliminar?")
#     if borr
#         autos[id_auto].remove(borr)

# ingresar(autos)
# print("="*40)
# mostrar(autos)

print("="*12, "menu", "="*12)
print(".-")
print(".-")
print(".-")
print(".-")
print(".-")
print(".-")