import tkinter as tk
from tkinter import *
from time import sleep
import random
import string

#clear
def clear():
	   text_widget.delete(1.0,tk.END)
#creditos
def credits():
	   clear()
	   text_widget.insert(tk.END, "Olá, este projeto foi desenvolvido por: 'gabri2012mi@gmail.com'")
#gerador de letra
def gerar():
     letra = random.choice(string.ascii_letters)
     return letra
letra1 = gerar()
#onclick
def onclick():
	  text_widget.insert(tk.END, letra1)
#size font
tamanho_fonte = 12
def aumentar_tamanho():
	   global tamanho_fonte
	   tamanho_fonte += 2
	   label.config(font=("Arial", tamanho_fonte)) 
def diminuir_tamanho():
	   global tamanho_fonte
	   tamanho_fonte -= 2
	   label.config(font=("Arial",tamanho_fonte))
def rgb():
	   rgb = ['red', 'green', 'blue']
	   selector = random.choice(rgb)
def select_color():
	   cores = ['black','pink','red','white']
	   tela.config(bg=random.choice(cores))
#set up
tela = tk.Tk()
tela.title('interface grafica')
tela.config(bg='gray30')
tela.geometry('400x640')
#labels
label = tk.Label(tela, text='Tamanho da fonte')
label.pack(pady=10)
label2 = tk.Label(tela,text=" INTERFACE GRÁFICA ", font=("Arial",tamanho_fonte))
label2.config(bg='red')
label2.pack(pady=50)
#buttons
btn1 = tk.Button(tela, text="Botão", command=onclick)
btn1.pack(pady=10)
btn2 = tk.Button(tela, text="Aumentar tamanho font", command=aumentar_tamanho)
btn2.pack(pady=10)
btn3 = tk.Button(tela, text="Diminuir tamanho font", command=diminuir_tamanho)
btn3.pack(pady=10)
btn4 = tk.Button(tela,text="Limpar(input)",command=clear)
btn4.pack(pady=10)
select = tk.Button(tela,text="Mudar cor da tela",command=select_color)
select.pack(pady=10)
creditos = tk.Button(tela,text="Creditos",command=credits)
creditos.pack(pady=10)
creditos.config(bg='blue')
#texts
text_widget = tk.Text(tela, height=10, width=40)
text_widget.pack(pady=10)
#end
tela.mainloop()