import pandas
datos_nasdaq = pandas.read_csv(r'nasdaq.csv')
#print(datos_nasdaq)
dataframe_nasdaq = pandas.DataFrame(datos_nasdaq)
print(dataframe_nasdaq)
