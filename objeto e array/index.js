var array = ['Banana', 'Palavra', 'Sorvete', 'Abacaxi', 'Carro']

var Banco = {
    conta: 235711,
    saldo: 2000,
    tipoDeConta: 'Corrente',
    agencia: '013',
}

function listaPropriedades(obj) {
    console.log('As propriedades do objeto são: ')
    for (let propriedade in obj) {
        console.log(`${propriedade}: ${obj[propriedade]}`)
    }
}

function listaElementos(arr) {
    console.log('Os elementos do array são: ')
    for (let elemento of arr) {
        console.log(`${elemento}`)
    }
}

listaPropriedades(Banco)
listaElementos(array)
