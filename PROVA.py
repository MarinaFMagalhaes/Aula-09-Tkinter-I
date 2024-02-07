from tkinter import *
import tkinter as tk

def converter():
    try:
        centimetros = float(entry_centimetros.get())
        metros = centimetros / 100
        resultado_var.set(f'{centimetros} cm = {metros:.2f} metros')
    except ValueError:
        resultado_var.set('Digite um valor válido em centímetros (sem ",").')

janela = tk.Tk()
janela.title('Conversor de Centímetros >> Metros')
canvas = Canvas(janela, width= 400, height= 20)
canvas.pack()

resultado_var = tk.StringVar()

label_centimetros = tk.Label(janela, text='Centímetros:')
label_centimetros.pack()

entry_centimetros = tk.Entry(janela)
entry_centimetros.pack()

botao_converter = tk.Button(janela, text='Converter', command=converter, bg = "light green")
botao_converter.pack()

label_resultado = tk.Label(janela, textvariable=resultado_var, bg = "white")
label_resultado.pack()

janela.mainloop()