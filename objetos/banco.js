const Banco = {
    conta: 235711,
    saldo: 2000,
    tipoDeConta: 'Corrente',
    agencia: '013',
    
    buscar: function() {
        console.log(`O saldo atual da conta é de ${this.saldo} R$.`)
    },
    deposito: function(dep) {
        this.saldo += dep
        console.log(`Após um depósito de ${dep} R$, o saldo da conta passou a ser ${this.saldo} R$`)
    },
    saque: function(saq) {
        this.saldo -= saq
        console.log(`Após um saque de ${saq} R$, o saldo da conta passou a ser ${this.saldo} R$`)
    },
    numeroDaConta: function() {console.log(`O número da conta é ${this.conta}`)}
}

Banco.numeroDaConta();
Banco.buscar();
Banco.deposito(1923);
Banco.saque(427);