Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Escreva um algoritmo que calcule o valor do imposto de renda de um contribuinte. Considere que o valor do imposto é calculado de acordo com a tabela abaixo:
//até R$10.000,00 / ALIQUOTA ISENTO / DEDUÇÃO 0
// > que R$10.000,00 e <= R$ 25.000,00 / ALIQUOTA 10% / DEDUÇÃO 1000
// > R$ 25.000,00 / ALIQUOTA 25% / DEDUÇÃO 4750
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
renda, imposto: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor da sua renda anual:")
leia(renda)
se renda <= 10000.00 entao
        escreval("Você está isento de imposto")
senao
        se (renda > 10000.00) e (renda <=25000.00) entao
                imposto <- (renda * 0.10) - 1000
                escreval("Seu imposto com 10% de aliquota foi: ", imposto:2:2)
        senao
                imposto <- (renda * 0.25) - 4750
                escreval("Seu imposto com 25% de aliquota foi: ", imposto:2:2)
        fimse
fimse
Fimalgoritmo