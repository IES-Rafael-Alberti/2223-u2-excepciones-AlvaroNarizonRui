from src.ejercicio4 import comprobarNumero
import pytest

def test_comprobar_numero_valido():
    resultado = comprobarNumero(42)
    assert resultado == 42


def test_comprobar_numero_cadena_error():
    with pytest.raises(ValueError):
        comprobarNumero("no_es_un_numero")


if __name__ == "__main__":
    pytest.main()