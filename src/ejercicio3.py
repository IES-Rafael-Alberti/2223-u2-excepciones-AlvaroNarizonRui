"""
Ejercicio 2.3.3¶
Escribir un programa que pida al usuario un 
número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero 
separados por comas. Deberá solicitar el 
número hasta introducir uno correcto.
"""
def cuenta_atras(numero):
    if numero <= 0:
        raise ValueError
    contenedor_numeros = ""
    for i in range(numero,-1,-1):
        contenedor_numeros += str(i) + ","
    return contenedor_numeros

if __name__ == "__main__":
    numero = 0
    #Entrada
    while numero <= 0:
        try:
            numero = int(input("Escribe un número entero positivo: "))
        except ValueError:
            print("Entrada inválida. Debes introducir un número positivo entero")
    #Procesamiento
    cuenta = cuenta_atras(numero)
    #Salida
    print(f"El número que introdujiste: {numero} \n Resultado: {cuenta}")

