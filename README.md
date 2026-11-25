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