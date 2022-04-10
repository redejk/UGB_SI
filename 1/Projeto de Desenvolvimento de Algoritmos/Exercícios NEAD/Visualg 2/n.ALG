Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Efetuar a leitura de três valores inteiros desconhecidos representados pelas variáveis A, B e C. Somar os valores fornecidos e apresentar o resultado somente se for maior ou igual a 100.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, B, C, SOMA:real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
escreval("Digite o valor de C:")
leia(C)
SOMA <- (A + B + C)
se SOMA >= 100 entao
        escreval("A soma dos valores A,B e C é igual a: ", SOMA)
fimse
Fimalgoritmo