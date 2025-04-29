from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import concurrent.futures

# Definir la lista de equipos
ns_Equipos_Top_Wanted,topWanted = (45, 73, 241, 243),{}

#TODO: scrap multi-get
ns_Equipos_Laliga_EA_Sports,laliga_EA_Sports=(240, 241, 243, 448,
                                              449, 450, 452, 453,
                                              457, 461, 462, 463,
                                              472, 479, 480, 481,
                                              483, 1860, 100888,
                                              110062),{}
ns_Equipos_Actuales,dicc_Actual=ns_Equipos_Laliga_EA_Sports,\
                                laliga_EA_Sports

'''[(448, ['Athletic Club']), (240, ['Atlético de Madrid']),
(463, ['D. Alavés']), (241, ['FC Barcelona']),
(110062, ['Girona FC']), (462, ['R. Valladolid CF']),
(450, ['RC Celta']), (453, ['RCD Mallorca']),
(480, ['Rayo Vallecano']), (449, ['Real Betis']),
(243, ['Real Madrid']), (457, ['Real Sociedad']),
(483, ['Villarreal CF'])]
'''

# Configurar el servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicializar el navegador con Selenium
driver = webdriver.Chrome(service=service)

# URL de la página
cadena=''

for nEquipo in ns_Equipos_Actuales: cadena+=f"&team={nEquipo}"

# Cargar la página web
driver.get(f"https://ea.com/games/ea-sports-fc/ratings?{cadena}")

# Función para obtener el valor de cada equipo
#def get_team_value(nEquipo):    
try:
    # Esperar hasta que el elemento esté presente
    tag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Tag_labelWrapper__s6Seg"))
    )

    # Buscar todos los elementos con esa clase
    tags = driver.find_elements(By.CLASS_NAME, "Tag_labelWrapper__s6Seg")
    
    # Guardar todos los textos de los tags
    #[tag.text for tag in tags if tag.text]
    print([tag.text for tag in tags])

except:
    print(f"e: 'Tag_labelWrapper__s6Seg'")

# Cerrar el navegador
driver.quit()

# Usar concurrent.futures para ejecutar los procesos en paralelo
#with concurrent.futures.ThreadPoolExecutor() as executor:
#    executor.map(get_team_value, ns_Equipos_Actuales)

#print(sorted(dicc_Actual.items(), key=lambda x:x[1]))
