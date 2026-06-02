'''
tests
'''

import pytest
from logica import agregar_producto, registrar_entrada, registrar_salida


@pytest.fixture(name='inventario_vacio')
def crear_lista_vacia():
    ''' . '''
    return []


@pytest.fixture(name='inventario_test')
def inventario_con():
    ''' . '''
    return [
        {'nombre': 'pan',
         'cantidad': 10,
         'stock_minimo': 5}
    ]


def test_agregar_producto_caso_normal(inventario_vacio):
    '''
    test
    '''
    agregar_producto(inventario_vacio, "arroz", 10, 5)
    assert len(inventario_vacio) == 1
    assert inventario_vacio[0]["nombre"] == "arroz"


def test_agregar_producto_nombre_vacio(inventario_vacio):
    '''
    test
    '''
    with pytest.raises(ValueError):
        agregar_producto(inventario_vacio, '', 10, 5)


def test_agregar_producto_nombre_repetido(inventario_test):
    '''
    test
    '''
    with pytest.raises(ValueError):
        agregar_producto(inventario_test, 'pan', 3, 1)
    assert len(inventario_test) == 1


def test_agregar_producto_cantidad_negativa(inventario_test):
    '''
    test
    '''
    with pytest.raises(ValueError):
        agregar_producto(inventario_test, 'mango', -1, 1)


def test_agregar_producto_stock_minimo_negativo(inventario_test):
    '''
    test
    '''
    with pytest.raises(ValueError):
        agregar_producto(inventario_test, 'mango', 3, -1)


def test_registrar_entrada_caso_normal(inventario_test):
    '''
    Verificar que cuando el producto extiste y las unidades son válidas,
    la cantidad se actualiza correctamente
    Recibe un inventario con al menos un producto, 
    un nombre que existe en él y un número positivo de unidades a agregar o cero
    Verifica que la cnatidad del producto en el inventario aumente exactamente 
    en el valor de unidades a agregar
    '''

    registrar_entrada(inventario_test, 'pan', 5)
    assert inventario_test[0]['cantidad'] == 15


def test_resgistar_entrada_producto_no_existe(inventario_test):
    '''
    test
    '''
    with pytest.raises(ValueError):
        registrar_entrada(inventario_test, 'arroz', 5)


def test_registar_entrada_unidades_negativas(inventario_vacio):
    '''
    Qué hace -> verificar si registrar entrada lanza ValueError si las unidades a agregar son menores a cero
    Qué recibe -> recibe una lista vacía, nombre y unidades a agregar negativas
    Qué verifica -> Que se lance un ValueError si las unidades a agregar son menores a cero
    '''

    with pytest.raises(ValueError):
        registrar_entrada(inventario_vacio, 'harina', -1)


def test_registar_entrada_unidades_cero(inventario_test):
    '''
    test
    '''
    registrar_entrada(inventario_test, 'pan', 0)
    assert inventario_test[0]['cantidad'] == 10


# def test_registrar_salida_caso_normal():
