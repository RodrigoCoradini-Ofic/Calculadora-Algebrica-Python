############ Importando Bibliotecas ############
from tkinter import *
from tkinter import ttk

############ VARIÁVEIS GLOBAIS ############
COR1 = "#feffff" #branco
FONTE = "Ivy 13 bold"

############ Função Criar Botões ############
def Criar_Botoes(frame, 
                texto, 
                width,
                height, 
                x, 
                y,
                comando,
                cor_fundo=COR1
            ):
    
    botão = Button(frame, 
                text=texto, 
                width=width, 
                height=height, 
                bg=cor_fundo,
                command=comando
                font=FONTE,
                relief=RAISED,
                overrelief=RIDGE
                )
    botão.place(x=x, y=y)