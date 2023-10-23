from src.ejercicio5 import comprobarContraseña
import pytest

def test_contraseña_correcta():
    contraseña = "trollface123"
    entrada = "trollface123"
    assert comprobarContraseña(contraseña,entrada) == entrada

def test_contraseña_incorrecta():
    contraseña = "trollface123"
    entrada = "contraseñaincorrecta"
    with pytest.raises(NameError):
        comprobarContraseña(contraseña,entrada)
if __name__ == "__main__":
    pytest.main()
