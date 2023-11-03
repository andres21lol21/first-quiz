package org.velezreyes.quiz.question6;

public class Drink {
    private String name;
    private double price;
    private boolean fizzy;

    public Drink(String name, double price, boolean fizzy) {
        this.name = name;
        this.price = price;
        this.fizzy = fizzy;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public boolean isFizzy() {
        return fizzy;
    }
}
