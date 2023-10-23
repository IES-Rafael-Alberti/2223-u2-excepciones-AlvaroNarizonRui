from src.ejercicio5 import comprobarContraseña
import pytest

def testcontraseña():
    assert comprobarContraseña("trollface123","trollface123") == "trollface123"

def testcontraseñaexcepcion():
    with pytest.raises(NameError):
        comprobarContraseña("trollface123","troll")

if __name__ == "__main__":
    pytest.main()
