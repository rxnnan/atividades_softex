package br.com.empresa.funcionario;

import br.com.empresa.pessoa.Pessoa;

public class Funcionario extends Pessoa{

	private float salario;
	
	public void setSalario(float salario) {
		
		if(salario < 0) {
			this.salario = 0;
		} else {
			this.salario = salario;
		}
		
	}
	
	public float getSalario() {
		return this.salario;
	}
	
}
