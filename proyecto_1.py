"""menu de opciones usando funciones"""

import math

def suma(a: float, b: float) -> float:
    """Suma a + b"""
    return a + b

def resta(a: float, b: float) -> float:
    """resta a - b"""
    return a - b

def multiplicacion(a: float, b: float) -> float:
    """multiplica a * b"""
    return a * b

def division(a: float, b: float) -> float:
    """divide a / b"""
    if b == 0:
        return "No es posible"
    else:
        return a / b

def raiz(nr: float) -> float:
    """encuentra la raiz"""
    try:
        return math.sqrt(nr)
    except ValueError:
        vl = math.sqrt(-nr)
        return f'{vl} j (Imaginario)'

def potenciacion(a: float, b: float) -> float:
    """encuentra la potencia"""
    return a ** b

def logaritmo10(a: float) -> float:
    """encuentra el logaritmo"""
    try:
        return math.log10(a)
    except ValueError:
        return "No es posible hallar logaritmo de un número negativo."

def valida_float(mensaje: str) -> float:
    """valida que reciba un numero decimal

    Args:
        mensaje (str): mensaje que se muestra al usuario

    Returns:
        float: retorna un numero decimal
    """
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Valor no numerico, intente de nuevo...")

def valida_int(mensaje: str, minimo: int, maximo: int) -> int:
    """valida que reciba un numero entero en el rango especificado

    Args:
        mensaje (str): mensaje que se muestra al usuario
        minimo (int): valor minimo del rango
        maximo (int): valor maximo del rango

    Returns:
        int: entero retornado dentro del rango
    """
    while True:
        try:
            num = int(input(mensaje))
            if minimo <= num <= maximo:
                return num
            else:
                print(f"Numero entero fuera de rango ({minimo} - {maximo}), Intente de nuevo")
        except ValueError:
            print("Valor no entero, intente de nuevo.")

def main():
    """Integra las funciones de la calculadora"""
    while True:
        print("*** Menu Principal ***")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Raiz Cuadrada")
        print("6. Potenciacion")
        print("7. Logaritmo")
        print("8. Salir")
        opcion = valida_int("Selecciona una de las opciones: ", 1, 8)
        if opcion == 1:
            nr1 = valida_float("Ingresa el primer numero: ")
            nr2 = valida_float("Ingresa el segundo numero: ")
            print("La suma es: ",suma(nr1,nr2))
        elif opcion == 2:
            nr1 = valida_float("Ingresa el primer numero: ")
            nr2 = valida_float("Ingresa el segundo numero: ")
            print("La resta es: ",resta(nr1,nr2))
        elif opcion == 3:
            nr1 = valida_float("Ingresa el primer numero: ")
            nr2 = valida_float("Ingresa el segundo numero: ")
            print("La multiplicacion es: ",multiplicacion(nr1,nr2))
        elif opcion == 4:
            nr1 = valida_float("Ingresa el primer numero: ")
            nr2 = valida_float("Ingresa el segundo numero: ")
            print("La division es: ",division(nr1,nr2))
        elif opcion == 5:
            nr1 = valida_float("Ingresa el  numero: ")
            print("La raiz cuadrada es: ",raiz(nr1))
        elif opcion == 6:
            nr1 = valida_float("Ingresa el primer numero: ")
            nr2 = valida_float("Ingresa el segundo numero: ")
            print("La potenciacion es: ",potenciacion(nr1,nr2))
        elif opcion == 7:
            nr1 = valida_float("Ingresa el  numero: ")
            print("El logaritmo es: ",logaritmo10(nr1))
        elif opcion == 8:
            break
        else:
            print("Opcion invalida, ingresa un numero del 1 al 8: ")
        input("\nPresione Enter para continuar... ")
        print()

main()
