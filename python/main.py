from operaciones import *
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Escoja la opcion que desee realizar: ")
option = input("1...2...3 :")
if option == "1" :
    try :
        value1 = float(input("Introduzca el primer valor: "))
        value2 = float(input("Introduzca el otro valor: "))
    except ValueError :
        print("El valor es incorrecto, tiene que ser un numero")
    else :
        calculadora(value1, value2)

if option == "2" :
    List = ["triangulo", "cuadrado", "rectangulo"]
    try :
        selection = int(
            input(
                "Escriba el numero de la figura al que le quiere hallar el area 0-triangulo,1- cuadrado o 2-rectangulo: "))
        print(List[selection])
        result = Area(selection, List)
        print(f"El area del {selection} es {result}")

    except IndexError :
        print("Opcion incorrecta debe estar entre 0 y 2")
    except ValueError :
        print("Tienes que poner un numero entero")

if option == "3" :
    CreateFile()