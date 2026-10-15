import csv

def cadastrar_jogador():
    nome = input("nome:")
    idade = input("idade:")
    pontuacao = input("pontuacao")
    with open("jogadores.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, pontuacao])
    print("jogador salvo:")

def ver_jogadores():
    with open("jogadores.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        print("=== JOGADORES ===")
        for linha in leitor:
            nome = linha[0]
            idade = linha[1]
            pontuacao = linha[2]
            print(f"{nome} - {idade} - {pontuacao}")

def ver_ranking():
    with open("jogadores.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        jogadores = []
        for linha in leitor:
            nome = linha[0]
            idade = linha[1]
            pontuacao = int(linha[2])
            jogadores.append([nome, idade, pontuacao])
    jogadores.sort(key=lambda x: x[2], reverse=True)
    print("=== RANKING ===")
    posicao = 1
    for jogador in jogadores:
        print(f"{posicao} - {jogador[0]} - {jogador[2]}")
        posicao += 1

def gerar_relatorio():
    with open("jogadores.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        jogadores = []
        for linha in leitor:
            nome = linha[0]
            idade = linha[1]
            pontuacao = int(linha[2])
            jogadores.append([nome, idade, pontuacao])
    total_pontos = 0
    maior_pontuacao = 0
    melhor_jogador = ""
    for jogador in jogadores:
        pontos = jogador[2]
        total_pontos += pontos
        if pontos > maior_pontuacao:
            maior_pontuacao = pontos
            melhor_jogador = jogador[0]
    media = total_pontos / len(jogadores)
    print("=== RELATORIO === ")
    print(f" total de jogadores; {len(jogadores)}")
    print(f"media de pontuacao: {media:.2f}")
    print(f"melhor jogador: {melhor_jogador}")
    print(f"maior pontuacao: {maior_pontuacao}")

while True:
    print("\n1 - cadastrar jogador")
    print("2 - ver jogadores")
    print("3 - ver ranking")
    print("4 - ver relatorio")
    print("5 - sair")
    opcao = input("escolha uma opcao:")
    if opcao == "1":
        cadastrar_jogador()
    elif opcao == "2":
        ver_jogadores()
    elif opcao == "3":
        ver_ranking()
    elif opcao == "4":
        gerar_relatorio()
    elif opcao == "5":
        print("saindo...")
        break
    else:
        print("opcao invalida!")
