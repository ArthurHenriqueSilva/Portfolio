from random import randint
from math import log2


print("Advinhe o número!")
print("Digite os valores limites para o jogo.")
v1 = int(input("Digite o menor valor: "))
v2 = int(input("Digite o maior valor: "))
answer = randint(v1,v2)
chances = round(log2(v2 - v1 + 1))

count = 0
status = False
aux = "chance" if chances == 1 else "chances"
print(f"Você terá {chances} {aux}")

while count < chances:
    if count == chances - 1:
        print("Essa é sua última chance!! Boa sorte!")
    while True:
        try:
            user_guess = int(input("Digite seu palpite: "))
            break
        except ValueError:
            print("Ops. Seu palpite não é um número. Tente novamente.")

    if answer == user_guess:
        print("Você acertou!!! Parabéns")
        status = True
        break
    if user_guess < answer:
        ref = "baixo"
    else:
        ref = "alto"
    print("Você errou :(")
    print(f"Uma dica: Você chutou {ref} demais.\n")
    count += 1
if not status:
    print(f"O número correto era: {answer}")
    print("Mais sorte da próxima vez.")