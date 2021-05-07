# importação
import turtle
from turtle import *

# Função para
# inicializar a velocidade
# Para 100
speed('fastest')

# Colocando o ponteiro para cima
rt(-90)

# O angulo pra formação da arvore
angulo = 30

# Função para inicar o Y
def y(tamanho, nivel):

    if nivel > 0:
        colormode(255)
        # Função para o intervalo
        # Rgb para verde
        # Definindo também a cor
        # para o nivel atual
        pencolor(0, 255//nivel, 0)

        # Função para desenhar
        # a base
        fd(tamanho)

        # Função para girar o cursor
        rt(angulo)

        # Função recursiva
        y(0.8 * tamanho, nivel-1)

        pencolor(0, 255//nivel, 0)

        # Função para girar o cursor
        lt(2 * angulo)

        # Função recursiva
        y(0.8 * tamanho, nivel-1)

        pencolor(0, 255//nivel, 0)

        rt(angulo)
        fd(-tamanho)

# Chamada principal da função
y(80, 15)

# Pausa quando acabar
# o programa
turtle.done()