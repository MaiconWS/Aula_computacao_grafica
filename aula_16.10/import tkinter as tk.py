import tkinter as tk
from tkinter import simpledialog, messagebox

def desenhar_eixos(canvas):
    #Eixo y
    canvas.create_line(300,0,300,600)

    #Eixo X
    canvas.create_line(0,300,600,300)

    for i in range(0, 601, 50):
        canvas.create_line(i, 295, i, 305)
        canvas.create_line(295, i, 305,i)

        if i != 300:
            canvas.create_line(i, 0, i, 600, fill="gray", dash=(2,2))
            canvas.create_line(0, i, 600,i, fill="gray", dash=(2,2))

def desenhar_linha(canvas):
    p1_x = simpledialog.askfloat("Ponto P1","Coordenada x de P1:")
    p1_y = simpledialog.askfloat("Ponto P1", "Coordenada Y de P1:")

    p2_x = simpledialog.askfloat("Ponto P2","Coordenada x de P2:")
    p2_y = simpledialog.askfloat("Ponto P2", "Coordenada Y de P2:")

    if None in [p1_x,p1_y,p2_x,p2_y]:
        messagebox.showwarning("Aviso", "Coordenadas incompletas!")
        return
    
    canvas.create_line(300 + p1_x, 300 - p1_y, 300 + p2_x, 300 - p2_y, fill="blue")
def main():
    root = tk.Tk()
    root.title("Plano Cartessiano com Função de Desenho")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack()

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    draw_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Desenhar", menu=draw_menu)
    draw_menu.add_command(label="Linha", command=lambda: desenhar_linha(canvas))

    desenhar_eixos(canvas)

    root.mainloop()

if __name__== "__main__":
    main()