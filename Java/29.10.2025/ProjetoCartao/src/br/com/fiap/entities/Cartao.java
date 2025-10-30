package br.com.fiap.entities;

import javax.swing.table.TableCellEditor;
import javax.swing.table.TableStringConverter;

public abstract class Cartao {

    private String nome;
    private String bandeira;
    private int cvv;
    protected double saldo;

    public Cartao(){}

    public Cartao(String nome, String bandeira, int cvv, double saldo) {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getBandeira() {
        return bandeira;
    }

    public void setBandeira(String bandeira) {
        this.bandeira = bandeira;
    }

    public int getCvv() {
        return cvv;
    }

    public void setCvv(int cvv) {
        this.cvv = cvv;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    @Override
    public String toString() {
        return "Cartao{" +
                "nome='" + nome + '\'' +
                ", bandeira='" + bandeira + '\'' +
                ", cvv=" + cvv +
                ", saldo=" + saldo +
                '}';
    }

    public abstract double limite();

    public abstract String identificador();
}