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
        OPCION = input("Elija una opcion: ")

        if OPCION == "1":
            decimal = int(input("Ingrese un numero en base 10 >> "))
            BASE = int(input("Ingrese la base (max 10) >> "))
            resultado = ""

            if str(decimal).isdecimal() and BASE <= 10:
                while decimal >= BASE:
                    residuo = decimal % BASE
                    resultado = str(residuo) + resultado
                    decimal = decimal // BASE

                resultado = str(decimal) + resultado
                print(f"El numero equivalente en base {BASE} es {resultado}")
                break

            print("No es un dato válido")
            break

        if OPCION == "2":
            BASE = int(input("Ingrese la base (max 10) >> "))
            NUM = input(f"Ingresa un numero en base {BASE} >> ")
            MAXIMO = int(max(list(NUM)))
            decimal = 0

            if NUM.isdecimal() and MAXIMO < BASE <= 10:
                for i in range(0, len(NUM)):
                    decimal = decimal + (int(NUM[-(i + 1)]) * (BASE ** i))

                print(f"El numero decimal equivalente es {decimal}")
                break

            print("No es un dato válido")
            break

        if OPCION == "3":
            BASE_X = int(input("Ingrese la base (max 10) >> "))
            NUM = input(f"Ingresa un numero en base {BASE_X} >> ")
            MAXIMO = int(max(list(NUM)))
            decimal = 0
            resultado = ""

            if NUM.isdecimal() and MAXIMO < BASE_X <= 10:
                for i in range(0, len(NUM)):
                    decimal = decimal + (int(NUM[-(i + 1)]) * (BASE_X ** i))

                BASE_Y = int(input("Ingrese la nueva base (max 10) >> "))

                while decimal >= BASE_Y:
                    residuo = decimal % BASE_Y
                    resultado = str(residuo) + resultado
                    decimal = decimal // BASE_Y

                resultado = str(decimal) + resultado
                print(f"El numero equivalente en base {BASE_Y} es {resultado}")
                break

            print("No es un dato válido")
            break

        if OPCION == "4":
            print("El programa ha finalizado")
            break


if __name__ == "__main__":
    main()
