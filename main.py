import csv 
import random 

# Lista que armazenará as aventuras lidas do arquivo CSV
pessoas = []

# Função para ler e imprimir todas as aventuras
def ler_aventura(p1):
    for linlin in p1:
        print(linlin)

# Função para mostrar os detalhes de uma aventura específica pelo índice
def mostra_aventura(p1, indice):
    if indice >= 0 and indice < len(p1):
        print(p1[indice])

# Função para carregar aventuras de um arquivo CSV para uma lista
def carregar_aventuras(arquivo):
    aventuras = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Pula o cabeçalho do arquivo CSV
        for linha in reader:
            if len(linha) > 9:
                linha = linha[:9]  # Garante que cada linha tenha exatamente 9 elementos
            if len(linha) == 9:
                aventuras.append(linha)  # Adiciona a aventura à lista de aventuras
            else:
                print(f"Formato inesperado: {linha}")  # Mensagem de erro se o formato não for o esperado
    return aventuras

# Função para salvar aventuras de uma lista de aventuras de volta ao arquivo CSV
def salvar_aventuras(arquivo, aventuras):
    with open(arquivo, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ambiente", "aventura", "op1", "op2", "porc1", "porc2", "rsuc1", "rsuc2", "rfrac1"])  # Escreve o cabeçalho
        writer.writerows(aventuras)  # Escreve as aventuras no arquivo CSV

# Função para imprimir todas as aventuras com seus índices
def ler_aventura(aventuras):
    for index, linlin in enumerate(aventuras):
        print(f"Índice {index + 1}: {linlin[1]}")

# Função para aguardar até que o usuário digite 'c' para continuar
def esperar_continuar():
    continuar = input("Digite c para continuar: ")
    while continuar.lower() != "c":
        continuar = input("Digite c para continuar: ")

# Função para mostrar os detalhes de uma aventura específica
def mostrar_detalhes_aventura(aventura):
    if len(aventura) != 9:
        print(f"Formato de aventura inesperado: {aventura}")  # Mensagem de erro se o formato não for o esperado
        return
    ambiente, descricao, op1, op2, porc1, porc2, rsuc1, rsuc2, rfrac1 = aventura
    print(f"Ambiente: {ambiente}\n")
    print(f"Aventura: {descricao}\n")
    print(f"op1: {op1} (sucesso: {porc1})\n")
    print(f"op2: {op2} (sucesso: {porc2})\n")

# Função para determinar o resultado com base na escolha do usuário
def determinar_resultado(escolha, aventura):
    if len(aventura) != 9:
        print(f"Formato de aventura inesperado: {aventura}")  # Mensagem de erro se o formato não for o esperado
        return
    _, _, op1, op2, porc1, porc2, rsuc1, rsuc2, rfrac1 = aventura

    if escolha == "op1":
        resultado = rsuc1 if float(porc1.rstrip('%')) >= 50 else rfrac1
    elif escolha == "op2":
        resultado = rsuc2 if float(porc2.rstrip('%')) >= 50 else rfrac1
    else:
        resultado = "Escolha inválida."

    print(f"Você escolheu {escolha}. {resultado}")

# Função para mostrar os detalhes de uma aventura específica pelo índice
def mostra_aventura(aventuras, indice):
    if indice >= 0 and indice < len(aventuras):
        mostrar_detalhes_aventura(aventuras[indice])
    else:
        print("Índice inválido. Tente novamente.")

# Função para remover uma aventura da lista pelo índice
def remover_aventura(aventuras, indice):
    total = len(aventuras)
    if indice >= 0 and indice < total:
        aventuras.pop(indice)
        print("Aventura removida com sucesso!")
        return aventuras
    else:
        print("Índice inválido. Tente novamente.")
        return aventuras

# Carregar aventuras do arquivo CSV para a lista 'pessoas'
pessoas = carregar_aventuras('camila.csv')

# Imprimir todas as aventuras com seus índices
ler_aventura(pessoas)

# Aguardar até que o usuário digite 'c' para continuar
esperar_continuar()

try:
    # Solicitar ao usuário que digite o índice da aventura desejada
    indice_aventura = int(input("Digite o índice da aventura: ")) - 1 
    if indice_aventura < 0 or indice_aventura >= len(pessoas):
        print("Índice inválido. Tente novamente.")
    else:
        # Mostrar os detalhes da aventura escolhida
        mostra_aventura(pessoas, indice_aventura)

        # Solicitar ao usuário que escolha op1 ou op2
        escolha = input("Escolha (op1/op2): ").strip()

        # Determinar e mostrar o resultado com base na escolha do usuário
        determinar_resultado(escolha, pessoas[indice_aventura])

        # Remover a aventura da lista 'pessoas' e atualizar o arquivo CSV
        pessoas = remover_aventura(pessoas, indice_aventura)
        salvar_aventuras('camila.csv', pessoas)

except ValueError:
    print("Entrada de índice inválida. Por favor, digite um número.")
