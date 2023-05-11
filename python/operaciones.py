def Sum(value1, value2) :
    """

    :param value1:
    :param value2:
    :return:
    """
    return value1 + value2


def Subtract(value1, value2) :
    """

    :param value1:
    :param value2:
    :return:
    """
    return value1 - value2


def multiplication(value1, value2) :
    """

    :param value1:
    :param value2:
    :return:
    """
    return value1 * value2


def Division(value1, value2) :
    """

    :param value1:
    :param value2:
    :return:
    """
    return value1 / value2


def calculadora(value1, value2) :
    """

    :param value1:
    :param value2:
    :return:
    """
    command = ""
    while command.lower() != "salir" :
        operation = input("Inrtroduzca la operacion que desee realizar +, -, * ,/: ")
        if operation == "+" :
            value1 = Sum(value1, value2)
        elif operation == "-" :
            value1 = Subtract(value1, value2)
        elif operation == "*" :
            value1 = multiplication(value1, value2)
        elif operation == "/" :
            value1 = Division(value1, value2)
        print(value1)
        value2 = float(input("Introduzca otro valor: "))
        command = input("$")


def Area(selection, List) :
    """

    :param selection:
    :param List:
    :return:
    """
    if List[selection] == "triangulo" :
        base = int(input("Introduzca el valor de la base del triangulo: "))
        height = int(input("Introduzca el valor de la altura del triangulo: "))
        result = (base * height) / 2
        return result
    elif List[selection] == "cuadrado" :
        side = int(input("Introduzca el valor del lado del cuadrado: "))
        result = side ** 2
        return result
    elif List[selection] == "rectangulo" :
        base = int(input("Introduzca el valor de la base del rectangulo: "))
        height = int(input("Introduzca el valor de la altura del rectangulo: "))
        result = (base * height)
        return result
    else :
        print("El nombre de la figura es incorrecto")


def CreateFile() :
    name = input("Introduzca el nombre del archivo: ")
    f = open(f'{name}.txt', 'w')
    f.write(input())
    f.close()

    f = open(f'{name}.txt', 'r')
    mensaje = f.read()
    print(mensaje)
    f.close()
