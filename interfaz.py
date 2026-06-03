'''
Módulo de interfaz. Responsable de la interacción con el usuario: 
mostrar información y recibir datos.
'''


def mostrar_menu():
    '''
    Muestra las opciones del menú
    '''
    print('''
          Bienvenido al programa
          1. Agregar producto
          2. Registrar entrada
          3. Registrar salida
          4. consultar inventario
          5. Consultar producto
          6. Eliminar producto
          7. Salir
          ''')


def pedir_eleccion():
    '''
    Solicita elección al usuario

    Returns:
        int: número correspondiente a la elección del usuario

   '''
    while True:
        try:
            eleccion = int(input('Digite su elección:\n').strip())

            if eleccion not in range(1, 8):
                raise ValueError('Opción no disponible')

        except ValueError as e:
            if 'invalid literal' in str(e):
                mostrar_error('Error: Solo se aceptan las opciones del menú')
            else:
                mostrar_error(f'Error: {e}')

        else:
            return eleccion


def pedir_nombre():
    '''
    solicita nombre al usuario.

    Returns:
        str: entrada de usuario si solo contiene caracteres alfabéticos
    '''
    while True:

        nombre = input('Ingresar nombre del producto:\n').strip()

        if not nombre.replace(' ', '').isalpha():
            mostrar_error('Solo se permiten letras')
        else:
            return nombre


def pedir_cantidad():
    '''
    solicita la cantidad al usuario

    Returns: 
        int: valor 'cantidad' ingresada. Si es mayor o igual a cero.  

    '''
    while True:
        try:
            cantidad = int(input('Ingresar cantidad del producto:\n'))

            if cantidad < 0:
                raise ValueError('No se aceptan valores negativos')

        except ValueError as e:
            if 'invalid literal' in str(e):
                mostrar_error('Error: Solo se aceptan números enteros')
            else:
                mostrar_error(f'Error: {e}')

        else:
            return cantidad


def pedir_stock_minimo():
    '''
    Solicita el stock mínimo al usuario

    Returns:
        int: cantidad mínima de stock. Si es mayor o igual a cero.
    '''

    while True:
        try:
            stock_minimo = int(
                input('Ingrese el stock mínimo para el producto:\n'))

            if stock_minimo < 0:
                raise ValueError('No se aceptan valores negativos')

        except ValueError as e:
            if 'invalid literal' in str(e):
                mostrar_error('Error: Solo se aceptan números enteros')
            else:
                mostrar_error(f'Error: {e}')

        else:
            return stock_minimo


def pedir_unidades_agregar():
    '''
    Solicita al usuario las unidades a agregar

    Returns: 
        int: unidades a agregar si son mayores o iguales a cero
    '''
    while True:
        try:
            unidades_agregar = int(
                input('Ingresar el número de unidades que se agregarán:\n'))

            if unidades_agregar < 0:
                raise ValueError('No se aceptan valores negativos')

        except ValueError as e:
            if 'invalid literal' in str(e):
                mostrar_error('Error: Solo se aceptan números enteros')
            else:
                mostrar_error(f'Error: {e}')

        else:
            return unidades_agregar


def pedir_unidades_retirar():
    '''
    Solicita al usuario las unidades a retirar

    Returns: 
        int: unidades a retirar si son mayores o iguales a cero
    '''

    while True:
        try:
            unidades_retirar = int(
                input('Ingresar el número de unidades que se retirarán:\n'))

            if unidades_retirar < 0:
                raise ValueError('No se aceptan valores negativos')

        except ValueError as e:
            if 'invalid literal' in str(e):
                mostrar_error('Error: Solo se aceptan números enteros')
            else:
                mostrar_error(f'Error: {e}')

        else:
            return unidades_retirar


def mostrar_producto(producto):
    '''
    Imprime -en consola- el producto

    Args:
        producto(dict): producto con campos 'nombre'(str), 'cantidad'(int), 'stock_minimo'(int)
    '''
    print(f'Nombre: {producto['nombre']}')
    print(f'Cantidad: {producto['cantidad']}')
    print(f'Stock mínimo: {producto['stock_minimo']}')


def mostrar_inventario(inventario):
    '''
    Imprime -en consola- el inventario

    Args:
        inventario(list): inventario del sistema
    '''
    for producto in inventario:
        mostrar_separador(producto['nombre'])
        mostrar_producto(producto)


def mostrar_separador(nombre):
    '''
    muestra el separador: --- nombre ---

    Args:
        nombre(str): nombre del producto
    '''
    print(f' --- {nombre} --- ')


def mostrar_error(mensaje):
    '''
    Imprime -en consola- los mensajes de error

    Args:
        mensaje(str): mensaje de error.
    '''
    print(mensaje)


def mostrar_alerta(mensaje):
    '''
    Imprime -en consola- las alertas concernientes a los productos

    Args:
        mensaje(str): mensaje de alerta
    '''
    print(mensaje)


def mostrar_confirmacion(mensaje):
    '''
    Imprime -en consola- mensaje de confirmación

    Args:
        mensaje(str): mensaje de confirmación
    '''
    print(mensaje)


def msn_guardado():
    '''
    Imprime -en consola- mensaje de guardado
    '''
    print('Guardado con éxito')


def msn_eliminacion():
    '''
    Imprime mensaje de eliminación
    '''
    print('Eliminado con éxito')


def msn_agregado_exitoso():
    '''
    Imprime -en consola- mensaje de agregado con éxito
    '''
    print('Producto agregado con éxito.')


def msn_retiro_exitoso():
    '''
    Imprime -en consola- mensaje de retiro con éxito
    '''
    print('Retiro exitoso.')


def msn_finalizar_programa():
    '''
    Imprime mensaje de finalización del programa
    '''
    print('Programa finalizado...')


def continuar():
    '''
    Función estética

    Returns:
        str: entrada del usuario
    '''
    return input('Presione enter para continuar')


if __name__ == '__main__':
    products = [{'nombre': 'coco',
                 'cantidad': 2,
                 'stock_minimo': 1}]
    stock = pedir_stock_minimo()
    print(stock)
