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
    

#Funcion en la que se usa elif
def rendimiento(calif):
    if calif >= 4.5 and calif <= 5.0:
        print("Excelente")
    elif calif >= 4.0 and calif < 4.5:
        print("Bueno")
    elif calif >= 3.5 and calif < 4.0:
        print("Aceptable")
    elif calif >= 3.0 and calif < 3.5:
        print("Regular")
    else:
        print("Deficiente")

print("\n Ingrese su calificación: ")
print("y le diré como es su rendimiento academico. \n")
calif = float(input("Ingrese calificación de 0 a 5"))
if calif >= 0 and calif <= 5:
    rendimiento(calif)
else:
    print("Calificación Invalida")

print("Fin")

#Funcion que calcula el producto de números dados por el usuario
def producto_num(nu):
    producto = 1
    for cont in range(nu):
        print("#", cont + 1, end = " ")
        num2 = float(input(" "))
        producto = producto * num2
    return producto

nu = int(input("Cantidad de números"))
print(f"El producto de los {nu} números es {producto_num(nu)}")


#Función que pregunta números al usuario y dice cuales fueron negativos, y cuanto sumaron los positivos
def cuenta_numeros_suma(nu1):
    cont_no_pos = 0
    suma = 0
    for cont in range(nu1):
        print("#", cont + 1, end = " ")
        num = int(input())
        if num <= 0:
            cont_no_pos = cont_no_pos + 1
        else:
            suma = suma + num
    return [cont_no_pos, suma]

nu1 = int(input("Cantidad de números a verificar: "))
[cont_no_pos, suma] = cuenta_numeros_suma(nu1)  #Invocación de la función
print(f"De los números dados {cont_no_pos} fueron negativos o ceros y los positivos sumaron {suma}")

#Función que calcula la cantidad de números pares y suma los impares, contenidos en un conjunto de números
def cuenta_pares_suma_impares(n1):
    cont_par = 0
    sum_impar = 0
    for cont in range(n1):
        print ("#", cont + 1, end = " ")
        num = int(input())
        if num % 2 == 0:
            cont_par = cont_par + 1
        else:
            sum_impar = sum_impar + num
    print(f"Los números pares son: {cont_par} y la suma de los impares es: {sum_impar}")
#otra opcion de invocacion seria [cont_par, sum_impar] = cuenta_pares_suma_impares(n1), para qye esta funcione la funcion debe retornar cont_par y sum_impar
n1 = int(input("Ingrese la cantidad de números a verificar: "))
cuenta_pares_suma_impares(n1)

#Función que halla el mayor de cierta cantidad de números dados por el usuario
def num_mayor(num3):
    mayor = 0
    for cont in range (num3):
        print("#", cont + 1, end =  " ")
        num = int(input())
        if num > mayor:
            mayor = num
    return mayor

num3 = int(input("Ingrese la cantidad de números: "))
mayor = num_mayor(num3)
print(f"El número mayor de los ingresados es: {mayor}")


#Hallar el número menor de los dados por el usuario
def menor_de_numeros(num4):
    menor = int(input("Ingrese el primer número: "))
    for cont in range (num4 - 1):
        print("#", cont + 2, end = " " )
        num = int(input())
        if num < menor:
            menor = num
    return menor

num4 = int(input("Ingrese la cantidad de números a verificar: "))
menor = menor_de_numeros(num4)
print(f"De los números dados {menor} es el número menor")


#Escribir los números pares en orden descendente desde el ingresado por el usuario
def pares_desc(num5):
    print("Los números pares de ", num5, " a uno son: ")
    for cont in range(num5, 0, -2):
        print(cont, end =" ")

num5 = int(input("cantidad de Números a verificar: "))
if num5 % 2 == 0:
    pares_desc(num5)    #Ejemplo de invocación de la funcion
else:
    pares_desc(num5 - 1)    #Ejemplo de invocación de la funcion


#Escirbir los impares de uno al ingresado por el usuario
def impar_ascen(num5):
    print("Los números impares de uno hasta", num5, "son: ")
    for cont in range (1, num5 + 1, 2):
        print(cont, end = " ")

num5 = int(input("Ingrese el número hasta donde desea verificar: "))
if num5 % 2 == 0:
    impar_ascen(num5 + 1)
