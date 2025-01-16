import tkinter as tk

def desenhar_linha():
    # Limpa o canvas
    canvas.delete("all")
    # Desenha uma linha com a largura especificada
    canvas.create_line(50, 50, 200, 200, fill="blue", width=linha_largura)

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Linha no Tkinter")

# Cria um canvas
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Define a largura da linha
linha_largura = 5  # Altere este valor para aumentar ou diminuir a finura da linha

# Botão para desenhar a linha
botao = tk.Button(root, text="Desenhar Linha", command=desenhar_linha)
botao.pack()

# Inicia o loop principal
root.mainloop()