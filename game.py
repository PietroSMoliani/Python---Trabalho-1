import random
import time

print("=== 🎬 Bem-vindo ao Jogo: Adivinhe o Filme! ===\n")
print("Você terá 3 tentativas por rodada para adivinhar o nome do filme a partir de uma dica.")
print("Não use acentos e digite apenas letras! Cada acerto vale 10 pontos.\n")

# Lista de filmes com dicas
filmes = [
    ("Um robô que vem do futuro para matar", "terminator"),
    ("Um jovem bruxo com uma cicatriz na testa", "harry potter"),
    ("Dinossauros ganham vida em um parque temático", "jurassic park"),
    ("Heróis lutando contra um titã roxo", "avengers"),
    ("Um palhaço assustador que vive nos esgotos", "it"),
]

pontuacao = 0

while True:
    dica, resposta = random.choice(filmes)
    tentativas = 3
    acertou = False

    while tentativas > 0:
        print(f"\nDica: {dica}")
        palpite = input("Qual é o filme? ").strip().lower()

        # Validação: entrada não pode ser vazia ou conter números
        if palpite == "":
            print("Entrada inválida! Você não digitou nada.")
            continue  # volta para pedir a resposta sem perder tentativa

        if not palpite.replace(" ", "").isalpha():
            print("Digite apenas letras e espaços, sem números ou símbolos!")
            continue

        # Verifica palpite
        if palpite == resposta:
            print("\n🎉 Parabéns! Você acertou o filme!")
            pontuacao += 10
            acertou = True
            break  # encerra rodada com vitória
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Resposta incorreta! Tente novamente. Tentativas restantes: {tentativas}")
            else:
                print("\nSuas tentativas acabaram...")
                print(f"O filme correto era: {resposta.title()}")

    # Mostra pontuação atual
    print(f"\nPontuação atual: {pontuacao} pontos")

    # Pergunta se quer jogar de novo
    jogar_novamente = input("\nQuer jogar outra rodada? (s/n) ").strip().lower()
    while jogar_novamente not in ["s", "n"]:
        jogar_novamente = input("Digite apenas 's' para sim ou 'n' para não: ").strip().lower()

    if jogar_novamente == "n":
        break  # sai do loop principal

# Fim do jogo
print("\n=== Fim do jogo! ===")
print(f"Sua pontuação final: {pontuacao} pontos")
print("Obrigado por jogar!")
time.sleep(1)
