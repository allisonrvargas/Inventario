import unittest

import inventario as inv


class PruebasInventario(unittest.TestCase):
    def setUp(self):
        self.lista = []
        inv.agregar_producto(self.lista, "Lapiz", 2.5, 10)
        inv.agregar_producto(self.lista, "Cuaderno", 15, 4)

    def test_agregar_guarda_los_datos(self):
        self.assertEqual(len(self.lista), 2)
        self.assertEqual(self.lista[0], {"nombre": "Lapiz", "precio": 2.5, "cantidad": 10})

    def test_agregar_rechaza_datos_invalidos(self):
        with self.assertRaises(ValueError):
            inv.agregar_producto(self.lista, "  ", 1, 1)
        with self.assertRaises(ValueError):
            inv.agregar_producto(self.lista, "Goma", -1, 1)
        with self.assertRaises(ValueError):
            inv.agregar_producto(self.lista, "Goma", 1, -5)

    def test_agregar_rechaza_nombre_repetido_sin_distinguir_mayusculas(self):
        with self.assertRaises(ValueError):
            inv.agregar_producto(self.lista, "lapiz", 3, 1)

    def test_actualizar_cantidad(self):
        self.assertTrue(inv.actualizar_cantidad(self.lista, "LAPIZ", 99))
        self.assertEqual(inv.buscar_producto(self.lista, "lapiz")["cantidad"], 99)
        self.assertFalse(inv.actualizar_cantidad(self.lista, "inexistente", 1))
        with self.assertRaises(ValueError):
            inv.actualizar_cantidad(self.lista, "lapiz", -1)

    def test_eliminar(self):
        self.assertTrue(inv.eliminar_producto(self.lista, "Cuaderno"))
        self.assertFalse(inv.eliminar_producto(self.lista, "Cuaderno"))
        self.assertEqual(len(self.lista), 1)

    def test_valor_total(self):
        self.assertAlmostEqual(inv.calcular_valor_total(self.lista), 2.5 * 10 + 15 * 4)
        self.assertEqual(inv.calcular_valor_total([]), 0)

    def test_listado_muestra_precio_y_cantidad_de_todos_los_productos(self):
        texto = inv.formatear_inventario(self.lista)
        self.assertIn("Precio: $2.50", texto)
        self.assertIn("Precio: $15.00", texto)
        self.assertIn("Cantidad: 4 unidades", texto)
        self.assertEqual(inv.formatear_inventario([]), "El inventario está vacío.")


if __name__ == "__main__":
    unittest.main()