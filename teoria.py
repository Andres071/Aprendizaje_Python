"""Este documento contiene ejercicios de ejemplo incluidos en un libro de aprendizaje de Python,
    Utilice el bloque de código que necesite. No lo ejecute todo de una sola vez, porque genera error"""
    
#Uso de print, print(argumentos), esta es la sintaxis de print, para mostrar en pantalla
varexe = "Bus N0 4408"
print(varexe) #Imprime lo almacenado en la variable sueldo
print(15)#imprime 15 en la pantalla
print("Ella dijo: \"Soy testigo\"")# Para imprimir comillas se usa \"
a = 23
b = 19
c = 0
print(a, "+", b, "=", c) #imprime la suma de las dos valiabres y el resultado lo guarda en c
print(a < b)#imprime True o False dependiendo del resultado de la evaluacion

"""input(texto), esta es la instruccion para ingresar datos por el teclado"""
nombre = input("Como se llama ? ")
edad = int(input("Cuantos años tiene? ")) # Se cambia el tipo de dato
sueldo = float(input("Cuanto gana? "))
#La funcion input solo acepta un argumeto

"""Uso de f para concatenar, en Python 3 en adelante"""
print(f"{nombre} tiene {edad} años y recibe pension de ${sueldo}")
print(nombre, "tiene", edad, "años y recibe pension de $", sueldo)
print("{nombre} tiene {edad} años y recibe pension de ${sueldo}")

"""ESTRUCTURAS DE CONTROL CONDICIONALES"""
#   No repetitivas
#   if
num = float(input("Ingrese un número negativo"))
if num >= 0:
    print(f"El numeroque ingreso es{num}, el cual no es negativo")

#   if-else
valor = int(input("Ingrese un número positivo"))
if valor % 2 == 0:
    print(f"El número {valor} es par")
else:
    print(f"El número {valor} es impar")

#   elif
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0
countOther = 0

vocal = input("Ingrese una vocal")
if vocal == "a" or vocal == "A":
    print(f"Ingreso una {vocal}")
    contA = contA + 1
elif vocal == "e" or vocal == "E":
    print(f"Ingreso una {vocal}")
    contE = contE + 1
elif vocal == "i" or vocal == "I":
    print(f"Ingreso una {vocal}")
    contI = contI + 1
elif vocal == "o" or vocal == "O":
    print(f"Ingreso una {vocal}")
    contO = contO + 1
elif vocal == "u" or vocal == "U":
    print(f"Ingreso una {vocal}")
    contU = contU + 1
else:
    print("No ingreso una vocal")
    countOther = countOther + 1

"""ESTRUCTURAS DE CONTROL REPETITIVAS"""

#   while
cont = 1
fin1 = int(input("Escribire los números desde el 1 hasta donde me diga "))
while cont <= fin1:
    print(cont, end=" ")
    cont = cont + 1
if cont == 1:
    print(fin1, "No es un número hasta donde llegar")



#   for
fin2 = int(input("Escribire los números desde el 1 hasta donde me diga "))
for cont in range(fin2):
    print(cont, end = " ")
# 9 output  0 1 2 3 4 5 6 7 8 

##for 
fin3 = int(input("Escribire los números desde el 1 hasta donde me diga "))
for cont in range(1, fin3 +1):
    print(cont, end = " ")
# 9 output  0 1 2 3 4 5 6 7 8 

#for
fin4 = int(input("Escribire los números desde el 1 hasta donde me diga "))
for cont in range(0, fin4 +1):
    print(cont + 1, end = " ")
# 9 output   1 2 3 4 5 6 7 8 9 10

#for 
fin5 = int(input("Escribo los impares desde 1 hasta donde me diga "))
for cont in range (1, fin5 +1, 2):
    print(cont, end = " ")
# 21 output 1 3 5 7 9 11 13 15 17 19 21

# for en orden descendente
inicio = int(input("Escribire los números en orden descendente "))
for cont in range(inicio, 0, -1):  #El -1 es el que permite contar hacia atras
    print(cont, end = " ")
# 9 outout 9 8 7 6 5 4 3 2 1 


"""FUNCIONES"""
# def nombre_de_la_funcion(lista de parámetros separada por comas):
#      cuerpo de la función(lo que hace la función)
#      return
#Función y su invocación
def impares(fin6):
    for cont in range (1, fin6 + 1, 2):
        print(cont, end = " ")
    
#Llamado de la función
#opcion 1
fin6 = int(input("Escribo los impares de 1 hasta donde me diga "))
impares(fin6)
# opcion 2
impares(25)
# 9 output 1 3 5 7 9 11 13 15 17 19 21 23 25 


#Función que devuelve un valor, y su invoción
def suma_1_a_n (fin7):
    suma = 0
    for cont in range (1, fin7 + 1):
        suma = suma + cont
    return suma
#Invocación de la función
fin7 = int(input("Sumo los numeros de 1 hasta donde me digas "))
print (f"Los números de 1 a {fin7} suman {suma_1_a_n(fin7)} ")
#En este ejemplo se requiere la funcion de retorno return

#Función Booleana, devuelve True o False
def es_par(num1):
    if num1 % 2 == 0:
        return True
    else: 
        return False

numero = int(input("Averiguo si un número es Par "))

if es_par (numero) == True:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
    

