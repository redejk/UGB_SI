Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Efetuar a leitura de um nome (variável NOME) e o sexo (variável SEXO) de uma pessoa e apresentar como saída uma das seguintes mensagens: "Ilmo. Sr.", caso seja informado o sexo masculino (utilizar como valor o caractere "M"), ou "Ilma. Sra.", caso seja informado o sexo feminino (utilizar como valor o caractere "F"). Após a mensagem de saudação, apresentar o nome informado. O programa deve, após a entrada do sexo, verificar primeiramente se o sexo fornecido é realmente válido, ou seja, se é igual a "M" ou a "F". Não sendo essa condição verdadeira, o programa deve apresentar a mensagem "Sexo informado inválido".
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
NOME, SEXO: caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite seu nome:")
leia(NOME)
escreval("Qual seu sexo? MASCULINO(M ou m) / FEMININO(F ou f)")
leia(SEXO)
se (SEXO = "M") ou (SEXO = "m") ou (SEXO = "F") ou (SEXO = "f") entao
        se (SEXO = "M") ou (SEXO = "m") entao
                escreval("Sr. ", nome)
        senao
                escreval("Sra. ", nome)
        fimse
senao
        escreval("Sexo informado é inválido")
fimse
Fimalgoritmo