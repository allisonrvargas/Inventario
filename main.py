import inventario as inv

def mostrar_menu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Calcular valor total")
    print("6. Salir")

def ejecutar():
    lista_productos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            inv.agregar_producto(lista_productos)
        elif opcion == "2":
            inv.listar_productos(lista_productos)
        elif opcion == "3":
            inv.actualizar_cantidad(lista_productos)
        elif opcion == "4":
            inv.eliminar_producto(lista_productos)
        elif opcion == "5":
            inv.calcular_valor_total(lista_productos)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar()