var num1 = prompt("Informe um número: ");
var num2 = prompt("Informe outro número: ")
var c;
var r;
if (isNaN(num1) || isNaN(num2)) {
  console.log('Por favor insira apenas números.')
} else {
  var op = prompt("Qual operação você deseja realizar:\nSoma [+]\nSubtração [-]\nMultiplicação [*]\nDivisão [/] ");  
  if (op === '+') {
    c = +num1 + +num2
    console.log(`${num1} + ${num2} = ${c}`)
  } else if (op === '-') {
    c = +num1 - +num2
    console.log(`${num1} - ${num2} = ${c}`)
  } else if (op === '*') {
    c = +num1 * +num2
    console.log(`${num1} * ${num2} = ${c}`) 
  } else if (op === '/') {
    if (num2 !== '0') {
      c = +num1 / +num2
      r = +num1 % +num2
      console.log(`${num1} / ${num2} = ${c}, e a sobra é ${r}`)
    } else {
      console.log('Não é possível divir por 0!')
    }
  } else {
    console.log('Operação inválida!')
  }
}