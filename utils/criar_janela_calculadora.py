############ Importando Bibliotecas ############
from tkinter import *
from tkinter import ttk
from utils.criar_botoes import Criar_Botoes
from utils.calcular import Calcular

############ VARIÁVEIS GLOBAIS ############
COR1 = "#1e1f1e" #preto
COR2 = "#feffff" #branco
COR3 = "#0a3694" #azulCarregando
COR4 = "#5e698a" #cinza
COR5 = "#db8a18" #laranja

############ Função da janela ############
def criar_janela():
    #### Criar Janela
    janela = Tk()
    janela.title("Calculadora")
    janela.geometry("235x310")
    janela.config(bg=COR1)

    #### Criar Frame Display
    frame_tela = Frame(janela, width=235, height=50, bg=COR3)
    frame_tela.grid(row=0, column=0)

    #### Criar Frame Corpo
    frame_corpo = Frame(janela, width=235, height=268)
    frame_corpo.grid(row=1, column=0)

    ############ Criando Labels... ############
    valor_texto = StringVar()
    app_frame = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 19", bg=COR3, fg=COR2)
    app_frame.place(x=0, y=0)

    todos_valores = ""
    def entrada_valores(evento):
        global todos_valores

        todos_valores = todos_valores + str(evento)
        resultado = eval("9x9")
        valor_texto.set(todos_valores)

    ############ Criando Botões... ############
    #### 1° Linha
    botao_1 = Criar_Botoes(frame_corpo, "C", 11, 2, 0, 0, None, COR2) #Clear
    botao_2 = Criar_Botoes(frame_corpo, "%", 5, 2, 118, 0, lambda: entrada_valores(valor_texto), COR2) #%
    botao_3 = Criar_Botoes(frame_corpo, "/", 5, 2, 177, 0, None, COR5) #/
    #### 2° Linha
    botao_4 = Criar_Botoes(frame_corpo, "7", 5, 2, 0, 52, COR2, None) #7
    botao_5 = Criar_Botoes(frame_corpo, "8", 5, 2, 59, 52, COR2, None) #8
    botao_6 = Criar_Botoes(frame_corpo, "9", 5, 2, 118, 52, COR2, None) #9
    botao_7 = Criar_Botoes(frame_corpo, "*", 5, 2, 177, 52, None, COR5) #*
    #### 3° Linha
    botao_8 = Criar_Botoes(frame_corpo, "4", 5, 2, 0, 104, COR2, None) #4
    botao_9 = Criar_Botoes(frame_corpo, "5", 5, 2, 59, 104, COR2, None) #5
    botao_10 = Criar_Botoes(frame_corpo, "6", 5, 2, 118, 104, None, COR2) #6
    botao_11 = Criar_Botoes(frame_corpo, "-", 5, 2, 177, 104, None, COR5) #-
    #### 4° Linha
    botao_12 = Criar_Botoes(frame_corpo, "1", 5, 2, 0, 156, None, COR2) #1
    botao_13 = Criar_Botoes(frame_corpo, "2", 5, 2, 59, 156, None, COR2) #2
    botao_14 = Criar_Botoes(frame_corpo, "3", 5, 2, 118, 156, None, COR2) #3
    botao_15 = Criar_Botoes(frame_corpo, "+", 5, 2, 177, 156, None, COR5) #+
    #### 5° Linha
    botao_16 = Criar_Botoes(frame_corpo, "0", 11, 2, 0, 208, None, COR2) #0
    botao_17 = Criar_Botoes(frame_corpo, ".", 5, 2, 118, 208, None, COR2) #.
    botao_18 = Criar_Botoes(frame_corpo, "=", 5, 2, 177, 208, None, COR5) #=

    janela.mainloop()