print("=== CALCULADORA ===")

num1 = float(input("Ingresa el primer número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: no se puede dividir entre cero"
else:
    resultado = "Error: operación no válida"

print("Resultado:", resultado)
