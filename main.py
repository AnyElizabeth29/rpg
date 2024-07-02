import csv 
import random 
pessoas=[]
with open('camila.csv','r') as sei_la:
  ler=csv.reader(sei_la)
  for linha in ler:
    pessoas.append(linha) 

def ler_aventura(p1):
  for linlin in p1:
    print(linlin)

def esperar_continuar():
  continuar = input("digite c para continuar")
  while continuar != "c" and continuar != "C":
    continuar = input("digite c para continuar")

def mostra_aventura(p1, indice):
  if indice >= 0 and indice < len(p1):
    print(p1[indice])


def remover_aventura(p1, indice):
  total = len(p1)-1
  if indice >= 0 and indice < total:
    p1.pop(indice)
    print("Aventura removida com sucesso!")
    for i in p1:
      print(i)
  return p1

ler_aventura(pessoas)
esperar_continuar()
indice_aventura = int(input("Digite o indice da aventura: "))
mostra_aventura(pessoas, indice_aventura)
novo = remover_aventura(pessoas, indice_aventura)


