Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/03/2022
Var
// Seção de Declarações das variáveis 
idade:inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite sua idade para saber se você deve votar nessa eleição.")
leia(idade)
se (idade >= 18) e (idade <=60) entao
   escreval("O voto é obrigatório!")
senao
     se (idade >=16)  e (idade <=17) entao
        escreval("O voto é opcional.")
     senao
     fimse
          se idade < 16 entao
             escreval("Não é permitido votar!")
          senao
          fimse
               se idade >=61 entao
               escreval("O voto não é mais obrigatório.")
               fimse
fimse
Fimalgoritmo