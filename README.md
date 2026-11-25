# Sistema de Gestión de Inventario

[![CI](https://github.com/allisonrvargas/Inventario/actions/workflows/ci.yml/badge.svg)](https://github.com/allisonrvargas/Inventario/actions/workflows/ci.yml)
[![Licencia: MIT](https://img.shields.io/badge/licencia-MIT-green.svg)](LICENSE)

Aplicación de consola en **Python 3** para administrar los productos de una tienda pequeña: registrar productos, listar el inventario, actualizar cantidades, eliminar artículos y calcular el valor total del stock.

![Captura](img/screenshot.png)

## Funciones

| Opción | Qué hace |
| --- | --- |
| 1. Agregar producto | Valida nombre, precio y cantidad; no permite nombres repetidos |
| 2. Listar productos | Muestra nombre, precio y cantidad de **todos** los productos |
| 3. Actualizar cantidad | Busca el producto sin distinguir mayúsculas |
| 4. Eliminar producto | Lo quita del inventario |
| 5. Calcular valor total | Suma precio × cantidad |
| 6. Salir | Termina el programa |

## Ejemplo de sesión

Salida real del programa. Entradas usadas: agregar *Cuaderno* (.50 x 10), agregar *Lapiz* (.25 x 40), listar, cambiar la cantidad de *cuaderno* a 7, calcular el valor total y salir (las respuestas no se ven porque se leyeron de un archivo, no del teclado).

```text
--- SISTEMA DE INVENTARIO ---
1. Agregar producto
2. Listar productos
3. Actualizar cantidad
4. Eliminar producto
5. Calcular valor total
6. Salir
Seleccione una opción: Nombre del producto: Precio: Cantidad disponible: Cuaderno agregado con éxito.

[ ...se muestra el menú... ]
Seleccione una opción: Nombre del producto: Precio: Cantidad disponible: Lapiz agregado con éxito.

[ ...se muestra el menú... ]
Seleccione una opción: 
--- Inventario de productos ---
1. Cuaderno
   Precio: $15.50
   Cantidad: 10 unidades
2. Lapiz
   Precio: $2.25
   Cantidad: 40 unidades

[ ...se muestra el menú... ]
Seleccione una opción: Nombre del producto a actualizar: Nueva cantidad: Cantidad actualizada.

[ ...se muestra el menú... ]
Seleccione una opción: 
Valor total del inventario: $198.50

[ ...se muestra el menú... ]
Seleccione una opción: ¡Gracias por usar el sistema de inventario! Saliendo...
```

## Cómo ejecutarlo

Requiere Python 3.9 o superior; no usa librerías externas.

```bash
python main.py
```

## Pruebas

```bash
python -m unittest discover -s tests -t . -v
```

## Estructura

```text
main.py                 menú de consola (entrada y salida)
inventario.py           lógica del inventario (funciones puras y probadas)
tests/test_inventario.py  pruebas unitarias
```

La lógica está separada del menú para poder probarla sin escribir nada por consola.

## Historial de cambios

Se corrigieron fallos de la primera versión: `main.py` tenía un error de sintaxis y no se podía ejecutar, y el listado mostraba el precio y la cantidad solo del último producto.

## Autor

Allison Rocío Vargas Mejía ([@allisonrvargas](https://github.com/allisonrvargas)) · Campuslands

## Licencia

MIT