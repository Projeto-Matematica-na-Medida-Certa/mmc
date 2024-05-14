# Código feito pelo aluno Paulo Nunes, para o caso da grade, usando o código do Prof. Dr. Ali Tahzibi como base

import turtle
import math
import random

###########

############ Declaração dos icones do mapa ############

dorian = turtle.Turtle() # Origem do caminho, podemos entender que é onde o nosso "boneco", dorian, parte
linedrawer = turtle.Turtle() # Linha estática que fica no nível das letras

#Declaração das letras, que representam os possíveis destinos dos caminhos

k = turtle.Turtle()
l = turtle.Turtle()
m = turtle.Turtle()
n = turtle.Turtle()
o = turtle.Turtle()
p = turtle.Turtle()
q = turtle.Turtle()
r = turtle.Turtle()
s = turtle.Turtle()
t = turtle.Turtle()
u = turtle.Turtle()
j = turtle.Turtle()
i = turtle.Turtle()
h = turtle.Turtle()
g = turtle.Turtle()
f = turtle.Turtle()
e = turtle.Turtle()
d = turtle.Turtle()
c = turtle.Turtle()
b = turtle.Turtle()
a = turtle.Turtle()

v = turtle.Turtle()
w = turtle.Turtle()
x = turtle.Turtle()
y = turtle.Turtle()


########################

t.speed(0)

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

a.penup(), a.goto(-200,  200), a.left(90), a.pendown()
b.penup(), b.goto(-100,  200), b.left(90), b.pendown()
c.penup(), c.goto(   0,  200), c.left(90), c.pendown()
d.penup(), d.goto( 100,  200), d.left(90), d.pendown()
e.penup(), e.goto( 200,  200), e.left(90), e.pendown()

f.penup(), f.goto(-200, 100), f.left(90), f.pendown()
g.penup(), g.goto(-100, 100), g.left(90), g.pendown()
h.penup(), h.goto(   0, 100), h.left(90), h.pendown()
i.penup(), i.goto( 100, 100), i.left(90), i.pendown()
j.penup(), j.goto( 200, 100), j.left(90), j.pendown()

k.penup(), k.goto(-200,    0), k.left(90), k.pendown()
l.penup(), l.goto(-100,    0), l.left(90), l.pendown()
m.penup(), m.goto(   0,    0), m.left(90), m.pendown() #Origem
n.penup(), n.goto( 100,    0), n.left(90), n.pendown()
o.penup(), o.goto( 200,    0), o.left(90), o.pendown()

p.penup(), p.goto(-200, -100), p.left(90), p.pendown()
q.penup(), q.goto(-100, -100), q.left(90), q.pendown()
r.penup(), r.goto(   0, -100), r.left(90), r.pendown()
s.penup(), s.goto( 100, -100), s.left(90), s.pendown()
t.penup(), t.goto( 200, -100), t.left(90), t.pendown()

u.penup(), u.goto(-200, -200), u.left(90), u.pendown()
v.penup(), v.goto(-100, -200), v.left(90), v.pendown()
w.penup(), w.goto(   0, -200), w.left(90), w.pendown()
x.penup(), x.goto( 100, -200), x.left(90), x.pendown()
y.penup(), y.goto( 200, -200), y.left(90), y.pendown()





####### INÍCIO - Controle do caminho de dorian #######

for i_ in range(0, 200):
  
  x = 0 # x e y iniciais de dorian
  y = 150 

  for j_ in range(0, 20):
   
   dorian.penup()
   dorian.goto(x,y) #Seta a posição inicial de dorian no inicio de cada partida

   coin=random.randint(0,100) #coin: valor aleatório entre 0 a 100 que será comparado com o valor de rand
   if coin > rand:
    x += 10
    y -= 10
    dorian.pendown(), dorian.speed(0), dorian.color("red"), dorian.goto(x,y)
    #t.clear()
   else:
    x -= 10
    y -= 10
    dorian.pendown(), dorian.speed(0), dorian.color("blue"), dorian.goto(x,y)

  dorian.clear()

  # Registrando em qual letra dorian chegou
  if x==0:
    k.forward(5)
  elif x==20:
    l.forward(5)
  elif x==40:
    m.forward(5)
  elif x==60:
    n.forward(5)  
  elif x==80:
    o.forward(5)  
  elif x==100:
    p.forward(5)  
  elif x==120:
    q.forward(5)  
  elif x==140:
    r.forward(5)  
  elif x==160:
    s.forward(5)  
  elif x==180:
    t.forward(5)  
  elif x==200:
    u.forward(5)  
  elif x==-20:
    j.forward(5)  
  elif x==-40:
    i.forward(5)  
  elif x==-60:
    h.forward(5)  
  elif x==-80:
    g.forward(5)  
  elif x==-100:
    f.forward(5)  
  elif x==-120:
    e.forward(5)  
  elif x==-140:
    d.forward(5)     
  elif x==-160:
    c.forward(5)
  elif x==-180:
    b.forward(5)
  elif x==-200:
    a.forward(5)

####### FIM - Controle do caminho de dorian #######

turtle.done() # Fim da animação
      
     