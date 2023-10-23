from src.ejercicio3 import cuenta_atras
import pytest

def test_cuenta_atras_5():
    resultado = cuenta_atras(5)
    assert resultado == "5,4,3,2,1,0,"

def test_cuenta_atras_1():
    resultado = cuenta_atras(1)
    assert resultado == "1,0,"

def test_cuenta_atras_10():
    resultado = cuenta_atras(10)
    assert resultado == "10,9,8,7,6,5,4,3,2,1,0,"

def test_cuenta_atras_0_error():
    with pytest.raises(ValueError):
        cuenta_atras(0)

def test_cuenta_atras_negativo_error():
    with pytest.raises(ValueError):
        cuenta_atras(-5)


if __name__ == "__main__":
    pytest.main()