else:
    impar_ascen(num5)


#Curiosidad Matemática TERNIMADO EJERCICIO PERSONAL, CALCULO DEL CUADRADO DE UN NÚMERO (n) SUMANDO LOS PRIMEROS NUMEROS (n)IMPARES 
def opc_cuadrado(num6):
    cuadrado = []
    for cont in range (1, 2 * num6 + 1, 2):  # se multiplica por dos para calcular cuales son los impares

        cuadrado.append(cont)
        sum = 0
    for i in (cuadrado):
        sum = sum + i
    print(sum)
    
        
num6 = int(input("De que numero desea averiguar el cuadrado: "))
opc_cuadrado(num6)

#Ejemplo 19 Curioidad Matemática
def pide_num_positivo(que):
    n = -1  #Para que el valor de n sea solicitado al menos una vez
    while n < 1:
        print(que, "(>0)", end = " ")
        n = int(input())
    return n

def curiosidad(n):
    suma_imp = 0
    for impar in range (1, 2 * n + 1, 2):
        suma_imp = suma_imp + impar
    if n ** 2 == suma_imp:
        return [True, suma_imp]
    else:
        return [False, suma_imp]

print("Verifico la curiosidad matemática que dice que el\n cuadrado de un número dado (n)")
print("es la suma de los primeros números impares (n)")
print("Ejemplo: si (n) es igual a 7, entonces 7^2 = 1 + 3 + 5 + 7 + 9 + 11 + 13 = 49")

n = pide_num_positivo("Número")
[cumple, suma_imp] = curiosidad(n)
if cumple == True:
    print(f"La curiosisdad si se cumple {n} ^2 = {suma_imp}")
    print(f"que corresponde a la suma de los impares entre 1 y {n}.")
else:
    print("La curiosidad no se cumple")
print("FIN")


#FUNCIONES QUE LLAMAN A OTRAS FUNCIONES

#Escribir los impares o los impares de acuerdo a la selccion del usuario
def escribe_pares(n):
    for cont in range(2, n + 1, 2 ):
        print(cont, end = " ")

def producto_impares(n):
    prodcucto = 1
    for cont in range(1, n + 1, 2):
        producto = producto * cont
    return producto

def pares_producto_impar(n):
    if n % 2 == 0:
        escribe_pares(n)
    else:
        producto = producto_impares(n)
        print("El producto de 1 a ", n, "es ", producto)

print("Ingrese un número positivo")
print("Si el número es par, escribo los pares hasta el indicado")
print("Si es impar, multiplico los impares desde uno hasta el indicado")
numero = int(input("Número = : "))

pares_producto_impar(numero)


#calcular el máximo divisor de un número ????
def maximo_divisor(n):
    num = n // 2
    while num >= 2:
        if n % 2 == 0:
            return num
        num = num - 1
    return 0

num = int(input("Ingrese el número entero"))
md = maximo_divisor(num)
if md == 0 or num == 2:
    print(f"El número {num} es primo")
else:
    print(f" El máximo divisor de {num} es {int(md)}.")


#Obtener el resultado de elevar BASE a EXPONENTE  sin usar el operador de potencia
def potencia(base, exponente):
    base_to_exp = 1
    cont = 1
    while cont <= exponente:
        base_to_exp = base_to_exp * base
        cont = cont + 1
    return base_to_exp

base = float(input("Base = : "))
exponente = int(input("Exponente = : "))
if exponente >= 0:
    res = potencia(base, exponente)
    print("=> ", base, "^", exponente, "= ", res)
else:
    print("El exponente debe ser positivo o cero")


 #EJECUCION A PARTIR DE LA FUNCION MAIN()

 #Calcula el maximo común divisor de dos números
def calc_mcd(n1, n2):
    mcd = 1
    divisor = 2
    num1 = n1
    num2 = n2
    while divisor <= num1 and divisor <= num2:
        if num1 % divisor == 0 and num2 % divisor == 0:
            mcd = divisor
        divisor = divisor + 1
    return mcd

def main():
    print("Averiguo el máximo común divisor de dos números enteros")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 > 0 and num2 > 0:
        print(f"El MCD entre {num1} y {num2} es {calc_mcd(num1, num2)}")
        print("El MCD de", num1, "y", num2, "es", calc_mcd(num1, num2))
    else:
        print("Ingreso números ceros o números negativos")

