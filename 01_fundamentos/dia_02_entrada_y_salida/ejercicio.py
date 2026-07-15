# Día 02 - Entrada, salida y conversión de datos

# Entrada de datos
producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

# Procesamiento
subtotal = cantidad * precio_unitario
igv = subtotal * 0.18
total = subtotal + igv

# Salida de datos
print("\n================== RESUMEN DE COMPRA ==================")
print(f"Producto: {producto}")
print(f"Subtotal: S/ {subtotal:.2f}")
print(f"IGV: S/ {igv:.2f}")
print(f"Total a pagar: S/ {total:.2f}")