from random import choice
import json
import numpy as np
import matplotlib.pyplot as plt
import numpy
#Lectura de archivo json
eje_x=np.array([i for i in range(38)])

def abrir_archivo():
    with open("data_file.json", "r") as read_file:
        datos = json.load(read_file)
    return datos

def get_estadisticas_2_ejecuciones(data):
    primera_iteracion_valor_min=np.array([])
    segunda_iteracion_valor_min=np.array([])
    for i in range(len(data[0])):
        print(i)
        primera_iteracion_valor_min=np.append(primera_iteracion_valor_min, data[0][i]['min'])
        segunda_iteracion_valor_min=np.append(segunda_iteracion_valor_min, data[1][i]['min'])
    return primera_iteracion_valor_min, segunda_iteracion_valor_min

def get_estadisticas_n_ejecuciones(data):
    n_iteracion_valor   =   np.array([])
    for k in range(len(data)):
        
        for i in range(len(data[0])):
            print(k, i)
            n_iteracion_valor   =   np.append(n_iteracion_valor, data[k][i]['min'])
    return n_iteracion_valor

def get_estadistica_promedio_n_ejecuciones(n_data):
    longitud=len(n_data)
    relacion=longitud/38
    lista=[]
    n_array=np.array([])
    #resultado da 2 por ejemplo, luego creo 2 vectores para luego apilarlos
    for i in range(2):
        lista.append("vector"+str(i))
    #print(lista)
    for i in lista:
        i=np.array([])
        n_array=vstack((i))    
        
    
    n_iteracion_valor   =   np.array([])
    '''Los primeros 38 valores van en un vector, los siguientes 38 en otro y asi
    sucesivamente.'''
    for i in range(len(n_data)):
        pass


def get_estadistica_promedio(data, primer_set, segundo_set):
    primera_iteracion_valor_min=np.array([])
    segunda_iteracion_valor_min=np.array([])
    n_iteracion_valor   =   np.array([])
    for i in range(1):
        pass
    #estadistica_promedio = np.array([])
    #for i in range(len(primer_set)):
    #    estadistica_promedio    =   np.append( estadistica_promedio, primer_set[0])
    #    estadistica_promedio    =   np.append( estadistica_promedio, segundo_set[0])


#MAIN

data = abrir_archivo()
print("--------PROCESAMIENTO--------------")
print("Numero de iteraciones: ",len(data)) 		#iteracion N, ejecutado desde el main
print("Numero de configuraciones : ",len(data[0]))		# i/38 configuraciones
print("Claves y valores: ",len(data[0][0]))		# valores y claves
#iteracion=0
#unode38=0
#clave_de_valor='avg'
#print(data[iteracion][unode38]['avg']) #[iteracion N][iteracion 1/38][valor en la clave]
print("------------------------------------")
#conseguir 


#primer_set,segundo_set=get_estadisticas_2_ejecuciones(data)
todos_los_valores_minimos=get_estadisticas_n_ejecuciones(data)
#print(len(primer_set), len(segundo_set))
#print( primer_set)
#print(primer_set[0])
print(int(len(todos_los_valores_minimos)/38))

get_estadistica_promedio_n_ejecuciones(todos_los_valores_minimos)




'''
primera_iteracion_valor_max=[]
primera_iteracion_valor_min=np.array([])
#para la primera iteracion externa
for i in range(len(data[0])):
    primera_iteracion_valor_max.append(data[0][i]['max'])
    primera_iteracion_valor_min=np.append(primera_iteracion_valor_min, data[0][i]['min'])
print(len(primera_iteracion_valor_max), len(primera_iteracion_valor_min))
#print(primera_iteracion_valor_max)

#plt.hist(primera_iteracion_valor_max, bins=40)
plt.plot( eje_x, primera_iteracion_valor_max, "bo-")
plt.plot(eje_x,primera_iteracion_valor_min, "g*-")
plt.grid(True)
plt.show()
'''
