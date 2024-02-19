from src.ejercicio1 import añosVida
import pytest

def test_años_vida_valido():
    resultado = añosVida(5)
    assert resultado == "1\n2\n3\n4\n5\n"

def test_años_vida_error_0():
    with pytest.raises(ValueError):
        añosVida(0)

def test_años_vida_error_negativo():
    with pytest.raises(ValueError):
        añosVida(-5)



if __name__ == "__main__":
    pytest.main()