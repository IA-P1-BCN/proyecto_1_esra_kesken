from taximetro import calcular_importe


def test_calcular_importe_parado():
    resultado = calcular_importe("parado", 10)
    assert resultado == 0.20


def test_calcular_importe_movimiento():
    resultado = calcular_importe("movimiento", 10)
    assert resultado == 0.50
