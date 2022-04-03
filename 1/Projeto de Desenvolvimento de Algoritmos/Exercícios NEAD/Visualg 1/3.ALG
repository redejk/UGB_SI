Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Construa um algoritmo que tome como entrada um número inteiro positivo e mostre uma mensagem dizendo se este número é par ou ímpar.
// Autor(a)    : Carlos Eduardo Ferreira
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
numero:inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite um número:")
leia(numero)
se numero > 0 entao
        se numero MOD 2 = 0 entao
                escreval("O número digitado é par")
        senao
                escreval("O número digitado é ímpar")
        fimse
senao
        escreval("O número digitado não é positivo")
fimse
Fimalgoritmo