# Sistema de Gestión de Notas

## Descripción

Este programa permite gestionar el ingreso de notas dinamicas y realizar diversos cálculos estadisticos. Valida que todas las entradas sean correctas (numeros entre 0 y 100), permite calcular el promedio, determinar aprobación según rangos personalizados, comparar valores y buscar frecuencias de notas específicas. Su principal ventaja es la interactividad mediante un menu que permite al usuario realizar múltiples operaciones sin reiniciar el programa.

## Características

- **Manejo robusto de errores**: El programa verifica todas las entradas y proporciona mensajes de error claros
- **Menú interactivo**: Facilita al usuario realizar diferentes operaciones sin reiniciar el programa
- **Validación de datos**: Rechaza valores fuera del rango 0-100 y entradas no numéricas
- **Formato de salida profesional**: Muestra resultados de manera clara y organizada
- **Flexibilidad**: Permite modificar la lista de notas en cualquier momento

## Tareas
- ✅ Verificar que en todo momento los datos ingresados son validos.
- ✅ Pedir al usuario que ingrese en un solo input, una lista de notas (de 0 a 100), separadas por comas.
- ✅ Convertir el input en una lista de numeros, para poder ejecutar las operaciones matematicas.
- ✅ Solicitar y validar la calificación mínima aprobatoria
- ✅ Calcular el promedio de todas las calificaciones y determinar si el usuario aprobó, (en base a la calificacion minima aprobatoria ingresada)
- ✅ Preguntar al usuario por un valor comparativo, y determinar cuantas calificaciones son mayores que este valor.
- ✅ Solicitar una calificación específica a buscar para verificar y contar cuántas veces aparece esa calificación específica
- ✅ Mostrar todos los resultados de manera clara y organizada

## Output esperado

Ejemplo de la ejecución del programa:

```
Bienvenido A Este Programa Para Gestionar El Ingreso De Notas Dinamicas
!!! Por favor ingresa las notas separadas por comas (,): 75, 80, 90, 65, 70

Lista de notas actuales: [75.0, 80.0, 90.0, 65.0, 70.0]
  Qué desea hacer? 
    0: Ingresar una nueva lista de notas
    1: Determinar el estado de aprobación
    2: Calcular promedio
    3: Contar calificaciones mayores
    4: Verificar y contar calificaciones específicas
    5: Salir
2
Ingrese el valor minimo aprobatorio: 70
****************************************
De las notas: [75.0, 80.0, 90.0, 65.0, 70.0]
El promedio es: 76.0
Del valor minimo aprobatorio 70.0: 

    !!!Felicidades aprobaste!!!
****************************************
Desea continuar? (Si/No): si
°°° Continuando... °°°

Lista de notas actuales: [75.0, 80.0, 90.0, 65.0, 70.0]
  Qué desea hacer? 
    0: Ingresar una nueva lista de notas
    1: Determinar el estado de aprobación
    2: Calcular promedio
    3: Contar calificaciones mayores
    4: Verificar y contar calificaciones específicas
    5: Salir
3
Ingrese un valor para comparar que notas son mayores a él: 75
****************************************
De las notas: [75.0, 80.0, 90.0, 65.0, 70.0]
Se encontraron 2 notas mayor(es) 
Las notas mayores a 75.0 son: [80.0, 90.0]
****************************************
Desea continuar? (Si/No): no
°°° Finalizando programa... °°°
```

## Estructura del Código

El programa está organizado en cinco partes principales:

1. **Funciones de menú y control**:
   - `mostrar_menu()`: Presenta opciones al usuario y gestiona la navegación
   - `continuar()`: Permite decidir si continuar o finalizar el programa

2. **Funciones de validación**:
   - `control_numeros()`: Validación de entradas numéricas individuales
   - `control_notas()`: Validación de listas de notas separadas por comas

3. **Funciones de cálculo**:
   - `determinar_aprobacion()`: Evalúa si una nota supera un valor mínimo
   - `calcular_promedio()`: Calcula el promedio de todas las notas
   - `comparar_valor()`: Identifica notas mayores que un valor dado
   - `buscar_frecuencia()`: Cuenta ocurrencias de una nota específica

4. **Programa principal**:
   - Inicialización de variables
   - Bucle principal para mantener el programa en ejecución

5. **Presentación de resultados**:
   - Formato de salida claro con separadores visuales

## Autor
Antonio Carlos Santiago Rodriguez