from random import choice
import json
import numpy as np
import matplotlib.pyplot as plt

#Lectura de archivo json
eje_x=np.array([i for i in range(38)])
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)

print("--------PROCESAMIENTO--------------")
print(len(data)) 		#iteracion N, ejecutado desde el main
print(len(data[0]))		# i/38 configuraciones
print(len(data[0][0]))		# valores y claves
iteracion=0
unode38=0
clave_de_valor='avg'
print(data[0][0]['avg']) #[iteracion N][iteracion 1/38][valor en la clave]


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
    

