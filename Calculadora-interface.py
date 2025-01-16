import tkinter as tk

# setup
def adicionar_numero(num):
    lcd.insert(tk.END, str(num))

def clear():
    lcd.delete(1.0, tk.END)

def verificar_texto():
    try:
        #scanner 2.0 KKKKK
        resultado = eval(lcd.get("1.0", tk.END).strip())
        clear()
        lcd.insert(tk.END, resultado)
    except Exception as e:
        clear()
        lcd.insert(tk.END, "Erro")
        
        
def adicao():
    lcd.insert(tk.END, "+")
def subtracao():
	    lcd.insert(tk.END, "-")
def divisao():
	    lcd.insert(tk.END, "/")
def multiplicacao():
	    lcd.insert(tk.END, "*")


# ajustes
tela = tk.Tk()
tela.geometry("400x640")
tela.title("Calculadora")
tela.config(bg="black")

# LCD
lcd = tk.Text(tela, height="5", width="30")
lcd.pack(pady=30)

#botao do bgl
for i in range(1, 10):
    button = tk.Button(tela, text=str(i), command=lambda i=i: adicionar_numero(i))
    button.pack(pady=10)
    button.place(x=(i % 3) * 100 + 150, y=(i // 3) * 100 + 300)
    
button0 = tk.Button(tela, text="0", command=lambda: adicionar_numero(0))
button0.pack(pady=10)
button0.place(x=150, y=500)

# clear
button_clear = tk.Button(tela, text="C", command=clear)
button_clear.pack(pady=10)
button_clear.place(x=250, y=500)


# operadores
adicao = tk.Button(tela, text="+", command=adicao)
adicao.pack(pady=10)
adicao.place(x=350, y=500)


subtracao = tk.Button(tela, text="-", command=subtracao)
subtracao.pack(pady=10)
subtracao.place(x=150,y=300)


divisao = tk.Button(tela, text="÷", command=divisao)
divisao.pack(pady=10)
divisao.place(x=450,y=300)

multiplicacao = tk.Button(tela, text="×", command=multiplicacao)
multiplicacao.pack(pady=10)
multiplicacao.place(x=450,y=400)


calcular = tk.Button(tela, text="=", command=verificar_texto)
calcular.pack(pady=10)
calcular.place(x=450, y=500)

# Iniciar a aplicação
tela.mainloop()
