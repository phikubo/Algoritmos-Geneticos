from random import choice
import json
import numpy as np
import matplotlib.pyplot as plt

#Lectura de archivo json
eje_x=np.array([i for i in range(38)])
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    #print(data)

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
#para la primera iteracion externa los 38 valores
for i in range(len(data[0])):
    primera_iteracion_valor_max.append(data[0][i]['max'])
    primera_iteracion_valor_min=np.append(primera_iteracion_valor_min, data[0][i]['min'])
print(len(primera_iteracion_valor_max), len(primera_iteracion_valor_min))


fig, ax = plt.subplots()
plt.plot( eje_x, primera_iteracion_valor_max, "bo-")
plt.plot(eje_x,primera_iteracion_valor_min, "g*-")

ax.grid()
ax.set_axisbelow(True)

# Customize the grid
#ax.grid(linestyle='-', linewidth='0.5', color='red')
ax.grid(which='minor', linewidth='0.5', color='black')

# Turn on the minor TICKS, which are required for the minor GRID
ax.minorticks_on()

# Turn off the display of all ticks.
ax.tick_params(which='bsoth', # Options for both major and minor ticks
                top='False', # turn False top ticks
                left='False', # turn False left ticks
                right='False',  # turn False right ticks
                bottom='False') # turn off bottom ticks
plt.show()
    
