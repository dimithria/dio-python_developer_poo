import datetime
class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento, endereco)

class Conta:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = Extrato(cliente.nome)

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, cliente, limite_saque=500.0, saque_diario=5):
        super().__init__(agencia, numero_conta, cliente)
        self.limite_saque = limite_saque
        self.saque_diario = saque_diario
        self.saques_realizados = 0
        self.data_ultimo_saque = datetime.date.today()

class Extrato:
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def visualizar_extrato(self):
        print("\n======= EXTRATO BANCÁRIO =======\n")
        
        print(f"Cliente: {self.nome_cliente}\n")
        if not self.transacoes:
            print("Nenhuma movimentação realizada.\n")
        else:
            for transacao in self.transacoes:
                print(transacao)        
        print("-----------------------------------")

class Transacao:
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.datetime.now()
        
    def __str__(self):
        return f"{self.data.strftime('%Y-%m-%d %H:%M:%S')} - {self.descricao()}: R$ {self.valor:,.2f}"

class Saque(Transacao):
    def descricao(self):
        return "Saque"
    
    def registrar(self, conta):
        if datetime.date.today() != conta.data_ultimo_saque:
            conta.saques_realizados = 0
            conta.data_ultimo_saque = datetime.date.today()
            
        if isinstance(conta, ContaCorrente):
            if conta.saques_realizados >= conta.saque_diario:
                print("\nLimite de saques diários atingido.")
                print("-----------------------------------")
                return

            if self.valor > conta.limite_saque:
                print(f"\nO limite máximo por saque é de R$ {conta.limite_saque:,.2f}.")
                print("-----------------------------------")
                return

            if self.valor > conta.saldo:
                print("\nSaldo insuficiente para saque.")
                print("-----------------------------------")
                return

            if self.valor > 0:
                conta.saldo -= self.valor
                conta.extrato.adicionar_transacao(str(self))
                conta.saques_realizados += 1
                conta.data_ultimo_saque = datetime.date.today()
                print(f"\nSaque de R$ {self.valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido para saque. Por favor, insira um valor positivo.")

class Deposito(Transacao):
    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.extrato.adicionar_transacao(f"Depósito: +R$ {self.valor:,.2f}")
            print(f"\nDepósito de R$ {self.valor:,.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito. Por favor, deposite apenas valores positivos.")

class Banco:
    def __init__(self):
        self.clientes = {}
        self.contas = []
        self.numero_conta = 1

    def cadastrar_cliente(self):
        print("===== Cadastro de Cliente ======")
        
        while True:
            cpf = input("\nDigite o CPF: ")
            if not cpf.isdigit():
                print("\nCPF Inválido. Apenas números, por favor.")
                print("-----------------------------------")
                return

            if cpf in self.clientes:
                print("Cliente com esse CPF já existe.")
                print("-----------------------------------")
                return
            break
        nome = input("Digite o nome: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Endereço: ")
        print("\n-----------------------------------")
        
        self.clientes[cpf] = PessoaFisica(cpf, nome, data_nascimento, endereco)
        print("\nCliente cadastrado com sucesso!")

    def criar_conta_corrente(self):
        print("\n==== CRIAR CONTA CORRENTE ====")
        
        while True:
            cpf = input("Digite o CPF: ")
            if not cpf.isdigit():
                print("CPF Inválido!. Apenas números, porfavor.")
                return

            if cpf not in self.clientes:
                print("\nCPF não encontrado. Cadastre o cliente.")
                return
            break

        conta = ContaCorrente('0001', self.numero_conta, self.clientes[cpf])
        self.contas.append(conta)
        self.numero_conta += 1

        print(f"\nConta criada com sucesso!\nAgência: {conta.agencia}\nConta: {conta.numero_conta}\nCliente: {conta.cliente.nome}")
        print("\n-----------------------------------")
        
    def listar_contas(self):
        print("\n==== LISTA DE CONTA CORRENTE ====\n")
        
        if not self.contas:
            print("Nenhuma Conta Corrente foi cadastrada!")
            return

        for conta in self.contas:
            print(f"Agência: {conta.agencia}\nConta: {conta.numero_conta}\nCliente: {conta.cliente.nome}\nCPF: {conta.cliente.cpf}\nSaldo: R$ {conta.saldo:,.2f}")
            print("\n-----------------------------------")

class Menu:
    def __init__(self):
        self.banco = Banco()

    def executar(self):
        while True:
            print("\n$$ Sistema Bancário $$")
            print("========== MENU ==========|")
            print("1 - Cadastrar Cliente     |")
            print("2 - Criar Conta Corrente  |")
            print("3 - Depositar             |")
            print("4 - Sacar                 |")
            print("5 - Ver Extrato           |")
            print("6 - Listar Contas         |")
            print("7 - Sair                  |")
            print("==========================|")

            opcao = input("\nDigite a opção desejada: ")

            if opcao == '1':
                self.banco.cadastrar_cliente()

            elif opcao == '2':
                self.banco.criar_conta_corrente()

            elif opcao == '3':
                cpf = input("Digite o CPF do cliente: ")
                if not cpf.isdigit():
                    print("CPF Inválido!. Apenas números, porfavor.")
                    
                if cpf in self.banco.clientes:
                    valor = float(input("Qual o valor do depósito? "))
                    deposito = Deposito(valor)
                    for conta in self.banco.contas:
                        if conta.cliente.cpf == cpf:
                            deposito.registrar(conta)
                            break
                        else:
                            print("\nCliente não encontrado. Cadastre o cliente.")

            elif opcao == '4':
                cpf = input("Digite o CPF do cliente: ")
                if not cpf.isdigit():
                    print("CPF Inválido!. Apenas números, porfavor.")
                    
                else:
                    if cpf in self.banco.clientes:
                        valor = float(input("Qual o valor do saque? "))
                        saque = Saque(valor)
                        for conta in self.banco.contas:
                            if conta.cliente.cpf == cpf:
                                saque.registrar(conta)
                                break
                            else:
                                print("Cliente não encontrado. Cadastre o cliente.")

            elif opcao == '5':
                cpf = input("Digite o CPF do cliente: ")
                if not cpf.isdigit():
                    print("CPF Inválido!. Apenas números, porfavor.")
                    
                if cpf in self.banco.clientes:
                    for conta in self.banco.contas:
                        if conta.cliente.cpf == cpf:
                            conta.extrato.visualizar_extrato()
                            print(f"Saldo atual: R$ {conta.saldo:,.2f}")
                            break
                        else:
                            print("Cliente não encontrado. Cadastre o cliente.")

            elif opcao == '6':
                self.banco.listar_contas()

            elif opcao == '7':
                print("Saindo do Sistema Bancário. Até logo!")
                break
            else:
                print("Opção Inválida. Tente novamente.")
if __name__ == "__main__":
    menu = Menu()
    menu.executar()