import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import prueba as p



fig1, ax1 = plt.subplots()
fig, ax = plt.subplots()
# Colocamos una etiqueta en el eje Y
ax.set_ylabel('Puestos')
# Colocamos una etiqueta en el eje X
ax.set_title('Cantidad de puestos disponibles')
# Creamos la grafica de barras utilizando 'los puestos' como eje Y y 'cantidad de puestos' como eje X.
ax.barh(p.listaPuestos, p.totalxpuesto)
# Creamos el grafico, añadiendo los valores
ax1.pie(p.totalxpuesto, labels=p.listaPuestos, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.savefig('barras_horizontal.png')
plt.show()
