

tienes_un_pc_input = input('¿Tienes un ordenador? (Si / No): ').upper()

if tienes_un_pc_input == 'SI':
    tienes_un_pc_input = True
elif tienes_un_pc_input == 'NO':
    tienes_un_pc_input = False
else:
    print('Te he dicho que me digas si o no')
    tienes_un_pc_input = False



tu_pc_grafica_input = input('¿Tu ordenador tiene una gráfica potente? (Si / No): ').upper()
conexion_internet_cable_input = input('¿Tu ordenador está conectado a internet por cable? (Si / No): ').upper()
conexion_internet_wifi_input = input('¿Tu ordenador está conectado a internet via Wi-Fi? (Si / No): ') .upper()



tienes_un_pc = tienes_un_pc_input == 'SI'
tu_pc_grafica = tu_pc_grafica_input == 'SI'
conexion_internet = conexion_internet_cable_input == 'SI' or conexion_internet_wifi_input == 'SI'



if tienes_un_pc and tu_pc_grafica and conexion_internet:
    print('Puedes jugar a todos los juegos que quieras')
else:
    print('No puedes jugar')

