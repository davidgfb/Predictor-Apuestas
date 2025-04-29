from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import concurrent.futures

'''OBJ: buscamos uno por uno en serie en la misma ventana para
optimizar la memoria, no sobrecargar y que no nos bloquee el
servidor
'''

# Definir la lista de equipos
ns_Equipos_Most_Wanted,mostWanted,\
ns_Equipos_Laliga_EA_Sports,laliga_EA_Sports=(45, 73, 241, 243),{},\
                                             (240, 241, 243, 448,
                                              449, 450, 452, 453,
                                              457, 461, 462, 463,
                                              472, 479, 480, 481,
                                              483, 1860, 100888,
                                              110062),{}
ns_Equipos_Actuales,dicc_Actual=ns_Equipos_Laliga_EA_Sports,\
                                laliga_EA_Sports

# Configurar el servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicializar el navegador con Selenium
driver = webdriver.Chrome(service=service)

for nEquipo in ns_Equipos_Actuales:
    # Cargar la página web
    driver.get(f"https://ea.com/games/ea-sports-fc/ratings?team={nEquipo}")

    # Función para obtener el valor de cada equipo
    #def get_team_value(nEquipo):    
    try:
        # Esperar hasta que el elemento esté presente
        tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Tag_labelWrapper__s6Seg"))
        )

        dicc_Actual[tag.text]=nEquipo
        print({tag.text:nEquipo})

    except:
        print(f"e: {nEquipo}")

# Cerrar el navegador
driver.quit()

print(sorted(dicc_Actual.items(), key=lambda x:x[1]))

'''laliga_EA_Sports
[('Atlético de Madrid', 240), ('FC Barcelona', 241),
('Real Madrid', 243), ('Athletic Club', 448), ('Real Betis', 449),
('RC Celta', 450), ('RCD Espanyol', 452), ('RCD Mallorca', 453),
('Real Sociedad', 457), ('Valencia CF', 461),
('R. Valladolid CF', 462), ('D. Alavés', 463),
('UD Las Palmas', 472), ('CA Osasuna', 479),
('Rayo Vallecano', 480), ('Sevilla FC', 481),
('Villarreal CF', 483), ('Getafe CF', 1860),
('CD Leganés', 100888), ('Girona FC', 110062)]

mostWanted
[('Juventus', 45), ('Paris SG', 73), ('FC Barcelona', 241),
('Real Madrid', 243)]
'''
