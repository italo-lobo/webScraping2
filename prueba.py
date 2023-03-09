import time
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

totalxpuesto=[]

# Inicializar el driver de Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navegar a la página de búsqueda de empleos
driver.get("https://empleoscordoba.com.ar/buscar-trabajo/")
# portal 2 https://www.bumeran.com.ar/

ofertasLaborales = {}


i = 1

#siempre que exista un boton en la pagina con mas ofertas hacer clic
def BotonMasOfertas():
    while True:
        time.sleep(5)
        driver.find_element(
            By.CLASS_NAME, "load_more_jobs").send_keys(Keys.ENTER)
        print("vuelta"+str(i))
        i += 1


# busca todos los puestos publicados (rubros)
elemento = driver.find_elements(By.CLASS_NAME, "level-0")
listaPuestos = []
diccionario={}
for i in elemento:
    listaPuestos.append(i.text) #cargo cada uno de los puestos 

#en el buscador ingreso el nombre del primer puesto a buscar 
    driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys(i.text + Keys.ENTER)
    time.sleep(5)
    BotonMasOfertas
  

    soup = BeautifulSoup(driver.page_source, "html.parser")
    resultados = soup.find_all('li', class_="job_listing")
    rubro = i.text
    
    ofertasLaborales= []
    for a in resultados: 
        nombrePuesto = a.h3.get_text()
        link = a.contents[1].attrs['href']
        ofertasLaborales.append({"nombrePuesto": nombrePuesto, "link": link})
        
    
    diccionario[i.text]=ofertasLaborales
   
    totalxpuesto.append(len(ofertasLaborales))        
            
# borrar el input del buscador
    driver.find_element(
        By.CLASS_NAME, "select2-search__field").send_keys(Keys.BACK_SPACE)



print(listaPuestos)
print(totalxpuesto)



with open("json.json","w") as archivo_json:
    archivo_json.write(json.dumps(diccionario))
