'''
tests
'''

import pytest
from logica import agregar_producto


def test_agregar_producto_caso_normal():
    inventario = []
    agregar_producto(inventario, "arroz", 10, 5)
    assert len(inventario) == 1
    assert inventario[0]["nombre"] == "arroz"


def test_agregar_producto_nombre_vacio():
    inventario = []
    with pytest.raises(ValueError):
        agregar_producto(inventario, '', 10, 5)


def test_agregar_producto_nombre_repetido():
    inventario = [{'nombre': 'coco', 'cantidad': 4, 'stock_minimo': 2}]
    with pytest.raises(ValueError):
        agregar_producto(inventario, 'coco', 3, 1)
    assert len(inventario) == 1


def test_agregar_producto_cantidad_negativa():
    inventario = [{'nombre': 'coco', 'cantidad': 4, 'stock_minimo': 2}]
    with pytest.raises(ValueError):
        agregar_producto(inventario, 'mango', -1, 1)


def test_agregar_producto_stock_minimo_negativo():
    inventario = [{'nombre': 'coco', 'cantidad': 4, 'stock_minimo': 2}]
    with pytest.raises(ValueError):
        agregar_producto(inventario, 'mango', 3, -1)


# consultar si hacer los test debe agregarse en un commit. De hecho está sesión se trato de eso. Lo único que se agrego fue este archivo test_logica.py y se aqgregaron 5 test y en lógica, se agregó una condición en la función de agregar. Dicha función surge de un error que se encontró al diseñar un test. La documentación sugería una validación, pero la implementación no la reflejaba.
