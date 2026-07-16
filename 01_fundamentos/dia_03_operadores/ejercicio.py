# Día 03 - Operadores en Python

# Entrada de datos
nombre = input("Ingrese su nombre: ")
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
pago_por_hora = float(input("Ingrese su pago por hora: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# Procesamiento
pago_bruto = horas_trabajadas * pago_por_hora
descuento_decimal = porcentaje_descuento / 100
monto_descuento = pago_bruto * descuento_decimal
pago_neto = pago_bruto - monto_descuento

dias_completos = horas_trabajadas // 8
horas_restantes = horas_trabajadas % 8
pago_supera_referencia = pago_neto >= 800

# Salida de datos
print("\n=====================================")
print("           RESUMEN DE PAGO")
print("=====================================\n")
print(f"Trabajador: {nombre}")
print(f"Pago bruto: S/ {pago_bruto:.2f}")
print(f"Descuento: S/ {monto_descuento:.2f}")
print(f"Pago neto: S/ {pago_neto:.2f}")
print(f"Días completos de 8 horas: {dias_completos}")
print(f"Horas restantes: {horas_restantes}")
print(f"¿El pago neto es mayor o igual a S/ 800?: {pago_supera_referencia}")