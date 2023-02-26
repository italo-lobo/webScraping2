import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Inicializar el driver de Selenium
driver = webdriver.Chrome("/home/ilobbo/Documentos/ITALO/Repositorio/webScraping2/chromedriver")

# Navegar a la página de búsqueda de empleos
driver.get("https://empleoscordoba.com.ar/buscar-trabajo/")

# Esperar a que cargue la página y luego hacer clic en el botón "Aceptar" para aceptar las cookies
time.sleep(3)
# driver.find_element_by_xpath("//button[contains(text(), 'Aceptar')]").click()

# Crear una lista para almacenar los trabajos
trabajos = []

while True:
    # Obtener los resultados de búsqueda de la página actual
    soup = BeautifulSoup(driver.page_source, "html.parser")
    resultados = soup.find_all("div", class_="elementor-post")

    # Iterar sobre cada resultado de búsqueda y recopilar información sobre el trabajo
    for resultado in resultados:
        trabajo = {}

        # Obtener el título del trabajo
        titulo = resultado.find("h3", class_="elementor-post__title").text.strip()
        trabajo["titulo"] = titulo

        # Obtener la empresa que publicó el trabajo
        empresa = resultado.find("div", class_="elementor-post__meta-data").find_all("span")[1].text.strip()
        trabajo["empresa"] = empresa

        # Obtener la ubicación del trabajo
        ubicacion = resultado.find("div", class_="elementor-post__meta-data").find_all("span")[0].text.strip()
        trabajo["ubicacion"] = ubicacion

        # Obtener el enlace del trabajo
        enlace = resultado.find("a", class_="elementor-post__read-more")["href"]
        trabajo["enlace"] = enlace

        # Agregar el trabajo a la lista de trabajos
        trabajos.append(trabajo)

    # Verificar si hay un botón "Siguiente"
    boton_siguiente = soup.find("div", class_="elementor-post__pagination").find("a", class_="next page-numbers")
    if boton_siguiente:
        # Si hay un botón "Siguiente", hacer clic en él y esperar a que se cargue la siguiente página
        driver.get(boton_siguiente["href"])
        time.sleep(3)
    else:
        # Si no hay un botón "Siguiente", detener la iteración y cerrar el navegador de Selenium
        break

driver.quit()

# Guardar la lista de trabajos como un archivo JSON
with open("trabajos.json", "w") as f:
    json.dump(trabajos, f, indent=4)