main()  #Importante llamar la funcion 


#Calcula el índice de Masa corporal IMC
def calc_imc():
    masa = float(input("Cuál es su peso en Kilos?  --> "))
    estatura = float(input("Cuál es su estatura en metros? --> "))
    imc = masa // (estatura ** 2)
    return [masa, estatura, imc]

def main():
    [masa, estatura, imc] = calc_imc()      #Invocacion de la funcion
    print(f"Como su peso es {masa} kilos, y su altura es {estatura} metros ", end = " "  )
    print(f"Su índice de masa corporal es {imc}")

main()


#Averigua si un entero positivo mayor que 1 es primo
def es_primo(numero):
    primo = True
    posible_divisor = 2
    while primo == True and posible_divisor <= numero // 2:
        if numero % 2 == 0:
            primo = False
        posible_divisor = posible_divisor + 1
    return primo

def main():
    print("Ingrese el número que desea verificar si es primo, debe ser mayor que uno: -->  ")
    num = int(input("Ingrese el número: "))
    if es_primo(num) == True:
        print(num, "Es PRIMO")
    else:
        print(num, "NO es primo")
    
main()

#Extrae las últimas tres cifras de un número de más de tres cifras
def ultimas_tres(n):
    cont = 1
    pot10 = 1
    num3cifras = 0
    while cont <= 3:
        num = n - (n // 10)*10
        #print("num = ",num)
        num3cifras = num3cifras + num * pot10
        #print("num3cifras = ", num3cifras)
        pot10 = pot10 * 10
        #print("pot10 = ", pot10)
        n = n // 10
        #print("n = ", n)
        cont = cont + 1
    return num3cifras

def main():
    numero = int(input("Ingrese número entero de más de tres cifras: "))
    num3 = ultimas_tres(numero)
    print(f"Las últimas tres cifras del dato ingresado son: --->  {num3}")

main()

#Calcula la potencia de 2 que es  menor o igual que un número dado
def mayor_pot2_menor_que_n(n):
    valor = 1
    potencia = 0
    while valor < n:
        valor = valor * 2
        potencia = potencia + 1
    if valor == n:
        return potencia
    else:
        return potencia - 1


def main():
    print("Ingrese un número positivo y yo le devuelvo la mayor potencia de 2, menor o igual que dicho número")
    numero = int(input("Número =  "))
    mayorpot_2 = mayor_pot2_menor_que_n(numero)
    print(mayorpot_2, "Es la mayor potencia de dos, menor o igual que", numero)
    print("Es decir,", 2 ** mayorpot_2, "<=", numero)

main()

#Soluciona una ecuación cuadrática, es deir, una ecuación de la forma ax^2 + bx + c = 0; a,b,c e R, a diferente 0
def ingresa_coeficientes():
    print("Valor de los coeficientes: --->")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    return[a, b, c]

def solu_ecuacion(a, b, c):
    print("La ecuación ", a, "x^2 + ", b, "x + ", c, " = 0 tiene dos soluciones")
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        s1 = (-b + (disc) ** 0.5) / (2 * a)
        s2 = (-b - (disc) ** 0.5) / (2 * a)
        print("reales: x1 = ", format(s1, ".2f"), "y x2 = ", format(s2, ".2f"))  # format se usa para definir la cantidad de decimales a usar
    elif disc < 0:
        p_r = -b / (2 * a)
        p_i =((-disc) ** 0.5) / (2 * a)
        print("complejas: \n\n\tx1 =", format(p_r, ".2f"), "+", format(p_i, ".2f"), "i")
        print("\n\tx2 = ", format(p_r, ".2f"), " - ", format(p_i, ".2f"), "i")
    else:
        #disc es cero
        print("reales e iguales: x1 = x2 = ", format( - b / (2 * a), ".2f"))

def main():
    print("\n\t Solucione ecuaciones cuadráticas, es decir, ecuaciones de la forma")
    print("\tax^2+bx+c=0; a, b, c que pertenecen al conjunto de los números reales.")
    print("Intentemoslo...")
    [a, b, c] = ingresa_coeficientes()
    solu_ecuacion(a, b, c)
    print("Fin")

main()


