package br.com.fiap.entities;

public class Credito extends Cartao {

    private double valorParcela;

    public Credito() {
    }

    public Credito(String nome, String bandeira, int cvv, double saldo, double valorParcela) {
        super(nome, bandeira, cvv, saldo);
        this.valorParcela = valorParcela;
    }

    public double getValorParcela() {
        return valorParcela;
    }

    public void setValorParcela(double valorParcela) {
        this.valorParcela = valorParcela;
    }

    @Override
    public String toString() {
        return "Credito" +
                "\nValor da parcela=" + valorParcela +
                "\n" + super.toString();
    }

    public double limite() {
        return saldo - valorParcela;
    }

    @Override
    public String identificador(
            return "1234";
    )
}