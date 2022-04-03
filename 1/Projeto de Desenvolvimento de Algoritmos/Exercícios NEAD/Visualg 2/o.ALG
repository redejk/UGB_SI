Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Ler um número inteiro qualquer e multiplicá-lo por dois. Apresentar o resultado da multiplicação somente se o resultado for maior que 30.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, MULTIPLICACAO: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
MULTIPLICACAO <- (A*2)
se MULTIPLICACAO > 30  entao
        escreval("A multiplicação do valor de A: ",A," com 2 é: ", MULTIPLICACAO)
fimse
Fimalgoritmo