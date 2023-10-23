"""
Ejercicio 2.3.5¶
Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""
def comprobarContraseña(contraseña,entrada):
    if contraseña.lower() == entrada.lower():
        return entrada
    else:
        raise NameError
    
if __name__ == "__main__":
    try:
        #Entrada
        contraseña = "trollface123"
        entrada = input("Escribe la contraseña : ")
        #Procesamiento
        comprobarContraseña(contraseña,entrada)
        #Salida
        print("Entraste")
    except NameError:
        print("Incorrect Password!!")
    