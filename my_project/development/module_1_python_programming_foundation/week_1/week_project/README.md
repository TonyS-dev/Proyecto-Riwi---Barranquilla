# Sistema de Gestión de Compras

## Descripción

Este programa permite registrar múltiples productos con su nombre, precio y cantidad. Valida que todas las entradas sean correctas (números positivos), calcula el subtotal para cada producto (precio × cantidad), permite aplicar un descuento al total de la compra y genera un resumen detallado. Su principal ventaja es que maneja varios productos diferentes en una sola ejecución.

## Características

- **Manejo robusto de errores**: El programa verifica todas las entradas y proporciona mensajes de error claros
- **Interfaz de usuario amigable**: Guía al usuario en cada paso con instrucciones claras
- **Validación de datos**: Rechaza valores negativos y entradas no numéricas
- **Formato de salida profesional**: Muestra un resumen detallado y bien organizado

## Output esperado

Ejemplo de la ejecución del programa:

```
!!! Por favor ingresa la cantidad de tipos de productos: 2
/// Cantidad de tipos de productos correctamente ingresada. ///
!!! Por favor ingresa el nombre del producto 1: Papa
!!! Por favor ingresa el precio unitario del producto 1: 2500
!!! Por favor ingresa la cantidad del producto 1: 10
/// Producto correctamente ingresado. ///
!!! Por favor ingresa el nombre del producto 2: Manzana
!!! Por favor ingresa el precio unitario del producto 2: 3000
!!! Por favor ingresa la cantidad del producto 2: 8 
/// Producto correctamente ingresado. ///
/// Productos ingresados correctamente ///
--- Existe algun descuento? (si/no): si
°°° Continuando... °°°
°°° Procediendo con descuentos... ingresa el descuento (0-100): 25
==>> Descuento correctamente asignado.

------------- ORDEN DETALLES -------------
Tipos de productos: #2

----------- LISTA DE PRODUCTOS -----------
Papa: $2500.00 x 10 = $25000.00
Manzana: $3000.00 x 8 = $24000.00
------------------------------------------
Precio sub-total: $49000.00
Descuento seleccionado: 25%
Descuento aplicado: $12250.00
Precio total: $36750.00
------------------------------------------
```

## Estructura del Código

El programa está organizado en tres partes principales:

1. **Funciones de validación**:
   - `handle_number_inputs()`: Validación de entradas numéricas
   - `handle_discounts()`: Gestión de la aplicación de descuentos

2. **Programa principal**:
   - Recopilación de información de productos
   - Cálculo de subtotales y totales

3. **Presentación de resultados**:
   - Generación de resumen detallado


## Autor
Antonio Carlos Santiago Rodriguez