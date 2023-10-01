from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ecuador.patiotuerca.com/usados/-/autos?type_autos_moderated=moderated")
autos = driver.find_elements(By.CLASS_NAME, "vehicle-container")
#for a in autos:
   #auto_name = a.find_element(by=By.TAG_NAME, value="img").accessible_name
   #auto_modelo = a.find_element(by=By.CLASS_NAME, value="module tittle").text
   #auto_detalle = a.find_element(by=By.CLASS_NAME, value="latam-secondary-text test-lighten-2 left vehicle-highlight").text
   #auto_precio = a.find_element(by=By.CLASS_NAME, value="price-text").text
   #print(auto_name)
   #print(auto_modelo)
   #print(auto_detalle)
   #print(auto_precio)

   # detalle = a.find_element(by=By.CLASS_NAME, value="vehicle-href")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
driver.close()
