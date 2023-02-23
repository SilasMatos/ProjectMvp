import tkinter as tk


class View:
    def __init__(self, presenter, janela):
        self.presenter = presenter

        # Criando os componentes da interface
        self.frame = tk.Frame(janela)
        self.frame.pack()

        self.label_peso = tk.Label(self.frame, text="Peso (kg):")
        self.label_peso.pack()

        self.entry_peso = tk.Entry(self.frame)
        self.entry_peso.pack()

        self.label_altura = tk.Label(self.frame, text="Altura (cm):")
        self.label_altura.pack()

        self.entry_altura = tk.Entry(self.frame)
        self.entry_altura.pack()

        self.button_calcular = tk.Button(
            self.frame, text="Calcular", command=self.calcular_imc)
        self.button_calcular.pack()

        self.label_resultado = tk.Label(self.frame, text="")
        self.label_resultado.pack()

    def calcular_imc(self):
        peso = float(self.entry_peso.get())
        altura = float(self.entry_altura.get())
        self.presenter.dados_informados(peso, altura)

    def exibir_resultado(self, imc):
        self.label_resultado.config(text=f"Seu IMC é {imc:.2f}")
