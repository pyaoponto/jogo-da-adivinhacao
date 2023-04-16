import graphviz


class NoArvore:
    def __init__(self, dados):
        self.dados = dados
        self.esquerda = None
        self.direita = None


def pergunta_sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (sim/nao): ").lower()
        if resposta in ['sim', 's', 'nao', 'n']:
            return resposta.startswith('s')


def visualizar_arvore(no):
    def adicionar_nos_arestas(no, dot=None):
        if dot is None:
            dot = graphviz.Digraph()
            dot.node(name=str(no), label=no.dados)

        for child in [no.esquerda, no.direita]:
            if child is not None:
                dot.node(name=str(child), label=child.dados)
                dot.edge(str(no), str(child))
                adicionar_nos_arestas(child, dot=dot)

        return dot

    dot = adicionar_nos_arestas(no)
    dot.render('arvore', format='png', cleanup=True)
    return dot


def jogo_adivinhacao_animal():
    raiz = NoArvore("É um mamífero?")
    raiz.esquerda = NoArvore("Tem listras?")
    raiz.esquerda.esquerda = NoArvore("zebra")
    raiz.esquerda.direita = NoArvore("cavalo")
    raiz.direita = NoArvore("Tem pescoço longo?")
    raiz.direita.esquerda = NoArvore("girafa")
    raiz.direita.direita = NoArvore("avestruz")

    while True:
        arvore_visualizada = visualizar_arvore(raiz)
        if arvore_visualizada: print("arvore.png gerado com sucesso!\n")

        print("\nPense em um animal e tentarei adivinhar!")
        no = raiz
        while no.esquerda and no.direita:
            if pergunta_sim_nao(no.dados):
                no = no.direita
            else:
                no = no.esquerda

        animal_adivinhado = no.dados
        print(f"O seu animal é um {animal_adivinhado}?")
        if pergunta_sim_nao("Acertei?"):
            print("Viva! Eu adivinhei!")
        else:
            novo_animal = input("Qual era o animal em que estava pensando? ").lower()
            nova_pergunta = input(
                f"Por favor, insira uma pergunta que distingue um {novo_animal} de um {animal_adivinhado}: ")

            no.dados = nova_pergunta
            if pergunta_sim_nao(f"A resposta é 'sim' para um {novo_animal}?"):
                no.esquerda = NoArvore(animal_adivinhado)
                no.direita = NoArvore(novo_animal)
            else:
                no.esquerda = NoArvore(novo_animal)
                no.direita = NoArvore(animal_adivinhado)

        if not pergunta_sim_nao("Deseja jogar novamente?"):
            break

if __name__ == "__main__":
    jogo_adivinhacao_animal()

