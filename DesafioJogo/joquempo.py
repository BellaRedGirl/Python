import random

continuar = True
jogadas = ['pedra', 'papel', 'tesoura']

def jogar():
    jogador = input("Olá! Você deseja jogar pedra, papel ou tesoura?: ").lower()
    return jogador

def escolhaComputador():
    computador = random.choice(jogadas)
    return computador

def verificar(jogador, computador):
    if jogador == computador:
        return "Tivemos um empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"
    
while continuar:
    jogador = jogar()
    computador = escolhaComputador()
    print(f"O computador jogou: {computador}")
    resultado = verificar(jogador, computador)
    print(resultado)

    continuar = input("Deseja jogar novamente? (s/n): ").lower() == 's'
