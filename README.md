# SISTEMA BANCÁRIO 2.1 - POO

# Sistema de Bancário em Python: Gerenciamento de Clientes e Contas

## Introdução
O código permite o cadastro de clientes, criação de contas correntes, realização de depósitos e saques, além de visualizar extratos.

## Conceitos Chave 
O sistema é estruturado em várias classes que representam diferentes entidades e funcionalidades:

    * Cliente: Representa um cliente do banco.

    * Conta: Representa uma conta bancária.

    * Transação: Representa uma transação 
    financeira, como depósitos e saques.

    * Banco: Gerencia clientes e contas.
    
    * Menu: Interface para interação com o usuário.

## Estrutura do Código
O código é organizado em classes, cada uma com suas responsabilidades. Aqui está um resumo das principais classes:

* *Cliente*: Classe base que armazena informações do cliente.

* *PessoaFisica*: Herda de Cliente, representando um cliente do tipo pessoa física.

* *Conta*: Classe base para contas, que armazena informações como agência, número da conta e saldo.

* *ContaCorrente*: Herda de Conta, adicionando funcionalidades específicas para contas correntes.

* *Extrato*: Armazena e exibe as transações realizadas pelo cliente.

* *Transacao*: Classe base para transações financeiras.

* *Saque e Deposito*: Heranças de Transacao, que implementam a lógica específica para saques e depósitos.

* *Banco*: Gerencia o cadastro de clientes e contas.

* *Menu*: Controla a interação do usuário com o sistema.

## Conclusão
Com classes bem definidas e uma estrutura clara, pode-se gerenciar clientes e contas de forma eficiente. Esse código pode ser expandido com mais funcionalidades, como transferências entre contas, gerenciamento de contas de poupança, entre outros.