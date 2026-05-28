'''
Lógica del programa
'''


def agregar_producto(inventario, nombre, cantidad, stock_minimo):
    '''
    Agrega un producto nuevo al inventario.

    Args:
        inventario (list): inventario del sistema
        nombre (str): nombre del producto. No puede estar vacío ni repetido.
        cantidad (int): cantidad inicial del disponible. Debe ser mayor o igual a cero.
        stock_minimo(int): umbral mínimo para alertas. Debe ser mayor o igual a cero.

    Returns:
        None

    Raises: 
        ValueError: Si el nombre coincide con alguno en la lista.
        ValueError: Si la cantidad o el stock_minimo son menores a cero. 
    '''

    if any(producto['nombre'] == nombre for producto in inventario):
        raise ValueError("Error: Producto existente")

    if cantidad < 0 or stock_minimo < 0:
        raise ValueError("Error: No se permiten valores negativos")

    inventario.append(
        {'nombre': nombre, 'cantidad': cantidad, 'stock_minimo': stock_minimo})


def registrar_entrada(inventario, nombre, unidades_a_agregar):
    '''
    Registra la entrada de -unidades de- producto.

    Args: 
        inventario(list): inventario del sistema.
        nombre(str): nombre del producto. No puede estar vacío.
        unidades_a_agregar(int): valor que representa las unidades de producto a agregar. Debe ser mayor o igual a cero.

    Returns:
        None

    Raises: 
        ValueError: Si el producto no existe en el inventario.
        ValueError: Si las unidades a agregar son menores a cero.
    '''
    if unidades_a_agregar < 0:
        raise ValueError('Error: Valor no permitido')

    if not any(producto['nombre'] == nombre for producto in inventario):
        raise ValueError('Error: Producto no existe')

    for producto in inventario:
        if nombre == producto['nombre']:
            producto['cantidad'] = producto['cantidad'] + unidades_a_agregar


def registrar_salida(inventario, nombre, unidades_a_despachar):
    '''
    Registra la salida de -unidades de- producto.

    Args: 
        inventario(list): inventario del sistema.
        nombre(str): nombre del producto. No puede estar vacío.
        unidades_a_despachar(int): valor que representa las unidades de producto a despachar. No debe ser menor a cero.

    Returns:
        str: Mensaje de advertencia si la cantidad queda por debajo del stock mínimo.
        None: Si la operación se completa sin alertas.

    Raises: 
        ValueError: Si las unidades a despachar son menores a cero.
        ValueError: Si el producto no existe en el inventario.
        ValueError: Si las unidades a despachar superan la cantidad disponible en el inventario.
    '''
    if unidades_a_despachar < 0:
        raise ValueError('Error: No se permiten negativos')

    if not any(producto['nombre'] == nombre for producto in inventario):
        raise ValueError('Error: Producto no existe')

    for producto in inventario:
        if nombre == producto['nombre']:
            if producto['cantidad'] - unidades_a_despachar < 0:
                raise ValueError(
                    'Error: La cantidad solicitada supera la cantidad disponible')

            producto['cantidad'] = producto['cantidad'] - unidades_a_despachar

            if producto['cantidad'] <= producto['stock_minimo']:
                return f'Disclaimer: Cantidad del producto {nombre} por debajo del mínimo'


def consultar_inventario(inventario):
    '''
    Consulta todo el inventario de la bodega.

    Args: 
        inventario(list): inventario del sistema.

    Returns:
        list: inventario
    '''
    return inventario


def consultar_producto(inventario, nombre):
    '''
    Consulta un producto específico en el inventario.

    Args: 
        inventario(list): inventario del sistema.
        nombre(str): nombre del producto. No puede estar vacío.

    Returns:
        dict: producto que coincide con el nombre buscado  

    Raises: 
        ValueError: Si el producto no existe en el inventario.
    '''
    if not any(producto['nombre'] == nombre for producto in inventario):
        raise ValueError('Error: Producto no existe')

    for producto in inventario:
        if nombre == producto['nombre']:
            return producto


def eliminar_producto(inventario, nombre):
    '''
    Elimina producto específico en el inventario.

    Args: 
        inventario(list): inventario del sistema.
        nombre(str): nombre del producto. No puede estar vacío.

    Returns:
        None
        # consultar sobre qué es y cómo funciona lo de las listas con las funciones. He leído sobre en lugar y no lugar. Debe haber alguna relación. 

    Raises:
        ValueError: si el producto no existe en el inventario.
    '''

    if not any(producto['nombre'] == nombre for producto in inventario):
        raise ValueError('Error: Producto no existe')

    for producto in inventario:
        if nombre == producto['nombre']:
            inventario.remove(producto)
