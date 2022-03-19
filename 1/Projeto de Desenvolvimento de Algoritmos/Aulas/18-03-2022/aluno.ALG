Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/03/2022
Var
// Seção de Declarações das variáveis 
nota1, nota2, media, notafinal, mediafinal:real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite sua nota 1:")
leia(nota1)
escreval("Digite sua nota 2:")
leia(nota2)
media <- (nota1 + nota2) / 2
se media >=7.0 entao
   escreval("Você está aprovado")
fimse
se media <3.5 entao
   escreval("Você está reprovado")
fimse
se (media >=3.5) e (media <=6.9) entao
   escreval("Você está de recuperação, sua média foi:", media)
   escreval("Você deve fazer um exame final")
   escreval("Digite sua nota do exame final:")
   leia(notafinal)
   mediafinal <- ((10.0 - media) + notafinal) / 2
   se mediafinal >=5.0 entao
      escreval("Aprovado com exame final, sua média final foi:", mediafinal)
   senao
      escreval("Você ficou reprovado, sua média final foi:", mediafinal)
   fimse
fimse
Fimalgoritmo