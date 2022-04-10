Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. Considerando que para um candidato, tem-se um registro contendo seu nome e as notas obtidas, em cada uma das provas, construir um algoritmo que forneça:
//a) O nome e as notas em cada prova do candidato.
//b) A média do candidato.
//c) Um informação dizendo se o candidato foi aprovado ou não. Considere que um candidato é aprovado se sua média for maior que 5,0 e se não apresentou nenhuma nota abaixo de 4,0.
// Autor(a)    : Carlos Eduardo Ferreira
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
nota1, nota2, nota3, media: real
nome: caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
Escreval("Digite seu nome:")
leia(nome)
Escreval("Digite sua primeira nota:")
leia(nota1)
Escreval("Digite sua segunda nota:")
leia(nota2)
Escreval("Digite sua terceira nota:")
leia(nota3)
media <- (nota1 + nota2 + nota3) / 3
se (media > 5.00) e (nota1 >= 4.00) e (nota2 >= 4.00) e (nota3 >= 4.00) entao
        escreval(nome, " você teve média:", media, " e foi aprovado")
senao
        escreval(nome, " você teve média:", media, " e foi reprovado")
fimse
Fimalgoritmo