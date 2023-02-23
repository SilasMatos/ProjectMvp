class Model:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        altura_metros = self.altura / 100
        return self.peso / (altura_metros ** 2)
