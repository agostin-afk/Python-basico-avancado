import sistema_conta as conta
import sistema_pessoas as pessoas


class Banco:
    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None = None,
                 contas: list[conta.Conta] | None = None):
        self.agencias = agencias or []
        self.contas = contas or []
        self.clientes = clientes or []

    def _checar_conta(self, conta: conta.Conta):
        if conta in self.contas:
            print('_checar_conta: ', True)
            return True
        print('_checar_: ', False)
        return False

    def _checar_agencia(self, conta: conta.Conta):
        if conta.agencia in self.agencias:
            print('_checar_agencia: ', True)
            return True
        print('_checar_: ', False)
        return False

    def _checar_cliente(self, clientes: pessoas.Pessoa):
        if clientes in self.clientes:
            print('_checar_cliente: ', True)
            return True
        print('_checar_: ', False)
        return False

    def _checa_se_conta_e_do_cliente(self, clientes, conta):
        if conta is clientes.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticacao(self, clientes: pessoas.Pessoa, conta: conta.Conta):
        return self._checar_agencia(conta) and \
            self._checar_conta(conta) and \
            self._checar_cliente(clientes) and \
            self._checa_se_conta_e_do_cliente(clientes, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.contas!r}, {self.clientes!r}'
        return f'{class_name} ({attrs})'


if __name__ == '__main__':
    c1 = pessoas.Cliente('Agosto', 45)
    cc1 = conta.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    banco = Banco()
    print(banco)
    banco.clientes.extend([c1])
    banco.contas.extend([cc1])
    banco.agencias.extend([111])
    print(banco.autenticacao(c1, cc1))
