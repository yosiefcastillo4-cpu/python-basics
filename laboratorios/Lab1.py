blocks = int(input("Ingresa el número de bloques: "))

height = 0
blocks_needed = 1  # La primera capa requiere 1 bloque

while blocks >= blocks_needed:
    blocks -= blocks_needed  # Restamos los bloques usados
    height += 1              # Aumentamos una capa a la altura
    blocks_needed += 1       # La siguiente capa requerirá un bloque más

print("La altura de la pirámide es:", height)

