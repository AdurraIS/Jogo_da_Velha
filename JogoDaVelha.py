import random

print("Jogo da Velha")
print("Você vs Computador")
print("Ganha quem conseguir uma linha, coluna do diagonal do grid com o mesmo símbolo")

print("Você precisa escolher uma posição no grid para marcar sua jogada, de acordo com a numeração")
print("_ _ _")
print("_ _ _")
print("_ _ _")
print("Escolha um numero de 1 a 9 para sua jogada a seguir")
print("1 2 3")
print("4 5 6")
print("7 8 9")

def verifica_grid(grid, jogador):
    # teste linha
    if(grid[0] == jogador and grid[1] == jogador and grid[2] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2
    if (grid[3] == jogador and grid[4] == jogador and grid[5] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2
    if (grid[6] == jogador and grid[7] == jogador and grid[8] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2

    #teste coluna
    if (grid[0] == jogador and grid[3] == jogador and grid[6] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2
    if (grid[1] == jogador and grid[4] == jogador and grid[7] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2
    if (grid[2] == jogador and grid[5] == jogador and grid[8] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2

    return 0
    #teste diagonal

    if (grid[0] == jogador and grid[4] == jogador and grid[8] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2
    if (grid[2] == jogador and grid[4] == jogador and grid[6] == jogador):
        if jogador == "X":
            return 1
        else:
            return 2

quantidade_escolhas = 0

def imprime_grid(grid):
    for i in range(len(grid)):
        print(grid[i], end=" ")
        if i == 2 or i == 5:
            print("")

grid = ["_"] * 9

while True:
    escolha = int(input("Qual é a sua escolha? "))
    while grid[escolha - 1] != "_":
        print("Escolha inválida")
        imprime_grid(grid)
        print("")
        escolha = int(input("Qual é a sua escolha? "))
    grid[escolha - 1] = "X"
    quantidade_escolhas +=1
    vencedor = verifica_grid(grid, "X")
    if vencedor !=0:
        break
    if quantidade_escolhas == 9:
        break
    print("O status da grid é:")
    imprime_grid(grid)
    print("")


    escolha_computador = random.randint(1,9)
    while grid[escolha_computador-1] != "_":
        escolha_computador = random.randint(1, 9)

    grid[escolha_computador-1] = "O"
    quantidade_escolhas += 1

    vencedor = verifica_grid(grid, "O")

    if vencedor != 0:
        break
    if quantidade_escolhas == 9:
        break


    print("O status da grid é:")
    imprime_grid(grid)

    print("")
if vencedor ==1:
    print("Parabéns, você ganhou")
elif vencedor ==2:
    print("Você perdeu, o computador ganhou")
elif(vencedor != 0):
    print("Deu velha, ninguém venceu, foi empate")
imprime_grid(grid)
