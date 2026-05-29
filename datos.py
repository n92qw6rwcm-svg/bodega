'''
Contiene las funciones encargadas de la gestión del inventario:
cargar y guardar
'''
import os
import json


def cargar_inventario():
    '''
    Carga y retorna datos desde el disco.

    Returns:
        list: Inventario cargado desde el archivo. 

    Raises:
        ValueError: El archivo no existe o no puede leerse.
    '''
    ruta = os.path.join('data', 'inventario.json')

    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = json.load(file)

    except FileNotFoundError as e:
        raise ValueError('El archivo o carpeta no existe') from e

    except json.JSONDecodeError as e:
        raise ValueError('No se puede leer el archivo') from e

    return contenido


def guardar_inventario(inventario):
    '''
    Escribe (guarda) el inventario en el disco duro.

    Args: 
        inventario(list): inventario del sistema

    Returns: 
        None

    Raises:
        OSError: Si el archivo no se puede escribir en el disco

    '''
    # se construye una ruta dinámica para que siempre apunte a la carpeta data
    ruta = os.path.join('data', 'inventario.json')
    try:
        with open(ruta, 'w', encoding='utf-8') as file:
            json.dump(inventario, file, ensure_ascii=False, indent=4)

    except OSError as e:
        raise OSError(f'Error al guardar: {e}') from e


if __name__ == '__main__':
    print(cargar_inventario())
    productos = [{'nombre': 'zapato', 'cantidad': 28}]
    guardar_inventario(productos)
