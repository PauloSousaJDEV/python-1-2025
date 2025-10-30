package br.com.fiap.entities;

public class Debito extends Cartao{

    private double descontoMensal;

    public Debito() {
    }

    public Debito(String nome, String bandeira, int cvv, double saldo, double descontoMensal) {
        super(nome, bandeira, cvv, saldo);
        this.descontoMensal = descontoMensal;
    }

    public double getDescontoMensal() {
        return descontoMensal;
    }

    public void setDescontoMensal(double descontoMensal) {
        this.descontoMensal = descontoMensal;
    }

    @Override
    public String toString() {
        return identificador() +
                "\nDesconto Mensal=" + descontoMensal +
                "\n" + super.toString() +
                "\nLimite: " + limite();
    }

    @Override
    public String identificador(){
        return "Informações do cartão"
    }
}
