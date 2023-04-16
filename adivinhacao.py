class NoArvore:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

def pergunta_sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (sim/nao): ").lower()
        if resposta in ['sim', 's', 'nao', 'n']:
            return resposta.startswith('s')

def jogo_adivinhacao_animal():
    raiz = NoArvore("É um mamífero?")
    raiz.esquerda = NoArvore("Tem listras?")
    raiz.esquerda.esquerda = NoArvore("zebra")
    raiz.esquerda.direita = NoArvore("cavalo")
    raiz.direita = NoArvore("Tem um pescoço longo?")
    raiz.direita.esquerda = NoArvore("girafa")
    raiz.direita.direita = NoArvore("avestruz")

    while True:
        print("\nPense em um animal e tentarei adivinhar!")
        no = raiz
        while no.esquerda and no.direita:
            if pergunta_sim_nao(no.dado):
                no = no.direita
            else:
                no = no.esquerda

        animal_adivinhado = no.dado
        print(f"O seu animal é um(a) {animal_adivinhado}?")
        if pergunta_sim_nao("Acertei?"):
            print("Oba! Eu adivinhei!")
        else:
            novo_animal = input("Qual era o animal que você estava pensando? ").lower()
            nova_pergunta = input(f"Digite uma pergunta que diferencia um(a) {novo_animal} de um(a) {animal_adivinhado}: ")

            no.dado = nova_pergunta
            if pergunta_sim_nao(f"A resposta é 'sim' para um(a) {novo_animal}?"):
                no.esquerda = NoArvore(animal_adivinhado)
                no.direita = NoArvore(novo_animal)
            else:
                no.esquerda = NoArvore(novo_animal)
                no.direita = NoArvore(animal_adivinhado)

        if not pergunta_sim_nao("Quer jogar novamente?"):
            break

if __name__ == "__main__":
    jogo_adivinhacao_animal()
