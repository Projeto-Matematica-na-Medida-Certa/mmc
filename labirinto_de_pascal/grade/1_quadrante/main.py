# Código feito pelo aluno Paulo Nunes, para o caso da grade, usando o código do Prof. Dr. Ali Tahzibi como base

import turtle
import math
import random

###########

############ INÍCIO - Declaração dos icones do mapa ############

dorian = turtle.Turtle() # Origem do caminho, podemos entender que é onde o nosso "boneco", dorian, parte
linedrawer = turtle.Turtle() # Linha estática que fica no nível das letras

#Declaração das letras, que representam os possíveis destinos dos caminhos

t = turtle.Turtle() # Abreviação do turtle.Turtle()

c  = turtle.Turtle()
caminho_c = 0

d  = turtle.Turtle()
caminho_d = 0

e  = turtle.Turtle()
caminho_e = 0

h  = turtle.Turtle()
caminho_h = 0

i  = turtle.Turtle()
caminho_i = 0

j  = turtle.Turtle()
caminho_j = 0

m  = turtle.Turtle()
caminho_m = 0 #Origem

n  = turtle.Turtle()
caminho_n = 0

o  = turtle.Turtle()
caminho_o = 0



############ FIM - Declaração dos icones do mapa ############

m.speed(0) # Setado na origem

dorian.hideturtle(), linedrawer.hideturtle() # "Esconder" inicialmente o boneco enquanto ele não é devidamente setado no mapa

pi = math.pi

##########################################

# Fator que define onde se concentrará a densidade de probalilidade dos caminhos pecorridos por doriam.
# O fator rand será comparado com o valor de "coin", que será constantemente setado como uma
# variável aleatória entre 0 a 100, de foma que:
#
# 0  <= rand <  50  -> dorian tende a ir para a direita
# 50 <  rand <= 100 -> dorian tende a ir para a esquerda
#       rand =  50  -> dorian tende a ir pelo o meio
#
# Observação: Com "tendência", leia-se por: Há uma maior probabilidade de os caminhos se orientem para esse sentido

rand = 50

##########################################

linedrawer.speed(0)
# linedrawer.penup(), linedrawer.goto(-200,-50), linedrawer.pendown(), linedrawer.forward(400) #Linha estática

# Animação, onde cada letra parte de um mesmo ponto, e vai em direção ao seu local no mapa

c.penup(),  c.goto(   0,  200),  c.left(90),  c.pendown()
d.penup(),  d.goto( 100,  200),  d.left(90),  d.pendown()
e.penup(),  e.goto( 200,  200),  e.left(90),  e.pendown()

h.penup(),  h.goto(   0,  100),  h.left(90),  h.pendown()
i.penup(),  i.goto( 100,  100),  i.left(90),  i.pendown()
j.penup(),  j.goto( 200,  100),  j.left(90),  j.pendown()

m.penup(),  m.goto(   0,    0),  m.left(90),  m.pendown() #Origem
n.penup(),  n.goto( 100,    0),  n.left(90),  n.pendown()
o.penup(),  o.goto( 200,    0),  o.left(90),  o.pendown()






####### INÍCIO - Controle do caminho de dorian #######

x = 0
y = 0
for ciclos in range (1, 100):

    dorian.penup()
    dorian.goto(x,y) #Seta a posição inicial de dorian no inicio de cada partida

    coin = random.randint(0,100) #coin: valor aleatório entre 0 a 100 que será comparado com o valor de rand
    if coin > rand:
        x += 100
        dorian.pendown(), dorian.speed(6), dorian.color("red"), dorian.goto(x,y)
    else:
        y += 100
        dorian.pendown(), dorian.speed(6), dorian.color("blue"), dorian.goto(x,y)


    # Registrando em qual letra dorian chegou

    if   x ==    0 and y ==    0: # m
        # m.forward(5)
        caminho_m += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_m, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        
    elif x ==  100 and y ==    0: # n
        # n.forward(5)
        caminho_n += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_n, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        
    elif x ==  200 and y ==    0: # o
        # o.forward(5)
        caminho_o += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_o, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        

    elif x ==    0 and y ==  100: # h
        # h.forward(5)
        caminho_h += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_h, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        
    elif x ==  100 and y ==  100: # i
        # i.forward(5)
        caminho_i += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_i, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        
    elif x ==  200 and y ==  100: # j
        # j.forward(5)
        caminho_j += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_j, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        

    elif x ==    0 and y ==  200: # c
        # c.forward(5)
        caminho_c += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_c, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        
    elif x ==  100 and y ==  200: # d
        # d.forward(5)
        caminho_d += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_d, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        
    elif x ==  200 and y ==  200: # e
        # e.forward(5)
        caminho_e += 1
        t.pendown()
        t.goto (x, y - 50)
        t.write (caminho_e, align = "center", font = ("Arial", 12, "normal"))
        t.penup()
        
    

    if x == 200 or y == 200: # Se chegar no limite da grade, reinicia
        x = 0
        y = 0
        dorian.clear()

####### FIM - Controle do caminho de dorian #######

turtle.done() # Fim da animação
      
     