import turtle

# Defina o tamanho da grade (por exemplo, 4x4)
rows = 4
cols = 4

# Inicialize o turtle
t = turtle.Turtle()
t.speed(10)
t.penup()



# Função para calcular o número de caminhos possíveis para cada ponto
def calculate_paths(rows, cols):
    # Cria uma matriz (grid) para armazenar os números de caminhos,
    # com os valores dos caminhos inicialmente sendo igual a 0
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # A primeira linha e a primeira coluna têm apenas 1 caminho (movendo-se apenas para a direita ou para baixo)
    for i in range(rows):
        grid[i][0] = 1
    for j in range(cols):
        grid[0][j] = 1
    
    # Calcula o número de caminhos para os outros pontos
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    return grid



# Função para desenhar a grade e adicionar os números de caminhos e índices
def draw_grid_and_numbers(rows, cols, grid):
    cell_size = 100  # Tamanho de cada célula da grade
    
    for i in range(rows):
        for j in range(cols):
            # Calcula a posição x e y do ponto superior esquerdo da célula
            x = j * cell_size
            y = -i * cell_size
            
            # Desenha a célula
            t.goto(x, y)
            t.pendown()
            for _ in range(4):
                t.forward(cell_size)
                t.right(90)
            t.penup()
            
            # Escreve o número de caminhos no centro da célula
            t.goto(x + cell_size/2, y - cell_size/2)
            t.write(grid[i][j], align="center", font=("Arial", 12, "normal"))
            
            # Escreve o índice ao lado do ponto superior esquerdo da célula
            index = f"({i},{j})"
            t.goto(x + cell_size/2, y - cell_size/2 - 20)
            t.write(index, align="center", font=("Arial", 8, "normal"))




# Calcular os caminhos para a grade
grid = calculate_paths(rows, cols)

# Desenhar a grade e adicionar os números de caminhos e índices
draw_grid_and_numbers(rows, cols, grid)

# Manter a janela aberta
turtle.done()
