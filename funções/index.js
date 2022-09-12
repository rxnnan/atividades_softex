// Função tradicional sem parâmetro 
function apresentacao() {
    console.log("Calculadora simples que realiza as 4 operações básicas.")
 }
apresentacao()

// Arrow functions com parâmetros que retornam um valor 
let soma = (num1, num2) => +num1 + +num2;
let sub = (num1, num2) => +num1 - +num2;
let prod = (num1, num2) => +num1 * +num2;
let div = (num1, num2) => +num1 / +num2;

// Função tradicional com parâmetros e um retorno de valor
function calculadora(num1, num2, operacao) {
  if (operacao === "+") {
    return soma(num1, num2);
  }
  if (operacao === "-") {
    return sub(num1, num2);
  }
  if (operacao === "*") {
    return prod(num1, num2);
  }
  if (operacao === "/") {
    return div(num1, num2);
  }
}

const resultado1 = calculadora(3, 13, "+");
console.log(resultado1);
const resultado2 = calculadora(5, 7, "-");
console.log(resultado2);
const resultado3 = calculadora(11, 2, "/");
console.log(resultado3);
const resultado4 = calculadora(17, 19, "*");
console.log(resultado4);