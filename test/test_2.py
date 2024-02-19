from src.ejercicio2 import numerosImpares
import pytest

def test_numeros_impares_5():
    resultado = numerosImpares(5)
    assert resultado == "1,3,5,"

def test_numeros_impares_10():
    resultado = numerosImpares(10)
    assert resultado == "1,3,5,7,9,"

def test_numeros_impares_1():
    resultado = numerosImpares(1)
    assert resultado == "1,"

def test_numeros_impares_0_error():
    with pytest.raises(ValueError):
        numerosImpares(0)

def test_numeros_impares_negativo_error():
    with pytest.raises(ValueError):
        numerosImpares(-5)

if __name__ == "__main__":
    pytest.main()