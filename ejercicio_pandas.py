import pandas as pd
ventas_mensuales = [
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},
{"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
{"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
{"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
{"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
{"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]

"""
● Agrupa los datos por trimestre y calcula el total de ventas para cada trimestre.
● Filtrar y mostrar solo los meses donde las ventas superen 20000.
● Encontrar el mes con el mayor volumen de ventas y mostrar esta información.
● Calcular el promedio de ventas mensuales y mostrar esta información.
● Crea un DataFrame que incluya dos columnas una para los meses y otra para
el total de ventas de cada mes.
"""
dataframe = pd.DataFrame(ventas_mensuales)

#Trimestres separados

#año 2023
trimestre1_2023 = pd.DataFrame(dataframe[0:3])
trimestre2_2023 = pd.DataFrame(dataframe[3:6])
trimestre3_2023 = pd.DataFrame(dataframe[6:9])
trimestre4_2023 = pd.DataFrame(dataframe[9:12])

#año 2024
trimestre1_2024 = pd.DataFrame(dataframe[12:15])
trimestre2_2024 = pd.DataFrame(dataframe[15:18])
trimestre3_2024 = pd.DataFrame(dataframe[18:21])
trimestre4_2024 = pd.DataFrame(dataframe[21:24])

#obtener las ventas por trimestre, sumando los valores de la columna con el metodo sum()
def obtener_ventas_trimestre(trimestre):
    resultado = trimestre["total_ventas"].sum()
    return resultado

print("Ventas trimestre1 2023,",obtener_ventas_trimestre(trimestre1_2023))
print("Ventas trimestre2 2023,",obtener_ventas_trimestre(trimestre2_2023))
print("Ventas trimestre3 2023,",obtener_ventas_trimestre(trimestre3_2023))
print("Ventas trimestre4 2023,",obtener_ventas_trimestre(trimestre4_2023))
print("Ventas trimestre1 2024,",obtener_ventas_trimestre(trimestre1_2024))
print("Ventas trimestre1 2024,",obtener_ventas_trimestre(trimestre2_2024))
print("Ventas trimestre1 2024,",obtener_ventas_trimestre(trimestre3_2024))
print("Ventas trimestre1 2024,",obtener_ventas_trimestre(trimestre4_2024))

#funcion para filtrar los meses donde la venta superar los 20000
def filtrar_meses(dataframe):
    limite = 20000
    meses = dataframe[dataframe['total_ventas'] > limite]
    return meses

print("Ventas supeiores a 20000: ")
print(filtrar_meses(dataframe))


#● Encontrar el mes con el mayor volumen de ventas y mostrar esta información.
def obtener_mayor_volumen_ventas(dataframe):

    venta_mayor = dataframe[dataframe['total_ventas'] == (dataframe["total_ventas"].max())]
    return venta_mayor

print("mes con mayor volumen de ventas: ")
print(obtener_mayor_volumen_ventas(dataframe))

#obtener el promedio de ventas mensual.
def obtener_promedio(dataframe):
    #con el metodo mean se obtiene el promedio de la columna total_ventas
    promedio_ventas = dataframe['total_ventas'].mean()
    return  promedio_ventas

print("Promedio de ventas mensual es de: ",obtener_promedio(dataframe))

#Crea un DataFrame que incluya dos columnas una para los meses y otra para el total de ventas de cada mes.
def nuevo_dataframe(dataframe):
    datos = dataframe[["mes" , "total_ventas"]]
    dataframe2 = pd.DataFrame(datos)
    return  dataframe2
print("Nuevo dataframe con solo los meses y el total de ventas")
print(nuevo_dataframe(dataframe))