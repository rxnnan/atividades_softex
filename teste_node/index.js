class Veiculo {
    constructor(tipoDoVeiculo) {
        this.tipoDoVeiculo = tipoDoVeiculo || 'carro';
        this.modelo = 'padrão';
        this.licenca = '00000-000';
    }
}
 
const testeDeInstancia = new Veiculo('carro');
console.log(testeDeInstancia);

const caminhao = new Veiculo('caminhão');
 
caminhao.setModelo = function(nomeDoModelo) {
    this.modelo = nomeDoModelo;
};
 
caminhao.setCor = function(cor) {
    this.cor = cor;
};
 
caminhao.setModelo('CAT');
caminhao.setCor('azul');
 
console.log(caminhao);
 
const segundaInstancia = new Veiculo('carro');
console.log(segundaInstancia);
 