import pandas as pd
import matplotlib.pyplot as mpl

#Traer datos con pandas

dataframe = pd.read_csv('ventas.csv')

#revenue calculado con pandas(ventas - gastos)  creando una nueva columna con el nombre Ganancias.

dataresult= dataframe.assign(Ganancia= dataframe["Ventas"] - dataframe["Gastos"])
print(dataresult)

# Codigo de grafico con matplotlib que indica el tamaño, leyenda, los nombres, labels, eje x y y.

mpl.figure(figsize=(8,8))
mpl.plot(dataframe["Mes"], dataframe["Ventas"], label="Ventas")
mpl.plot(dataframe["Mes"], dataframe["Gastos"], label="Gastos")
mpl.title("Phyton II \n Laboratorio 4 \n csv chart" )
mpl.xlabel("Meses")
mpl.ylabel("Monto")
mpl.legend()
mpl.show()

