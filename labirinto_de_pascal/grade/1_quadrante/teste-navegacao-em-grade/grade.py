import turtle

# Definição do tamanho da grade
linhas  = 4
colunas = 4 

# Inicializar o turtle
t = turtle.Turtle()
t.speed(10) # Velocidade
t.penup()


# Função para calular o número de caminhos possíveis (Labirinto de Pascal)

def calcula_caminho (linhas, colunas):

    # Coloca os valores iniciais dos caminhos sendo iguais a 0
    grade = [ [0 for _ in range(colunas)] for _ in range(linhas) ]

    # Coloca como valores da primeira linha e coluna como 1
    for i in range (linhas):
        grade [i][0] = 1
    for i in range (colunas):
        grade [0][i] = 1

    # Cálculo do numero de caminhos para os demais pontos da grade
    for i in range (1, linhas):
        for j in range (1, colunas):
            grade [i][j] = grade [i - 1][j] + grade [i][j - 1]
    
    return grade


# Função que desenha a grade e coloca os caminhos e índices na tela
def desenha_grade (grade, linhas, colunas):
    tamanho_da_celula = 100 # Tamanho de cada espaço da grade

    for j in range (linhas):
        for i in range (colunas):

            # Cálculo da posição, em relação ao canto superior esquerdo da célula
            x = i * tamanho_da_celula
            y = j * tamanho_da_celula

            # Desenha a célula
            t.goto (x, y)
            t.pendown()
            for _ in range (4):
                t.forward(tamanho_da_celula)
                t.right(90)
            t.penup()

            # Escreve o número de caminhos na célula
            t.goto (x + tamanho_da_celula/2, y - tamanho_da_celula/2)
            t.write (grade [i][j], align = "center", font = ("Arial", 12, "normal"))

            # Escreve o índice ao lado do ponto superior esquerdo da célula
            index = f"({i}, {j})"
            t.goto ( x + tamanho_da_celula/2, y - tamanho_da_celula/2 - 20)
            t.write (index , align = "center", font = ("Arial", 8, "normal"))

##### INÍCIO DA MAIN #####

# Calcular caminhos da grade
grade = calcula_caminho (linhas, colunas)

# Desenhar a grade com o número de caminhos e índices de cada célula
desenha_grade (grade, linhas, colunas)

# Manter a janela aberta
turtle.done()