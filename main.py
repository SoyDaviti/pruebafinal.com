from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from mongo import MongoConnection

db_client = MongoConnection().client
db = db_client.get_database('Pruebafinal')
col = db.get_collection('autos')

driver = webdriver.Chrome()
driver.get("https://ecuador.patiotuerca.com/usados/-/autos?type_autos_moderated=moderated")
autos = driver.find_elements(By.CLASS_NAME, value="vehicle-container")
for a in autos:
    auto_name = a.find_element(by=By.TAG_NAME, value="img").accessible_name
#    auto_modelo = driver.find_element(by=By.CLASS_NAME, value='module').text
    auto_detalle = a.find_element(by=By.CLASS_NAME, value='year').text
    auto_precio = a.find_element(by=By.CLASS_NAME, value='price-text').text
    auto_negociable = a.find_element(by=By.CLASS_NAME, value='latam-secondary-text').text

    document = {
        "modelo_auto": auto_name,
        "anio_auto": auto_detalle,
        "precio_auto:": auto_precio,
        "auto_detalle:": auto_negociable
    }
    col.insert_one(document=document)


    print(auto_name)
#    print(auto_modelo)
    print(auto_detalle)
    print(auto_precio)
    print(auto_negociable)
    print('='*40)

   # detalle = a.find_element(by=By.CLASS_NAME, value="vehicle-href")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
driver.close()
