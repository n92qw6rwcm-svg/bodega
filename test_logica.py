'''
tests
'''

import pytest
from logica import agregar_producto, registrar_entrada, registrar_salida, consultar_inventario
from logica import consultar_producto, eliminar_producto


@pytest.fixture(name='inventario_vacio')
def crear_lista_vacia():
    ''' . '''
    return []


@pytest.fixture(name='inventario_test')
def inventario_con_producto():
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


def test_agregar_producto_cantidad_cero(inventario_vacio):
    '''
    test
    '''
    agregar_producto(inventario_vacio, 'lápiz', 0, 5)
    assert len(inventario_vacio) == 1
    assert inventario_vacio[0]["cantidad"] == 0


def test_agregar_producto_stock_minimo_cero(inventario_vacio):
    '''
    test
    '''
    agregar_producto(inventario_vacio, 'carro', 5, 0)
    assert len(inventario_vacio) == 1
    assert inventario_vacio[0]['stock_minimo'] == 0


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


def test_resgistrar_entrada_producto_no_existe(inventario_test):
    '''
    test
    '''
    with pytest.raises(ValueError):
        registrar_entrada(inventario_test, 'arroz', 5)


def test_registrar_entrada_unidades_negativas(inventario_test):
    '''
    test
    '''

    with pytest.raises(ValueError):
        registrar_entrada(inventario_test, 'pan', -1)


def test_registrar_entrada_unidades_cero(inventario_test):
    '''
    test
    '''
    registrar_entrada(inventario_test, 'pan', 0)
    assert inventario_test[0]['cantidad'] == 10


def test_registrar_salida_caso_normal_sin_alerta(inventario_test):
    '''
    test
    '''
    registrar_salida(inventario_test, 'pan', 5)
    assert inventario_test[0]['cantidad'] == 5


def test_registrar_salida_caso_normal_con_alerta(inventario_test):
    '''
    test
    '''
    resultado = registrar_salida(inventario_test, 'pan', 6)
    assert isinstance(resultado, str)
    assert inventario_test[0]['cantidad'] == 4


def test_registrar_salida_unidades_menores_cero(inventario_test):
    '''test'''
    with pytest.raises(ValueError):
        registrar_salida(inventario_test, 'pan', -1)


def test_registrar_salida_unidades_producto_no_existe(inventario_test):
    '''test'''
    with pytest.raises(ValueError):
        registrar_salida(inventario_test, 'postre', 1)


def test_registrar_salida_unidades_superar_cantidad_disponible(inventario_test):
    '''test'''
    with pytest.raises(ValueError):
        registrar_salida(inventario_test, 'pan', 11)


def test_registrar_salida_unidades_cero(inventario_test):
    '''test'''
    registrar_salida(inventario_test, 'pan', 0)
    assert inventario_test[0]['cantidad'] == 10


def test_consultar_inventario_caso_normal(inventario_test):
    '''test'''
    resultado = consultar_inventario(inventario_test)
    assert resultado == inventario_test


def test_consultar_inventario_inventario_vacio(inventario_vacio):
    '''test'''
    resultado = consultar_inventario(inventario_vacio)
    assert resultado == inventario_vacio


def test_consultar_producto_caso_normal(inventario_test):
    '''test'''
    consulta = consultar_producto(inventario_test, 'pan')
    assert consulta == inventario_test[0]


def test_consultar_producto_no_existe(inventario_test):
    '''test'''
    with pytest.raises(ValueError):
        consultar_producto(inventario_test, 'postre')


def test_eliminar_producto_caso_normal(inventario_test):
    '''test'''
    eliminar_producto(inventario_test, 'pan')
    assert len(inventario_test) == 0


def test_eliminar_producto_no_existe(inventario_test):
    '''test'''
    with pytest.raises(ValueError):
        eliminar_producto(inventario_test, 'postre')
