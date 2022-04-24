


def sumar(x: int, y: int)->int :
    """ Retorna la suma de x + y"""
    return x + y

def restar(x: int, y: int)->int :
    """ Retorna la suma de x - y"""
    return x - y

def multiplicar(x: int, y: int)->int :
    """ Retorna la suma de x + y"""
    return x * y

def dividir(x: int, y: int)->int :
    """ Retorna la suma de x + y"""
    
    try:
        return x / y
    except ZeroDivisionError:
        return 0