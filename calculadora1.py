#inicio 
print("*****************")
print("***Calculadora***")
print("*****************")
print("             v0.1")
print("")

#variables
numero_uno = int(input("Digite el primer número: "))
numero_dos = int(input("Digite el segundo número: "))

print("")

print("suma")
print("resta")
print("multiplicación")
print("división")

print("")

eleccion = str(input("¿Qué desea hacer? "))

#condicionales
if eleccion == "suma":
	resultado = numero_uno + numero_dos
	print("El resultado es: ", resultado)

if eleccion == "resta":
	resultado = numero_dos - numero_dos
	print("El resultado es: ", resultado)

if eleccion == "multiplicación":
	resultado = numero_uno * numero_dos
	print("El resultado es: ", resultado)

if eleccion == "división":
	resultado = numero_uno / numero_dos
	print("El resultado es: ", resultado)	