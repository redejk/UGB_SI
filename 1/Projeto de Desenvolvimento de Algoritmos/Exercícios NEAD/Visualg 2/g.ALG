Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Fazer a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D. Apresentar apenas os valores que sejam divisíveis por 2 e 3.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, B, C, D: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
escreval("Digite o valor de C:")
leia(C)
escreval("Digite o valor de D:")
leia(D)
se (A MOD 2 = 0) e (A MOD 3 = 0) entao
        escreval("O valor de A: ",A," é divisível por 2 e 3")
fimse
se (B MOD 2 = 0) e (B MOD 3 = 0) entao
        escreval("O valor de B: ",B," é divisível por 2 e 3")
fimse
se (C MOD 2 = 0) e (C MOD 3 = 0) entao
        escreval("O valor de C: ",C," é divisível por 2 e 3")
fimse
se (D MOD 2 = 0) e (D MOD 3 = 0) entao
        escreval("O valor de D: ",D," é divisível por 2 e 3")
fimse
Fimalgoritmo