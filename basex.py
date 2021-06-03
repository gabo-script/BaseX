"""
Name: BaseX
Date: June 3, 2021
Created by Gaboscript
"""


def main():

    """
    Programa que convierte un número en base numérica n
    a la base que el usuario quiera
    """

    while True:
        print(
            """
            Bienvenido a BaseX
            Base10 a baseX(1) | BaseX a base10(2) | BaseX a baseY(3) | Salir(4)
        """
        )
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            decimal = int(input("Ingrese un numero en base 10 >> "))
            base = int(input("Ingrese la base (max 10) >> "))
            resultado = ""

            if str(decimal).isdecimal() and base <= 10:
                while decimal >= base:
                    residuo = decimal % base
                    resultado = str(residuo) + resultado
                    decimal = decimal // base

                resultado = str(decimal) + resultado
                print(f"El numero equivalente en base {base} es {resultado}")
                break

            print("No es un dato válido")
            break

        if opcion == "2":
            base = int(input("Ingrese la base (max 10) >> "))
            num = input(f"Ingresa un numero en base {base} >> ")
            maximo = int(max(list(num)))
            decimal = 0

            if num.isdecimal() and maximo < base <= 10:
                for i in range(0, len(num)):
                    decimal = decimal + (int(num[-(i + 1)]) * (base ** i))

                print(f"El numero decimal equivalente es {decimal}")
                break

            print("No es un dato válido")
            break

        if opcion == "3":
            base_x = int(input("Ingrese la base (max 10) >> "))
            num = input(f"Ingresa un numero en base {base_x} >> ")
            maximo = int(max(list(num)))
            decimal = 0
            resultado = ""

            if num.isdecimal() and maximo < base_x <= 10:
                for i in range(0, len(num)):
                    decimal = decimal + (int(num[-(i + 1)]) * (base_x ** i))

                base_y = int(input("Ingrese la nueva base (max 10) >> "))

                while decimal >= base_y:
                    residuo = decimal % base_y
                    resultado = str(residuo) + resultado
                    decimal = decimal // base_y

                resultado = str(decimal) + resultado
                print(f"El numero equivalente en base {base_y} es {resultado}")
                break

            print("No es un dato válido")
            break

        if opcion == "4":
            print("El programa ha finalizado")
            break


if __name__ == "__main__":
    main()
