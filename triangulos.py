

def mostrar_triangulo(altura:int):
    """Muestra un triangulo de # en pantalla"""
    for i in range(1, altura+1):
        print('#'*i)
        
        
        
if __name__ == "__main__":
    mostrar_triangulo(5)