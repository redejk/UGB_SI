Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Ler cinco valores numéricos inteiros (variáveis A, B, C, D e F), identificar e apresentar o maior e o menor valores informados. Não execute a ordenação dos valores como no exercício "f".
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, B, C, D, F, MAIOR, MENOR: inteiro
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
escreval("Digite o valor de D:")
leia(D)
se D > MAIOR entao
        MAIOR <- D
fimse
se D < MENOR entao
        MENOR <- D
fimse
escreval("Digite o valor de F:")
leia(F)
se F > MAIOR entao
        MAIOR <- F
fimse
se F < MENOR entao
        MENOR <- F
fimse
escreval("O maior valor digitado é: ", MAIOR," e o menor: ", MENOR)
Fimalgoritmo