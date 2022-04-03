Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Faça um algoritmo que tome como entrada dois valores inteiros e determine se são múltiplos um do outro, ou não.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, B:inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
se (A MOD B = 0) ou (B MOD A = 0) entao
        escreval("Os valores de A e B são múltiplos")
senao
        escreval("Os valores de A e B não são múltiplos")
fimse
Fimalgoritmo