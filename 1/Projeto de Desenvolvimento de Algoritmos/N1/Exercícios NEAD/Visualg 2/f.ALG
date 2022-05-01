Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Ler três valores inteiros representados pelas variáveis A, B e C e apresentar os valores lidos dispostos em ordem crescente. Dica: utilizar tomada de decisão sequencial e as ideias trabalhadas nos exercícios "g" (propriedade distributiva) e "f" (troca de valores) do capítulo 3.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A, B, C: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
escreval("Digite o valor de C:")
leia(C)
se (A<B) entao
        se (B<C) entao
                escreval("A: ",A)
                escreval("B: ",B)
                escreval("C: ",C)
        senao
                se (A<C) entao
                        escreval("A: ",A)
                        escreval("C: ",C)
                        escreval("B: ",B)
                senao
                        escreval("C: ",C)
                        escreval("A: ",A)
                        escreval("B: ",B)
                fimse
        fimse
senao
        se (B<C) entao
                se (A<C) entao
                        escreval("B: ",B)
                        escreval("A: ",A)
                        escreval("C: ",C)
                senao
                        escreval("B: ",B)
                        escreval("C: ",C)
                        escreval("A: ",A)
                fimse
        senao
                escreval("C: ",C)
                escreval("B: ",B)
                escreval("A: ",A)
        fimse
fimse
Fimalgoritmo