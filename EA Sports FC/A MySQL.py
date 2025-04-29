laliga_EA_Sports = [('Atlético de Madrid', 240), ('FC Barcelona', 241),
('Real Madrid', 243), ('Athletic Club', 448), ('Real Betis', 449),
('RC Celta', 450), ('RCD Espanyol', 452), ('RCD Mallorca', 453),
('Real Sociedad', 457), ('Valencia CF', 461),
('R. Valladolid CF', 462), ('D. Alavés', 463),
('UD Las Palmas', 472), ('CA Osasuna', 479),
('Rayo Vallecano', 480), ('Sevilla FC', 481),
('Villarreal CF', 483), ('Getafe CF', 1860),
('CD Leganés', 100888), ('Girona FC', 110062)]

nom_bd = 'EA_Sports_FC'

print(f'''CREATE DATABASE {nom_bd};\n
USE {nom_bd};\n''')

for par in laliga_EA_Sports:
    nom_Equipo,ID=par
    nom_Equipo = nom_Equipo.replace(" ", "_")

#con acentos graves (cadena) para que R. no de error
    print(f'''CREATE TABLE `{nom_Equipo}` (
    ID INT PRIMARY KEY NOT NULL
);\n
INSERT INTO `{nom_Equipo}` (ID) VALUES ({ID});\n''')

print(f'DROP DATABASE {nom_bd};')
