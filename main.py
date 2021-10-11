class Probabilidade:
    def __init__(self):
        # definindo as variáves
        self.probabilidades = []
        self.quantidade_pessoas = []

        # pedir a entrada do usuário
        self.porcentagem_desejada = self.pedir_porcentagem()

        self.insere_probabilidades()  # insere as prob. no list, que vai ser usado para retornar a quantidade de pessoas

        # parte responsável pelos calculos
        # além de realizar o calculo de quantas pessoas necessárias, adicionando ao list
        # vai retornar a porcentagem aproximada da desejada pelo usuario
        self.porcentagem = self.calcula_quantidade()

        self.imprime_resultado()  # retorna o resultado

    @staticmethod
    def pedir_porcentagem():
        porcentagem_entrada = float(input('Insira a porcentagem desejada (%): '))
        porcentagem_esperada = 1 - (porcentagem_entrada / 100)
        return porcentagem_esperada

    def insere_probabilidades(self):
        for dia in range(0, 366):
            probabilidade = (365-dia)/365
            self.probabilidades.append(probabilidade)

    def calcula_quantidade(self):
        porcentagem = 1

        for each in self.probabilidades:
            if porcentagem > self.porcentagem_desejada:
                porcentagem *= each
                self.quantidade_pessoas.append(each)

        porcentagem = (1 - porcentagem) * 100
        return porcentagem

    def imprime_resultado(self):
        print(f'Porcentagem aproximada: {self.porcentagem:.2f}%.\n'
              f'Pessoas necessárias: {len(self.quantidade_pessoas)}.')


Probabilidade()
