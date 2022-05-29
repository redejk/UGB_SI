Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/05/2022
Var
// Seção de Declarações das variáveis 
res, num1, num2: inteiro
divisao: real
subtracao: inteiro
inicio
escreval("Digite o valor do numero 1: ")
leia(num1)
escreval("Digite o valor de numero 2: ")
leia(num2)
procedimento soma(n,m:inteiro)
             var
                aux: inteiro
             inicio
                   aux <- n + m
                   res <- aux
fimprocedimento
soma(num1,num2)
escreval("SOMA")
escreval(res)

funcao divide(n1, n2:inteiro): real
       var
          resto: inteiro
       inicio
             resto <- n1 % n2
             retorne n1 / n2
fimfuncao

funcao subtrai(x, y:inteiro) :inteiro
       inicio
             retorne x - y
fimfuncao

divisao <- divide(num1, num2)
escreval("DIVISAO")
escreval(divisao)

subtracao <- subtrai(num1, num2)
escreval("SUBTRACAO")
escreval(subtracao)

Fimalgoritmo