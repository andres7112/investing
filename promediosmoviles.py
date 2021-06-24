import numpy
import pandas #importamos la librería para manipulación de datos
import matplotlib.pyplot #importamos la librería para visualización de datos
datos_nasdaq = pandas.read_csv(r'nasdaq.csv') #importamos los datos de nasdaq de un mes
#print(datos_nasdaq)
dataframe_nasdaq = pandas.DataFrame(datos_nasdaq) #creamos un dataframe con los datos que importamos.
#print(dataframe_nasdaq)
matplotlib.pyplot.plot(dataframe_nasdaq.loc[:,"Date"], dataframe_nasdaq.loc[:,"Close"])
matplotlib.pyplot.xlabel("Fecha")
matplotlib.pyplot.ylabel("Precio Stock")
matplotlib.pyplot.title("Gráfica de datos Nasdaq")
matplotlib.pyplot.show()
promedio_movil=dataframe_nasdaq.loc[:,"Close"].rolling(2).mean()
print(promedio_movil)
fecha=dataframe_nasdaq.loc[:,"Date"]
matplotlib.pyplot.plot(dataframe_nasdaq.loc[:,"Date"], promedio_movil)
matplotlib.pyplot.xlabel("Fecha")
matplotlib.pyplot.ylabel("Precio Stock")
matplotlib.pyplot.title("Promedios Móviles")
matplotlib.pyplot.show()