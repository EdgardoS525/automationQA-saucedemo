import pytest

from Calculadora import suma,resta,multiplicacion,division

@pytest.fixture
def numeros():
    return 10,5

@pytest.mark.operador # Decorador de etiquetas, se usa con el archivo pytest.ini 
def test_suma(numeros):
    a, b = numeros
    resultado = suma(a,b)

    assert resultado == 15

@pytest.mark.parametrize("a,b,esperado", [ # Decorador para realiza varias pruebas con distintos valores
    (2,3,-1),
    (10,5,5),
    (-2,2,-4)
])
@pytest.mark.operador
def test_resta(a,b,esperado):
    resultado = resta(a,b)

    assert resultado == esperado

@pytest.mark.operador
def test_multiplicacion(numeros):
    a, b = numeros
    resultado = multiplicacion(a,b)

    assert resultado == 50

@pytest.mark.operador
def test_division(numeros):
    a, b = numeros
    resultado = division(a,b)

    assert resultado == 2

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(10,0)