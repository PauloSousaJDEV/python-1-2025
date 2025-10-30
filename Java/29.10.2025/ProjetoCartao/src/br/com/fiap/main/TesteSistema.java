package br.com.fiap.main;

import br.com.fiap.entities.Credito;
import br.com.fiap.entities.Debito;

import javax.swing.*;

public class TesteSistema {

    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    static int inteiro(String j){
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        Credito objCredito = new Credito(
                texto("Nome"),
                texto("Bandeira"),
                inteiro("CVV"),
                real("Saldo"),
                real("Valor Parcela")
        );

        Debito objDebito = new Debito(
                texto("Nome do Cartão de Débito"),
                texto("Bandeira"),
                inteiro("CVV"),
                real("Saldo"),
                real("Desconto mensal")
        );

        System.out.println();
    }
}