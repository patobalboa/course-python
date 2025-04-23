
n1 = int(input("Ingresa un numero"))
n2 = int(input("Ingresa un segundo numero"))

print(n1 + n2) # Suma devuelve 12
print(n1 - n2) # Resta devuelve 2
print(n1 * n2) # Multiplica devuelve 35
print(n1 / n2) # Divide devuele 1.4
print(n1 ** n2) # Potencia no devuelve 16807
print(n1 // n2) # Divide y devuelve entero 1
print(n1 % n2) # Modulo nos devulve 2

# Escribe un codigo donde le solicites 2 numeros 
# Al usuario y resultado te indique si este es
# Par o Impar.
resultado = n1 + n2

if resultado % 2 == 0:
    print("Es par")
else:
    print("Es impar")