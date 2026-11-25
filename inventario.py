"""Lógica del inventario: funciones puras (sin input/print) para poder probarlas."""


def buscar_producto(inventario, nombre):
    """Devuelve el producto cuyo nombre coincide (sin distinguir mayúsculas) o None."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.strip().lower():
            return producto
    return None


def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto validando los datos. Lanza ValueError si son inválidos."""
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    if buscar_producto(inventario, nombre):
        raise ValueError(f"Ya existe un producto llamado '{nombre}'.")
    producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
    inventario.append(producto)
    return producto


def actualizar_cantidad(inventario, nombre, nueva_cantidad):
    """Cambia la cantidad de un producto. Devuelve True si existía."""
    if nueva_cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        return False
    producto["cantidad"] = int(nueva_cantidad)
    return True


def eliminar_producto(inventario, nombre):
    """Elimina un producto por nombre. Devuelve True si existía."""
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        return False
    inventario.remove(producto)
    return True


def calcular_valor_total(inventario):
    """Suma precio x cantidad de todos los productos."""
    return sum(p["precio"] * p["cantidad"] for p in inventario)


def formatear_inventario(inventario):
    """Devuelve el texto del listado de productos."""
    if not inventario:
        return "El inventario está vacío."
    lineas = ["--- Inventario de productos ---"]
    for i, p in enumerate(inventario, 1):
        lineas.append(f"{i}. {p['nombre']}")
        lineas.append(f"   Precio: ${p['precio']:.2f}")
        lineas.append(f"   Cantidad: {p['cantidad']} unidades")
    return "\n".join(lineas)