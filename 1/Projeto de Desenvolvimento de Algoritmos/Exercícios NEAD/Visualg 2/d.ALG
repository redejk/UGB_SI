Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Ler os valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD1) desse aluno e apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 7; caso contrário, o programa deve solicitar a quinta nota (nota de exame, representada pela variável NE) do aluno e calcular uma nova média aritmética (variável MD2) entre a nota de exame e a primeira média aritmética. Se o valor da nova média for maior ou igual a cinco, apresentar a mensagem "Aprovado em exame"; caso contrário, apresentar a mensagem "Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
N1, N2, N3, N4, NE, MD1, MD2: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor da nota 1:")
leia(N1)
escreval("Digite o valor da nota 2:")
leia(N2)
escreval("Digite o valor da nota 3:")
leia(N3)
escreval("Digite o valor da nota 4:")
leia(N4)
MD1 <- (N1 + N2 +N3 +N4) / 4
se MD1 >= 7.00 entao
        escreval("Aprovado com média: ", MD1)
senao
        escreval("Reprovado com média: ", MD1, " Digite a nota de exame: ")
        leia(NE)
        MD2 <- (NE + MD1) / 2
        se MD2 >= 5.00 entao
                escreval("Aprovado com média: ", MD2)
        senao
                escreval("Reprovado com média: ", MD2)
        fimse
fimse
Fimalgoritmo