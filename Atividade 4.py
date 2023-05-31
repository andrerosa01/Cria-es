import tkinter as tk

calculo = str()

def inserir_texto(x):
    global calculo
    calculo = calculo + x
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def avaliar():
    global calculo
    a = str(eval(texto.get(1.0, "end")))
    calculo = str()
    inserir_texto(a)

def apagar():
    global calculo
    calculo = str()
    texto.delete(1.0, "end")

def calcular_potencia():
    global calculo
    calculo += "**"
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def calcular_raiz():
    global calculo
    calculo = "sqrt(" + calculo + ")"
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def calcular_inverso():
    global calculo
    calculo = "1/(" + calculo + ")"
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

janela = tk.Tk()

texto = tk.Text(janela, height=4, width=26, font=("Arial", 24))
texto.grid(columnspan=5)

botao1 = tk.Button(janela, text="1", command=lambda: inserir_texto("1"), width=13, height=4, font=("Arial", 12))
botao1.grid(column=1, row=2)

botao_potencia = tk.Button(janela, text="^", command=calcular_potencia, width=13, height=4, font=("Arial", 12))
botao_potencia.grid(column=1, row=5)
botao_raiz = tk.Button(janela, text="√", command=calcular_raiz, width=13, height=4, font=("Arial", 12))
botao_raiz.grid(column=2, row=5)
botao_inverso = tk.Button(janela, text="1/x", command=calcular_inverso, width=13, height=4, font=("Arial", 12))
botao_inverso.grid(column=3, row=5)