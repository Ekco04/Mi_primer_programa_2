

tienes_un_pc_input = input('¿Tienes un ordenador? (Si / No): ').upper()

if tienes_un_pc_input == 'SI':
    tienes_un_pc = True
elif tienes_un_pc_input == 'NO':
    tienes_un_pc = False
else:
    print('Te he dicho que me digas si o no, así que lo tomo como que no')
    tienes_un_pc = False



tu_pc_grafica_input = input('¿Tu ordenador tiene una gráfica potente? (Si / No): ').upper()

if tu_pc_grafica_input == 'SI':
    tu_pc_grafica = True
elif tienes_un_pc_input == 'NO':
    tu_pc_grafica = False
else:
    print('Te he dicho que me digas si o no, así que lo tomo como que no')
    tienes_un_pc = False



conexion_internet_cable_input = input('¿Tu ordenador está conectado a internet por cable? (Si / No): ').upper()

if conexion_internet_cable_input == 'SI':
    conexion_internet_cable = True
elif conexion_internet_cable_input == 'NO':
    conexion_internet_cable = False
else:
    print('Te he dicho que me digas si o no, así que lo tomo como que no')
    conexion_internet_cable = False



conexion_internet_wifi_input = input('¿Tu ordenador está conectado a internet via Wi-Fi? (Si / No): ') .upper()

if conexion_internet_wifi_input == 'SI':
    conexion_internet_wifi = True
elif conexion_internet_wifi_input == 'NO':
    conexion_internet_wifi = False
else:
    print('Te he dicho que me digas si o no, así que lo tomo como que no')
    conexion_internet_wifi = False



if tienes_un_pc and tu_pc_grafica and (conexion_internet_cable or conexion_internet_wifi):
    print('Puedes jugar a todos los juegos que quieras')
else:
    print('No puedes jugar')

