const {consultarCep} = require('correios-brasil')
const cep = '53441470';
consultarCep(cep).then(response => {
    console.log(response)
});

const { rastrearEncomendas } = require('correios-brasil')
let  codRastreio = ['PW123456789BR'] 
rastrearEncomendas(codRastreio).then((response) => {
  console.log(response);
});