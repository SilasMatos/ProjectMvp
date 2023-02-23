from model_mvp import Model
from view_mvp import View


class Presenter:
    def __init__(self, janela):
        self.modelo = None
        self.visao = View(self, janela)

    def dados_informados(self, peso, altura):
        self.modelo = Model(peso, altura)
        imc = self.modelo.calcular_imc()
        self.visao.exibir_resultado(imc)
