import turtle

# método screen para mostrar tela
tela = turtle.Screen()
tela.bgcolor('light pink')

# criando objeto pincel
pincel = turtle.Turtle()


def triangulo(x, y):
    # função para desenhar a caneta
    pincel.penup()

    # função para mover o cursor
    # na posição x em y
    pincel.goto(x, y)

    # função para  desenhar
    pincel.pendown()
    for i in range(3):

        # mover o cursor
        # em 100 unidades
        pincel.forward(100)

        # gira o cursor
        # para esquerda em 120 graus
        pincel.left(120)

        # mover o cursor
        # em 100 unidades
        pincel.forward(100)

# Chamada da função turtle screen
turtle.onscreenclick(triangulo, 1)

# Chamada para começar
turtle.listen()

# Pausar o screen
turtle.done()
