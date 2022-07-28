def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1,num2):
    return num1 // num2

num1 = int(input("Selecciona el primer numero: "))
num2 = int(input("Selecciona el segundo numero: "))
operacion = input("Que tipo de operacion quieres realizar (suma,resta,multiplicacion,division):")

if operacion == "suma":
    print(suma(num1,num2))
elif operacion == "resta":
    print(resta(num1,num2))
elif operacion == "multiplicacion":
    print(multiplicacion(num2,num2))
elif operacion == "division":
    print(division(num1,num2))
else:
    print("Selecciona una de las cuatro operaciones posibles")

print("operacion realizada")