# Día 01 - Variables y tipos de datos
# Escribe tu solución debajo de cada comentario.
#============================================
# ENTRADA DE DATOS
#============================================
# 1. Solicita el nombre del usuario.
nombre = input("Ingrese su nombre: ")
# 2. Solicita la edad y conviértela a entero.
edad = int(input("Ingrese su edad: "))
# 3. Solicita la ciudad.
ciudad = input("Ingrese su ciudad: ")
# 4. Solicita la carrera.
carrera = input("Ingrese su carrera: ")
#============================================
# PROCESAMIENTO
#============================================
anio_actual = 2026
anio_nacimiento = anio_actual - edad

#============================================
# SALIDA DE DATOS
#============================================
# 5. Muestra una presentación utilizando una f-string.
print(f"Hola, {nombre}.")
print(f"Tienes {edad} años, vives en {ciudad} y estudias {carrera}.")
print(f"Naciste aproximadamente en el año {anio_nacimiento}.")
