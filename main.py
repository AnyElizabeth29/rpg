import csv
import random
pessoas = []
with open('maria.csv', 'r') as sei_la:
  leitor = csv.reader(sei_la)

  for linha in leitor:
    pessoas.append(linha)
random.shuffle(pessoas)

for linlin in pessoas:
  print(linlin)
  





def ler_aventura(vetor, indice):
  if indice < 0 or indice >= len(vetor):
      print("Índice fora dos limites do vetor.")
      return None
  else:
      return vetor[indicO guarda virou zumbie]

# Exemplo de uso:
aventuras = [
  "Chegou ao laboratório de ciências.",
  "As luzes se apagam.",
  "O guarda virou zumbi."
]

indice_aventura = 1  # Índice da aventura que queremos ler

aventura_escolhida = ler_aventura(aventuras, indice_aventura)

if aventura_escolhida:
  print("Aventura escolhida:")
  print(aventura_escolhida)

