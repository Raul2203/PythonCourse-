"""Modulo que contiene funciones para la validacion e ingreso de datos"""

def ingreso_entero(msg :str ="Ingrese un número entero: ") -> int:
    """Retorna un número entero solicitado al usuario"""
    try:
        x = int(input(msg))
        return x
    except:
        return ingreso_entero(msg)

def ingreso_decimal(msg :str ="Ingrese un número decimal: ") -> float:
    """Retorna un número decimal solicitado al usuario"""
    try:
        x = float(input(msg))
        return x
    except:
        return ingreso_decimal(msg)


# test
# entero = ingreso_entero()
# print(entero, type(entero))

# decimal = ingreso_decimal()
# print(decimal, type(decimal))


