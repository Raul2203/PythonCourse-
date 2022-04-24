# 1. Librerias
import validacion_datos as v # 'v' es un alias para referirme al modulo 'validacion_datos'
# from "nombre_sub_carpeta" import "nombre_archivo" as 'alias'
from funciones_avanzadas import maths_functions as m 
# import 'nombre_sub_carpeta.nombre_script' as 'alias'
import funciones_avanzadas.triangulos as t
# from 'carpeta' import 'scrip1', 'script2'
from funciones_avanzadas import maths_functions, triangulos

# from 'carpeta'.'script' import 'funcion'
from basics.operaciones_basicas import sumar

# 2. Constantes
MSG_BIENVENIDA = "Bienvenido al menú interactivo"
MSG_OPCIONES = """¿Qué quieres hacer? Escribe una opción
        1) Sumar 2 numeros enteros
        2) Calcular el factorial de un numero
        3) Área de la circunferencia
        4) Mostrar un triangulo
        5) Evaluar si un numero es primo
        6) Salir
        """

# 3. Funciones y/o clases

def main():
    
    print(MSG_BIENVENIDA)

    while True:
        
        opcion = input(MSG_OPCIONES) # me devuelve un string ''
        if opcion == '1':
            numero1 = v.ingreso_entero("Ingrese el primero número entero: ")
            numero2 = v.ingreso_entero("Ingrese el segundo número entero: ")
            
            suma = sumar(numero1, numero2)
            print(f'La suma de los numeros es: {suma}')
            
        elif opcion == '2':
            # 1. solicito ingreso de dato
            n = v.ingreso_entero()
            # 2. calculo factorial
            factorial = m.calcular_factorial_recursivo(n)
            # 3. muestro en pantalla resultado
            print(f'El factorial de {n} es {factorial}')
            
        elif opcion == '3':
            radio = v.ingreso_decimal('Ingrese el radio del circulo: ')
            area = m.area_circulo(radio)
            print(f'El área de la circunferencia es: {area}')
            
        elif opcion == '4':
            altura = v.ingreso_entero('Ingrese la altura del triangulo: ')
            triangulos.mostrar_triangulo(altura)
            
        elif opcion == '5':
            pass
        elif opcion =='6':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# 4. Principal
if __name__ == '__main__':
    try:
        main()
    finally:
        print('Programa Finalizado')