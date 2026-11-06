c0 = int(input("Ingrese un numero entero que no sea negativo y que no sea cero:"))

steps = 0
if c0 > 0:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = (3 * c0) + 1
            
        print(c0)
        steps += 1
    
    print("El número de pasos es:", steps)
else:
    print("El número ingresado no es válido. Debe ser un entero positivo mayor que cero.")




