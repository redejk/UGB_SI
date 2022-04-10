Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Construa um algoritmo que, para três valores, imprima o maior e o menor deles.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, B, C, MAIOR, MENOR: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
MAIOR <- A
MENOR <- A
escreval("Digite o valor de B:")
leia(B)
se B > MAIOR entao
MAIOR <- B
fimse
se B < MENOR entao
MENOR <- B
fimse
escreval("Digite o valor de C:")
leia(C)
se C > MAIOR entao
MAIOR <- C
fimse
se C < MENOR entao
MENOR <- C
fimse
escreval("O maior valor entre A,B e C é: ", MAIOR," e o menor valor é: ", MENOR)
Fimalgoritmo