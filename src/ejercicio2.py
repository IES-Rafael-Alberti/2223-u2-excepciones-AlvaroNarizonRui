"""
Ejercicio 2.3.2¶
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""
def numerosImpares(numero):
    if numero <= 0:
        raise ValueError
    else:
        contenedor_numeros = ""
        for i in range(1,numero+1,1):
            if i % 2 != 0:
                contenedor_numeros += str(i) + ","
        return contenedor_numeros

if __name__ == "__main__":
    try:
        #Entrada
        numero = int(input("Escribe un numero : "))
        #Procesamiento
        impares = numerosImpares(numero)
        #Salida
        print(f"El número que introdujiste: {numero} \n Resultado: {impares}")
    except ValueError:
        print("No se puede introducir un número igual o menor que 0")
