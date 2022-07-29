package br.com.empresa.pessoa;

import java.io.Serializable;

public class Pessoa implements Serializable {
    private int idPessoa;
    private String nome;
    private float salario;
    
    public Pessoa(int idPessoa, String nome, float salario) {
        this.setIdPessoa(idPessoa);
        this.setNome(nome);
        this.setSalario(salario);
    }
    
    public int getIdPessoa() {
        return idPessoa;
    }
    public void setIdPessoa(int idPessoa) {
        this.idPessoa = idPessoa;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public float getSalario() {
        return salario;
    }
    public void setSalario(float salario) {
        this.salario = salario;
    }
}