Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Fazer a leitura de um valor numérico inteiro qualquer e apresentá-lo caso não seja maior que 3. Dica: para a solução deste problema utilize apenas o operador lógico de negação.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
A: inteiro
solucao: logico
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
solucao <- nao (A >=3 )
escreval("O valor digitado de A: ",A," não é maior do que 3. ", solucao)
Fimalgoritmo