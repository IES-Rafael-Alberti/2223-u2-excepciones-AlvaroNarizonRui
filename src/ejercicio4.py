"""Ejercicio 2.3.4¶
Escribir un programa que pida al usuario un 
número entero, si la entrada no es correcta, 
mostrará el mensaje "La entrada no es correcta" 
y lanzará la excepción capturada."""

def comprobarNumero(numero):
    if numero != int(numero):
        return ValueError
    else:
        return numero

if __name__ == "__main__":
    try:
        #Entrada
        numero = int(input("Escribe un numero entero : "))
        #Procesamiento
        comprobacion = comprobarNumero(numero)
        #Salida
        print(f"Entrada correcta")
    except ValueError:
        print("La entrada no es correcta")