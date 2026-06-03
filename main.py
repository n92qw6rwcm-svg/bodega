'''
Módulo principal. Punto de entrada del programa. 
Coordina el flujo de ejecución entre lógica, interfaz y persistencia.
'''
import sys
from datos import cargar_inventario, guardar_inventario
import logica
import interfaz


try:
    bodega = cargar_inventario()

except ValueError as e:
    interfaz.mostrar_error(e)
    sys.exit()

while True:

    interfaz.mostrar_menu()

    eleccion = interfaz.pedir_eleccion()

    if eleccion == 1:

        try:
            nombre_producto = interfaz.pedir_nombre()
            cantidad_producto = interfaz.pedir_cantidad()
            stock_minimo_producto = interfaz.pedir_stock_minimo()
            logica.agregar_producto(bodega,
                                    nombre_producto,
                                    cantidad_producto, stock_minimo_producto)

        except ValueError as e:
            interfaz.mostrar_error(e)

        else:
            guardar_inventario(bodega)
            interfaz.msn_guardado()

        finally:
            interfaz.continuar()

    if eleccion == 2:

        try:
            nombre_producto = interfaz.pedir_nombre()
            unidad_producto = interfaz.pedir_unidades_agregar()

            logica.registrar_entrada(bodega,
                                     nombre_producto,
                                     unidad_producto)

        except ValueError as e:
            interfaz.mostrar_error(e)

        else:
            guardar_inventario(bodega)

            interfaz.msn_agregado_exitoso()

        finally:
            interfaz.continuar()

    if eleccion == 3:

        try:
            nombre_producto = interfaz.pedir_nombre()
            unidad_producto = interfaz.pedir_unidades_retirar()

            alerta = logica.registrar_salida(bodega,
                                             nombre_producto,
                                             unidad_producto)

        except ValueError as e:
            interfaz.mostrar_error(e)

        else:
            guardar_inventario(bodega)
            if alerta:
                interfaz.msn_retiro_exitoso()
                interfaz.mostrar_alerta(alerta)
            else:
                interfaz.msn_retiro_exitoso()

        finally:
            interfaz.continuar()

    if eleccion == 4:

        mostrar_inventario = logica.consultar_inventario(bodega)
        interfaz.mostrar_inventario(mostrar_inventario)

        interfaz.continuar()

    if eleccion == 5:

        try:
            nombre_producto = interfaz.pedir_nombre()
            mostrar_producto = logica.consultar_producto(bodega,
                                                         nombre_producto)
            interfaz.mostrar_producto(mostrar_producto)

        except ValueError as e:
            interfaz.mostrar_error(e)

        finally:
            interfaz.continuar()

    if eleccion == 6:

        try:
            nombre_producto = interfaz.pedir_nombre()
            logica.eliminar_producto(bodega, nombre_producto)

        except ValueError as e:
            interfaz.mostrar_error(e)

        else:
            guardar_inventario(bodega)
            interfaz.msn_eliminacion()

        finally:
            interfaz.continuar()

    if eleccion == 7:
        interfaz.msn_finalizar_programa()
        break
