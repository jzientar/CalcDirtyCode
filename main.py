#Dirty Code

o = 1

print("Seleccione una operacion.")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("0. Salir")

while o != 0:
    o = input("\nIntroduzca su opcion (0-4): ")
    if o == '1':
        a = float(input("Introduzca el primer numero: "))
        b = float(input("Introduzca el segundo numero: "))
        print(a, "+", b, "=", a + b)
    elif o == '2':
        a = float(input("Introduzca el primer numero: "))
        b = float(input("Introduzca el segundo numero: "))
        print(a, "-", b, "=", a - b)
    elif o == '3':
        a = float(input("Introduzca el primer numero: "))
        b = float(input("Introduzca el segundo numero: "))
        print(a, "*", b, "=", a * b)
    elif o == '4':
        a = float(input("Introduzca el primer numero: "))
        b = float(input("Introduzca el segundo numero: "))
        print(a, "/", b, "=", a / b)
    elif o == '0':
        break