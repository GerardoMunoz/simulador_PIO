#import pandas as pd1
import pd_sim as pd2

nombre_archivo = "FSM_dosUnosSeguidos.csv"

#data_frame1 = pd1.read_csv(nombre_archivo)
data_frame2 = pd2.read_csv(nombre_archivo)


# #print(data_frame1)
# print(data_frame2)


# print()

#print(data_frame1.head())
#error print(data_frame2.head())

# print()

# #print(data_frame1.tail())
# #error print(data_frame2.tail())

# print()

# #print(data_frame1.index)
# #error print(data_frame2.index)

# print()

# #print(data_frame1.describe())
# #error print(data_frame2.describe())

# print()


# #print(data_frame1.T)
# print(data_frame2.T)
# #error print(data_frame2.T())


# print()


# #print(data_frame1.sort_index(axis=1, ascending=False))
# #error print(data_frame2.sort_index(axis=1, ascending=False))

# print()

# #print(data_frame1['Est_act'])
# #print(data_frame2['Est_act'])

# print()

# #print(data_frame1[0:3])
# #print(data_frame2[0:3])

# print()

# #print(data_frame1.loc[0])
# #error print(data_frame2.loc[0])
# #error print(data_frame2.loc(0))

# print()

#print(data_frame1.at[1, "Est_act"])
#error print(data_frame2.at[1, "Est_act")])
#error print(data_frame2.at(1, "Est_act"))

# print()

# #print(data_frame1 > 0)
# #error print(data_frame2 > 0)

# print()

# #print(data_frame1.iloc[3])
# #error print(data_frame2.iloc[3])
# #error print(data_frame2.iloc(3))

# print()

# #data_frame1_a=data_frame1.copy()
# #print(data_frame1_a)
# #error data_frame2_a=data_frame2.copy()
# #error print(data_frame2_a)

# print()

# #data_frame1_a['Est_act'] = 0
# #print(data_frame1_a)
# #data_frame2['Est_act'] = 0
# #print(data_frame2)

# print('Función negar -, Gerardo Muñoz')

# #print(-data_frame1)
# print(-data_frame2)

#Test función 1 y 2 iloc
#Oscar David Poblador Parra- 20211005116
# print("\nIloc selección entero y slice - Oscar Poblador 20211005116")
# print("\nPrueba con parámetro entero)
# data=data_frame2.iloc[2]
# print(data)
# #print("\nPreuba con parámetro de 2 slices")
# data=data_frame2.iloc[0:3,1:4] 
# print(data)

#Test función 3 y 6 iloc
#Juan David Bello Rodríguez - 20211005028
# print("\nIloc selección con lista y listas - Juan David Bello Rodríguez 20211005028")
# print("\nPrueba con 2 listas de valores en columnas y en filas")
# data=data_frame2.iloc[[1,3],[1,3]] 
# print(data)
# print("\nPrueba una lista que tiene una fila y columna especifica")
# data=data_frame2.iloc[3,1]
# print(data)

#Test función 4 y 5 iloc
#Manuel Alejandro Guio Cardona - 20211005061
# print("\nIloc seleccion slice y slice completo - Manuel Guio 20211005061")
# print("\nPrueba con slice en columnas (derecha), imprime todas las filas")
# data=data_frame2.iloc[ : ,0:2]
# print(data)
# print("\nPrueba con slice en filas (izquierda), imprime todas las columnas")
# data=data_frame2.iloc[0:2, : ]
# print(data)
