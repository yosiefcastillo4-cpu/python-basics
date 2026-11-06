print ("Hola mundo")
print ("Estoy aprendiendo Python")

print ("")
# Practica de repaso python 

#Variables
num1= 15
num2= 26

print ("La suma de num1 y num2 es:",num1 + num2)
print ("")
#Entrada y conversión 
usuario= int(input("Ingrese su edad:"))

usuario+= 10
print ("Dentro de 10 años tendrás:", usuario)
print ("")

#Condicionales

nota= int(input("Ingrese su nota:"))

if nota >= 91 and nota <= 100:
    print ("Tu nota es A")

elif nota >= 81 :
    print ("Tu nota es B")

elif nota >= 71 :
    print ("Tu nota es C")

elif nota >= 61 :
    print ("Tu nota es D")

else:
    print ("Tu nota es F")

print ("")

#Operadores 

num= int(input("Ingrese un número:"))

if num % 2 == 0:
    print ("El número es par")
else:
    print ("El número es impar")

print ("")

#Listas

numeros= [1,2,3,4,5]

print ("Los números en la lista son:", numeros)

print ("La cantidad de números en la lista es:", len(numeros))

print ("")

#Bucles for

for i in range(21):
    print (i)

#Bucles while

contador = 10

while contador > 0:
    print (contador)
    contador -= 1

print(" ")

#Acumuladores   

suma = 0
i = 1

while i <= 100:
    suma += i
    i += 1
print ("La suma de los números del 1 al 100 es:", suma) 

print ("")

#Condicionales + bucles

for i in range(1, 31):
    if i % 2 == 0:
        print (i)
