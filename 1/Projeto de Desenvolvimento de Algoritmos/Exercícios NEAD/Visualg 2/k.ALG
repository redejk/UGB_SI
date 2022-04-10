Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Efetuar a leitura de um valor numérico inteiro que esteja na faixa de valores de 1 até 9. O programa deve apresentar a mensagem "O valor está na faixa permitida", caso o valor informado esteja entre 1 e 9. Se o valor estiver fora da faixa, o programa deve apresentar a mensagem "O valor está fora da faixa permitida".
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
se (A >= 1) e (A <= 9) entao
        escreval("O valor está na faixa permitida")
senao
        escreval("O valor está fora da faixa permitida")
fimse
Fimalgoritmo