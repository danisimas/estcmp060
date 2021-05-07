# Exercicio um
# Python programa de linhas de uma sequência Fibonacci
# Espiral desenhada usando Turtle
import turtle
import math


# Função principal do desenho do Fibonacci
def fiboPlot(n):
    a = 0
    b = 1
    quadrado_a = a
    quadrado_b = b

    # Configurar a cor do pincel 
    x.pencolor("pink")

    # Desenhar o primeiro quadrado
    x.forward(b*factor)
    x.left(90)
    x.forward(b*factor)
    x.left(90)
    x.forward(b*factor)
    x.left(90)
    x.forward(b*factor)

    # Procedimento para fazer a serie Fibonacci
    aux = quadrado_b
    quadrado_b = quadrado_b + quadrado_a
    quadrado_a = aux 

    # Desenhando o resto do quadrados
    for i in range(1, n):
        x.backward(quadrado_a * factor)
        x.right(90)
        x.forward(quadrado_b * factor)
        x.left(90)
        x.forward(quadrado_b * factor)
        x.left(90)
        x.forward(quadrado_b * factor)

        # Procedimento para serie Fibonacci
        aux = quadrado_b
        quadrado_b = quadrado_b + quadrado_a
        quadrado_a = aux

    # Movendo para o ponto inicial a caneta 
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Escolhendo a cor da caneta
    x.pencolor("blue")

    # Espiral de Fibonacci 
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * (b*factor/2)
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        aux = a
        a = b
        b = aux + b


# O factor significa o multiplicativo
# Do qual aumentar o tamanho das linhas
factor = 5

# Insira um número para 
# Interagir com o código 
num = int(input("Entre com um número para interações (maior que > 1): "))

# As linhas da espiral do Fibonacci
# Elas serão desenhadas de acordo
# com o número inserido
if num > 0:
    print("Série de Fibonacci de", num, "elementos :")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(num)
    turtle.done()
else:
    print("Número tem que ser maior que > 0")
