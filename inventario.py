def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad disponible: "))
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f" {nombre} agregado con éxito.")

def listar_productos(inventario):
    if not inventario:
        print("⚠️ El inventario está vacío.")
        return
    
    print("\n--- Inventario de productos ---")
    for i, p in enumerate(inventario, 1):
        print(f"{i}. {p['nombre']}")
        print(f"   Precio: {p['precio']}")
        print(f"   Cantidad: {p['cantidad']}")

def actualizar_cantidad(inventario):
    nombre = input("Nombre del producto a actualizar: ")
    for p in inventario:
        if p['nombre'].lower() == nombre.lower():
            nueva_cant = int(input("Nueva cantidad: "))
            p['cantidad'] = nueva_cant
            print("✅ Cantidad actualizada.")
            return
    print(" Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    for p in inventario:
        if p['nombre'].lower() == nombre.lower():
            inventario.remove(p)
            print("🗑️ Producto eliminado.")
            return
    print(" No se encontró el producto.")

def calcular_valor_total(inventario):
    total = sum(p['precio'] * p['cantidad'] for p in inventario)
    print(f"\n💰 Valor total del inventario: {total}")