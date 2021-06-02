while True:
    print('''
        Bienvenido a BaseX
        Base10 a baseX(1) | BaseX a base10(2) | BaseX a baseY(3) | Salir(4)
    ''')
    opcion = input('Elija una opcion: ')

    if opcion == '1':
        decimal = int(input('Ingrese un numero en base 10 >> '))
        base = int(input('Ingrese la base (max 10) >> '))
        resultado = ''

        if str(decimal).isdecimal() and base <= 10:
            while decimal >= base:
                residuo = decimal % base
                resultado = str(residuo) + resultado
                decimal = decimal // base

            resultado = str(decimal) + resultado
            print(f'El numero equivalente en base {base} es {resultado}')
            break

        else:
            print('No es un dato válido')
            break

    elif opcion == '2':
        base = int(input('Ingrese la base (max 10) >> '))
        num = input(f'Ingresa un numero en base {base} >> ')
        maximo = int(max(list(num)))
        decimal = 0

        if num.isdecimal() and base <= 10 and base > maximo:
            for i in range(0, len(num)):
                decimal = decimal + (int(num[-(i + 1)]) * (base ** i))

            print(f'El numero decimal equivalente es {decimal}')
            break

        else:
            print('No es un dato válido')
            break

    elif opcion == '3':
        baseX = int(input('Ingrese la base (max 10) >> '))
        num = input(f'Ingresa un numero en base {baseX} >> ')
        maximo = int(max(list(num)))
        decimal = 0
        resultado = ''

        if num.isdecimal() and baseX <= 10 and baseX > maximo:
            for i in range(0, len(num)):
                decimal = decimal + (int(num[-(i + 1)]) * (baseX ** i))

            baseY = int(input('Ingrese la nueva base (max 10) >> '))
            while decimal >= baseY:
                residuo = decimal % baseY
                resultado = str(residuo) + resultado
                decimal = decimal // baseY

            resultado = str(decimal) + resultado
            print(f'El numero equivalente en base {baseY} es {resultado}')
            break

        else:
            print('No es un dato válido')
            break

    elif opcion == '4':
        print('El programa ha finalizado')
        break
