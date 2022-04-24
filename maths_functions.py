import math

def calcular_factorial(n: int)->int:
    """Calcula el factorial de un número n"""
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def calcular_factorial_recursivo(n: int)->int:
    """Calcular el factorial de un número de forma recursiva"""
    if n==1:
        return 1
    elif n > 1:
        return n * calcular_factorial_recursivo(n-1)
    
def area_circulo(radio: float, pi: float=3.14)->float:
    """Calcula el área de un circulo

    Args:
        radio (float): Radio del circulo
        pi (float, optional): Valor de PI. Defaults to 3.14.
        
    Returns:
        float: Area del circulo
    """
    potencia = math.pow(radio,2)
    return pi * potencia

# pruebo mis funciones
if __name__ == '__main__':
    x = calcular_factorial(5)
    print(x == 120) # 

    y = calcular_factorial_recursivo(3)
    print(y == 6) # 


    # prueba
    a = area_circulo(1)
    print(a)