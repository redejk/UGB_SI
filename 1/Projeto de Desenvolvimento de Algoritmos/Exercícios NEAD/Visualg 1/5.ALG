Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descrição   : Escreva um algoritmo que, para uma conta bancária, leia seu número, o saldo, o tipo de operação a ser realizada (depósito ou saque) e o valor da operação. Após, determine e mostre o novo saldo. Se o novo saldo ficar negativo, deve ser mostrada também a mensagem 'Conta estourada'.
// Data atual  : 03/04/2022
Var
// Seção de Declarações das variáveis 
conta: inteiro
operacao: caractere
saldo, valorop: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Digite o número da sua conta:")
leia(conta)
escreval("Digite seu saldo atual:")
leia(saldo)
escreval("Qual operação você quer efetuar? SAQUE(S) ou DEPOSITO(D)")
leia(operacao)
se (operacao = "S") ou (operacao = "s") entao
        escreval("Qual valor você quer sacar?")
        leia(valorop)
        saldo <- saldo - valorop
        se saldo < 0.00 entao
                escreval("Sua conta: ",conta," ficou estourada, com saldo: ", saldo)
        senao
                escreval("Operação realizada com sucesso, seu novo saldo é: ", saldo)
        fimse
senao
        escreval("Qual valor você quer depositar?")
        leia(valorop)
        saldo <- saldo + valorop
        escreval("Operação relizada com sucesso, seu novo saldo é: ", saldo)
fimse
Fimalgoritmo