# Día 02 — Entrada, salida y conversión de datos

## Objetivo

Comprender cómo recibir información del usuario, convertir los datos al tipo correcto, realizar operaciones y mostrar resultados formateados en pantalla.

En esta práctica reforzaremos el flujo fundamental de un programa:

```text
Entrada → Procesamiento → Salida
```

---

## Conceptos del día

* Entrada de datos con `input()`
* Salida de datos con `print()`
* Conversión de datos con `int()` y `float()`
* Operaciones aritméticas
* Uso de variables descriptivas
* Uso de `f-strings`
* Formateo de números decimales

---

## 1. Entrada de datos

La entrada representa la información que el programa recibe del usuario.

Para solicitar información usamos la función:

```python
input()
```

Ejemplo:

```python
producto = input("Ingrese el nombre del producto: ")
```

El dato ingresado se guarda en la variable `producto`.

### Importante

Todo valor recibido mediante `input()` se almacena inicialmente como texto, es decir, como un dato de tipo:

```python
str
```

Incluso cuando el usuario escribe un número.

---

## 2. Conversión de datos

Cuando necesitamos realizar operaciones matemáticas, debemos convertir el texto recibido al tipo numérico adecuado.

### Conversión a número entero

Usamos `int()` cuando el dato no necesita decimales.

```python
cantidad = int(input("Ingrese la cantidad: "))
```

Ejemplos de números enteros:

```text
1
5
20
100
```

### Conversión a número decimal

Usamos `float()` cuando el dato puede contener decimales.

```python
precio_unitario = float(input("Ingrese el precio unitario: "))
```

Ejemplos de números decimales:

```text
10.50
25.90
80.75
```

En Python, los números decimales se escriben utilizando punto y no coma.

Correcto:

```text
15.50
```

Incorrecto:

```text
15,50
```

---

## 3. Procesamiento de datos

El procesamiento consiste en utilizar los datos ingresados para generar nueva información.

En esta práctica calcularemos el costo de una compra.

### Cálculo del subtotal

```python
subtotal = precio_unitario * cantidad
```

La operación representa:

```text
Precio unitario × Cantidad = Subtotal
```

### Cálculo del IGV

En Perú, el IGV utilizado en esta práctica será del 18 %.

```python
igv = subtotal * 0.18
```

### Cálculo del total

```python
total = subtotal + igv
```

El flujo completo será:

```text
Subtotal = precio unitario × cantidad
IGV = subtotal × 18 %
Total = subtotal + IGV
```

---

## 4. Salida de datos

La salida representa la información que el programa muestra al usuario.

Para mostrar información utilizamos:

```python
print()
```

Ejemplo:

```python
print(f"Producto: {producto}")
```

La letra `f` permite insertar variables dentro de un texto utilizando llaves:

```python
{variable}
```

---

## 5. Formateo de decimales

Los precios normalmente deben mostrarse con dos cifras decimales.

Para ello utilizamos:

```python
{variable:.2f}
```

Ejemplo:

```python
print(f"Total: S/ {total:.2f}")
```

Si el valor de `total` fuera:

```text
284.969999
```

El resultado mostrado sería:

```text
S/ 284.97
```

El formato `.2f` significa:

* `f`: número decimal.
* `.2`: mostrar dos cifras después del punto decimal.

---

## Ejercicio principal

Crear un programa que solicite:

* Nombre del producto
* Precio unitario
* Cantidad comprada

Después deberá calcular:

* Subtotal
* IGV del 18 %
* Total de la compra

Finalmente, deberá mostrar todos los resultados utilizando `f-strings` y dos decimales para los importes.

---

## Ejemplo de ejecución

```text
Ingrese el producto: Aceite hidráulico
Ingrese el precio unitario: 80.50
Ingrese la cantidad: 3

Producto: Aceite hidráulico
Subtotal: S/ 241.50
IGV: S/ 43.47
Total: S/ 284.97
```

---

## Reglas del ejercicio

1. Utilizar nombres de variables descriptivos.
2. Convertir el precio unitario utilizando `float()`.
3. Convertir la cantidad utilizando `int()`.
4. Calcular los resultados mediante operaciones entre variables.
5. No escribir manualmente el subtotal, IGV o total.
6. Mostrar los importes con dos decimales.
7. Organizar el código en entrada, procesamiento y salida.

---

## Estructura recomendada

```python
# Entrada de datos


# Procesamiento


# Salida de datos
```

Esta separación mejora la lectura y organización del programa.

---

## Preguntas de reflexión

Al finalizar la práctica, responde:

1. ¿Por qué `input()` devuelve siempre un texto?
2. ¿Cuál es la diferencia entre `int()` y `float()`?
3. ¿Por qué el precio debe convertirse a `float()`?
4. ¿Qué sucede si intentamos multiplicar un texto sin convertirlo?
5. ¿Qué significa el formato `.2f`?
6. ¿Cuál es la diferencia entre entrada, procesamiento y salida?

---

## Aprendizajes

Completar después de realizar la práctica.

*
*
*

---

## Errores encontrados

Registrar los errores que aparecieron durante la práctica.

*
*
*

---

## Cómo resolví los errores

Explicar brevemente cómo se corrigió cada problema.

*
*
*

---

## Estado de la práctica

* [ ] Leí y comprendí los conceptos.
* [ ] Realicé el ejercicio principal.
* [ ] Probé el programa con diferentes valores.
* [ ] Revisé los tipos de datos.
* [ ] Completé las preguntas de reflexión.
* [ ] Registré mis errores y aprendizajes.
* [ ] Realicé el mini-reto.
