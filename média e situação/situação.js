var n1 = prompt('Informe a primeira nota: ');
var n2 = prompt('Informe a segunda nota: ')
var sn = +n1 + +n2

if (isNaN(n1) || isNaN(n2)) {
    console.log("Por favor, insira apenas números!")
} else {
    // Supondo que a média para passar seja 7
    var m = 21 - sn;
    console.log(`Para passar com média 7 na terceira prova, o aluno vai precisar tirar, no mínimo: ${m}.`)
}