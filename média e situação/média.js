var n1 = prompt('Informe a primeira nota: ')
var n2 = prompt('Informe a segunda nota: ')
var n3 = prompt('Informe a terceira nota: ')
var m = (+n1 + +n2 + +n3)/3

if (isNaN(n1) || isNaN(n2) || isNaN(n3)) {
  console.log("Por favor, insira apenas números.")
} else {
  // Supondo que a média para passar seja 7
  var situacao = m < 7 ? console.log(`Reprovado com média ${m}`) : console.log(`Aprovado com média ${m}`);
}

