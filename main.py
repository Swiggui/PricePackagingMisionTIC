import json
#inserte el numero de paquetes a calcular
def calcularCosto(alto, ancho, profundo):
  #calcula los datos introducidos
  volumen = alto * ancho * profundo
  coste = volumen * 5
  #Validar si la altura es mayor a 30 y suma 2k al coste
  if alto > 30:
    coste = coste + 2000
  #Verifica si el coste es mayor a 10k y le agrega el IVA
  if coste > 10000:
    coste = coste + (coste * 0.19)
  return coste

def costoTotal(listaPaquetes, discount):
  totalCost = 0
  for counter, values in enumerate(listaPaquetes):
    alto = values["ALTO"]
    ancho = values["ANCHO"]
    profundo = values["PROFUNDO"]
    coste = calcularCosto(alto, ancho, profundo) 
    totalCost = coste + totalCost

  priceDisc = totalCost * (discount / 100)
  totalCost = totalCost - priceDisc
  return totalCost
def import_json():
  with open('paquetes.json') as file:
    empresa = json.load(file)
  return empresa
empresa = import_json()
paquetes = [
  {
    'ALTO': 20,
    'ANCHO': 10,
    'PROFUNDO': 5
  },
  {
    'ALTO': 7,
    'ANCHO': 10,
    'PROFUNDO': 5
  },
]
print (costoTotal(paquetes, 15))