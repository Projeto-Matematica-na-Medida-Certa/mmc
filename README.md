# Matemática na Medida Certa (MMC)
Repositório dos códigos usados no projeto de extensão Matemática na Medida Certa, pela Universidade de São Paulo

## Sobre este repositório
Os códigos desse repositório foram feitos com o intuito de tornar conceitos relacionados ao Labirinto de Pascal mais visuais.

Foram arbodados algumas formas diferentes de análises, em sua maioria, tendo a origem ao primeiro quadrante do plano cartesiano.

## Como executar os códigos
Para executar os códigos no seu computador, será necessário instalar o Python, e executar o seguinte comando via terminal:

```
Python ./caminho/do/arquivo
```

Por exemplo, para executar o dorian, que a localização do arquivo é "./labirinto_de_pascal/caso_original/src/original-src/dorian.py", estando no diretório onde foi baixado o repositório, o comando seria:

```
Python ./labirinto_de_pascal/caso_original/src/original-src/dorian.py
```

Serão mostrados, a seguir, como funciona alguns dos programas contidos nesse repositório.

## Dorian

### Localização no repositório:
---
Versão original:

./labirinto_de_pascal/caso_original/src/original-src/dorian.py

Versão comentada: 

./labirinto_de_pascal/caso_original/src/original-src/versao-comentada-por-aluno/main.py

### Descrição
---
Este código mostra o Labirinto de Pascal na sua forma triangular. De forma análoga, podemos dizer que seria o caso onde temos uma grade com pregos e deixamos cair uma moeda no seu centro, e conforme a "moeda" cai, a sua localização, representada por uma seta, sobe um pouco.

Ele ilustra de maneira prática as densidades de probabilidades de onde teria maior propensão de cair a moeda, o que matematicamente temos como o Triângulo de Pascal.

A versão original e a comentada são o mesmo código em si, mudando apenas os comentários do código em si e a sua identação, que serviram de modelo para os demais códigos nesse repositório.

## Casos de grade
Para o caso de grade, inicialmente foi desenvolvido apenas o caso para um quadrante, em que estudaríamos as possibilidades de caminhos de alguém que estivesse partindo da origem de um plano cartesino.

## Caso 1º quadrante
### Localização no repositório:
---
Caso original:

./labirinto_de_pascal/grade/1_quadrante/main.py

Caso de teste de navegação:

./labirinto_de_pascal/grade/1_quadrante/teste-navegacao-em-grade/grade.py

### Caso original
---
Nesse caso foi estudado as possiveis rotas de alguem que partisse da origem, sendo que a cada momento poderia ser tomada qualquer direção de caminho, sendo que a cada vez que o nosso personagem fosse para uma localização na grade, a sua tragetória ficaria marcada, e abaixo dela ficaria o número de vezes que ele passou por ela.

### Caso de Teste de Navegação
--- 
Aqui o foco foi que dessa vez, o nosso personagem partisse da origem, com o objetivo de chegar do lado extremo oposto, de forma muito semelhante ao caso clásssico do labirinto de pascal, mas ao invés de caso triangular de costume, seria para um caso de grade.

Aqui, o programa se resume a desenhar a grade em si, com cada coordenada de cada ponto, e o seu respectivo número do Labirinto de Pascal.