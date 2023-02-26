import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Inicializar el driver de Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navegar a la página de búsqueda de empleos
driver.get("https://empleoscordoba.com.ar/buscar-trabajo/")
# portal 2 https://www.bumeran.com.ar/




i=1

def BotonMasOfertas():
    while True:
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "load_more_jobs").send_keys(Keys.ENTER)
        print("vuelta"+str(i))
        i+=1

# elementos = driver.find_elements(By.ID, "search_categories")
elemento = driver.find_elements(By.CLASS_NAME,"level-0")
puestos = []

for i in elemento:
    puestos.append(i.text)
    driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys(i.text + Keys.ENTER)
    time.sleep(5)
    BotonMasOfertas
    print(i.text + "############################################")
    ofertas = driver.find_elements(By.CLASS_NAME, "position")
    # for a in ofertas:
    #     print(a.text)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    resultados = soup.find_all('div',class_="position")
   
    for i in resultados:
        print(i.h3.get_text())
        
    driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys(Keys.BACK_SPACE)
 

