import matplotlib.pyplot as plt
from ejercicio_pandas import dataframe as datos
import pandas as pd
meses = ["Enero","Febrero","Marzo","Abril","Mayo", "Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]

ventas_2023 = pd.DataFrame(datos[0:12])
ventas_2024 = pd.DataFrame(datos[12:24])

plt.plot(meses, ventas_2023["total_ventas"], color='red')
plt.plot(meses, ventas_2024["total_ventas"])
plt.title("Grafico de ventas por mes")
plt.xlabel("Meses 2023-2024")
plt.ylabel("Ventas")
plt.legend("34")
plt.show()
