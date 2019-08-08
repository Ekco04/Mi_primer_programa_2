operación = input('!Hola¡ ¿Qué operacion quieres realizar? (Suma / Resta / Multipilicaión / División):')

while operación == 'Suma':
    primer_numero = int(input('Dame el primer número: '))
    segundo_numero = int(input('Dame el segundo número:'))
    resultado = primer_numero + segundo_numero
    print('El resultado es {}'.format(resultado))

while operación == 'Resta':
    primer_numero = int(input('Dame el primer número: '))
    segundo_numero = int(input('Dame el segundo número:'))
    resultado = primer_numero - segundo_numero
    print('El resultado es {}'.format(resultado))

while operación == 'Multipilicaión':
    primer_numero = int(input('Dame el primer número: '))
    segundo_numero = int(input('Dame el segundo número:'))
    resultado = primer_numero * segundo_numero
    print('El resultado es {}'.format(resultado))

while operación == 'División':
    primer_numero = int(input('Dame el primer número: '))
    segundo_numero = int(input('Dame el segundo número:'))
    resultado = primer_numero / segundo_numero
    print('El resultado es {}'.format(resultado))

print('No me has dicho bien la operacion que quieres que realize')
