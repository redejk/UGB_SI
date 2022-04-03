Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Efetuar a leitura de três valores numéricos (representados pelas variáveis A, B e C) e processar o cálculo da equação completa de segundo grau, utilizando a fórmula de Bhaskara (considerar para a solução do problema todas as possíveis condições para delta: delta < 0 – não há solução real, delta > 0 – há duas soluções reais e diferentes e delta = 0 – há apenas uma solução real). Lembre- -se de que é completa a equação de segundo grau que possui todos os coeficientes A, B e C diferentes de zero. O programa deve apresentar respostas para todas as condições estabelecidas para delta.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, B, C, DELTA, X1, X2: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
escreval("Digite o valor de C:")
leia(C)
DELTA <- ((B*B) - 4*A*C)
se DELTA < 0 entao
        escreval("Não há solução real")
senao
        se DELTA = 0 entao
                X1 <- -B / (2*A)
                escreval("Há apenas uma solução real, X: ",X1)
        senao
                X1 <- (-B + RAIZQ(DELTA)) / (2*A)
                X2 <- (-B - RAIZQ(DELTA)) / (2*A)
                escreval("Há duas soluções reais e diferentes: X1: ",X1," X2: ", X2)
        fimse
fimse
Fimalgoritmo