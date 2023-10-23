"""Ejercicio 2.3.1¶
Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

def añosVida(edad):
    if edad <= 0:
        raise ValueError
    else:
        contenedor_años = ""
        for i in range(1,edad+1,1):
            contenedor_años += str(i) + "\n"
        return contenedor_años


if __name__ == "__main__":
    try:
        #Entrada
        edad = int(input("Escribe tu edad actual : "))
        #Procesamiento
        cumpleaños = añosVida(edad)
        #Salida
        print(f"Tu edad actual: {edad} \n Todos los cumpleaños que has tenido: {cumpleaños}")
    except ValueError:
        print("|Error Numérico| No se puede tener edad negativa, 0 o con decimales")