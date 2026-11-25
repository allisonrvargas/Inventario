import inventario as inv


def mostrar_menu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Calcular valor total")
    print("6. Salir")


def pedir_numero(mensaje, tipo):
    """Pide un número por consola; repite hasta que sea válido."""
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print("Valor no válido, intenta de nuevo.")


def agregar():
    nombre = input("Nombre del producto: ")
    precio = pedir_numero("Precio: ", float)
    cantidad = pedir_numero("Cantidad disponible: ", int)
    try:
        producto = inv.agregar_producto(lista_productos, nombre, precio, cantidad)
        print(f"{producto['nombre']} agregado con éxito.")
    except ValueError as error:
        print(f"No se pudo agregar: {error}")


def actualizar():
    nombre = input("Nombre del producto a actualizar: ")
    nueva = pedir_numero("Nueva cantidad: ", int)
    try:
        if inv.actualizar_cantidad(lista_productos, nombre, nueva):
            print("Cantidad actualizada.")
        else:
            print("Producto no encontrado.")
    except ValueError as error:
        print(f"No se pudo actualizar: {error}")


def eliminar():
    nombre = input("Nombre del producto a eliminar: ")
    print("Producto eliminado." if inv.eliminar_producto(lista_productos, nombre) else "No se encontró el producto.")


lista_productos = []


def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar()
        elif opcion == "2":
            print("\n" + inv.formatear_inventario(lista_productos))
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            print(f"\nValor total del inventario: ${inv.calcular_valor_total(lista_productos):,.2f}")
        elif opcion == "6":
            print("¡Gracias por usar el sistema de inventario! Saliendo...")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 6.")


if __name__ == "__main__":
    ejecutar()