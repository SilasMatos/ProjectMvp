import tkinter as tk
from view_mvp import View
from presenter_mvp import Presenter
from model_mvp import Model
if __name__ == '__main__':
    janela = tk.Tk()
    janela.title("Cálculo do Índice de Massa Corporal (IMC)")
    apresentador = Presenter(janela)
    janela.mainloop()
