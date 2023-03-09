import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_json('/home/ilobbo/Documentos/ITALO/Repositorio/webScraping2/json.json')

Rates = [i["nombrePuesto"] for i in data["Administración"]]
Qty = [i['link'] for i in data['Administraci\u00f3n']]

plt.plot(Rates, Qty)
plt.show()