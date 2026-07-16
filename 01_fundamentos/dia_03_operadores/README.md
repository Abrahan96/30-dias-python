# Día 03 — Operadores en Python

## Objetivo

Comprender cómo Python realiza operaciones matemáticas, asigna valores y compara datos.

Al finalizar esta práctica, seremos capaces de:

* Realizar cálculos con variables.
* Comprender los operadores aritméticos.
* Actualizar valores mediante operadores de asignación.
* Comparar resultados.
* Aplicar el orden correcto de las operaciones.
* Construir un programa que procese datos numéricos.

---

## 1. Operadores aritméticos

Los operadores aritméticos permiten realizar cálculos matemáticos.

| Operador | Operación        | Ejemplo   |
| -------- | ---------------- | --------- |
| `+`      | Suma             | `10 + 5`  |
| `-`      | Resta            | `10 - 5`  |
| `*`      | Multiplicación   | `10 * 5`  |
| `/`      | División decimal | `10 / 5`  |
| `//`     | División entera  | `10 // 3` |
| `%`      | Residuo o módulo | `10 % 3`  |
| `**`     | Potencia         | `2 ** 3`  |

### Suma

```python
resultado = 10 + 5
```

Resultado:

```text
15
```

### Resta

```python
resultado = 10 - 5
```

Resultado:

```text
5
```

### Multiplicación

```python
resultado = 10 * 5
```

Resultado:

```text
50
```

### División

```python
resultado = 10 / 4
```

Resultado:

```text
2.5
```

La división con `/` devuelve normalmente un valor de tipo `float`.

### División entera

```python
resultado = 10 // 4
```

Resultado:

```text
2
```

La división entera descarta la parte decimal.

### Módulo

```python
resultado = 10 % 4
```

Resultado:

```text
2
```

El operador `%` devuelve el residuo de una división.

### Potencia

```python
resultado = 2 ** 3
```

Representa:

```text
2 × 2 × 2
```

Resultado:

```text
8
```

---

## 2. Operadores de asignación

El operador principal de asignación es:

```python
=
```

Ejemplo:

```python
saldo = 100
```

También existen operadores que permiten actualizar una variable.

| Operador | Ejemplo       | Equivalencia         |
| -------- | ------------- | -------------------- |
| `+=`     | `saldo += 20` | `saldo = saldo + 20` |
| `-=`     | `saldo -= 10` | `saldo = saldo - 10` |
| `*=`     | `saldo *= 2`  | `saldo = saldo * 2`  |
| `/=`     | `saldo /= 2`  | `saldo = saldo / 2`  |

Ejemplo:

```python
saldo = 100
saldo += 50
```

Resultado:

```text
150
```

---

## 3. Operadores de comparación

Los operadores de comparación permiten comparar dos valores.

El resultado siempre será un valor booleano:

```python
True
False
```

| Operador | Significado       |
| -------- | ----------------- |
| `==`     | Igual que         |
| `!=`     | Diferente de      |
| `>`      | Mayor que         |
| `<`      | Menor que         |
| `>=`     | Mayor o igual que |
| `<=`     | Menor o igual que |

Ejemplo:

```python
edad = 30

print(edad > 18)
```

Resultado:

```text
True
```

Otro ejemplo:

```python
precio = 100

print(precio == 80)
```

Resultado:

```text
False
```

### Diferencia entre `=` y `==`

El operador:

```python
=
```

sirve para asignar un valor.

```python
edad = 30
```

El operador:

```python
==
```

sirve para comparar valores.

```python
edad == 30
```

Confundirlos es uno de los errores más frecuentes al comenzar.

---

## 4. Orden de las operaciones

Python respeta el orden matemático de las operaciones.

El orden principal es:

1. Paréntesis
2. Potencias
3. Multiplicaciones y divisiones
4. Sumas y restas

Ejemplo:

```python
resultado = 10 + 5 * 2
```

Primero se multiplica:

```text
5 × 2 = 10
```

Luego se suma:

```text
10 + 10 = 20
```

Resultado:

```text
20
```

Si queremos cambiar el orden:

```python
resultado = (10 + 5) * 2
```

Primero se resuelve el paréntesis:

```text
10 + 5 = 15
```

Después se multiplica:

```text
15 × 2 = 30
```

Resultado:

```text
30
```

---

# Ejercicio principal

## Calculadora de pago semanal

Crear un programa que solicite:

* Nombre del trabajador
* Horas trabajadas
* Pago por hora
* Descuento porcentual

El programa deberá calcular:

```text
Pago bruto = horas trabajadas × pago por hora
```

```text
Descuento = pago bruto × porcentaje de descuento
```

```text
Pago neto = pago bruto - descuento
```

También deberá calcular cuántos días completos de ocho horas trabajó el empleado y cuántas horas quedaron como residuo.

```text
Días completos = horas trabajadas // 8
Horas restantes = horas trabajadas % 8
```

---

## Ejemplo de ejecución

```text
Ingrese el nombre del trabajador: Abrahan
Ingrese las horas trabajadas: 45
Ingrese el pago por hora: 20
Ingrese el porcentaje de descuento: 10

=============== RESUMEN DE PAGO ===============
Trabajador: Abrahan
Pago bruto: S/ 900.00
Descuento: S/ 90.00
Pago neto: S/ 810.00
Días completos de 8 horas: 5
Horas restantes: 5
```

---

## Reglas del ejercicio

1. Usar nombres de variables descriptivos.
2. Convertir las horas trabajadas a `int`.
3. Convertir el pago por hora a `float`.
4. Convertir el porcentaje de descuento a `float`.
5. No escribir manualmente los resultados.
6. Utilizar los operadores `*`, `/`, `-`, `//` y `%`.
7. Mostrar los importes con dos decimales.
8. Organizar el programa en entrada, procesamiento y salida.
9. No utilizar todavía condicionales.

---

## Fórmulas

```python
pago_bruto = horas_trabajadas * pago_por_hora
```

Para convertir el porcentaje ingresado:

```python
porcentaje_decimal = porcentaje_descuento / 100
```

Después:

```python
descuento = pago_bruto * porcentaje_decimal
```

Y finalmente:

```python
pago_neto = pago_bruto - descuento
```

Para obtener días completos:

```python
dias_completos = horas_trabajadas // 8
```

Para obtener las horas restantes:

```python
horas_restantes = horas_trabajadas % 8
```

---

## Preguntas de reflexión

1. ¿Cuál es la diferencia entre `/` y `//`?
2. ¿Qué devuelve el operador `%`?
3. ¿Cuál es la diferencia entre `=` y `==`?
4. ¿Por qué debemos dividir un porcentaje entre `100`?
5. ¿Qué operación se ejecuta primero en `10 + 5 * 2`?
6. ¿Para qué sirven los paréntesis en una expresión?
7. ¿Qué tipo de dato devuelve una comparación?

---

## Aprendizajes

Completar al finalizar la práctica.

*
*
*

---

## Errores encontrados

Registrar los errores que aparezcan.

*
*
*

---

## Cómo resolví los errores

Explicar brevemente cómo se corrigieron.

*
*
*

---

## Estado de la práctica

* [ ] Comprendí los operadores aritméticos.
* [ ] Comprendí los operadores de asignación.
* [ ] Comprendí los operadores de comparación.
* [ ] Diferencié `/`, `//` y `%`.
* [ ] Realicé el ejercicio principal.
* [ ] Probé el programa con diferentes valores.
* [ ] Completé las preguntas de reflexión.
* [ ] Registré mis errores y aprendizajes.
* [ ] Realicé el mini-reto.
