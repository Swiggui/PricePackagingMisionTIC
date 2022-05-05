#Introducir datos
alto = float(input())
ancho = float(input())
profundo = float(input())
#calcula los datos introducidos
volumen = alto * ancho * profundo
coste = volumen * 5
#Validar si la altura es mayor a 30 y suma 2k al coste
if alto > 30:
  coste = coste + 2000
#Verifica si el coste es mayor a 10k y le agrega el IVA
if coste > 10000:
    coste = coste + (coste * 0.19)
#imprime datos calculados
print(volumen)
print(coste)