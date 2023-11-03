package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {
    private static VendingMachineImpl instance;
    private Map<String, Drink> drinks;
    private double moneyInserted;

    private VendingMachineImpl() {
        drinks = new HashMap<>();
        drinks.put("ScottCola", new Drink("ScottCola", 0.75, true));
        drinks.put("KarenTea", new Drink("KarenTea", 1.00, false));
    }

    public static VendingMachine getInstance() {
        if (instance == null) {
            instance = new VendingMachineImpl();
        }
        return instance;
    }

    @Override
    public void insertQuarter() {
        moneyInserted += 0.25;
    }

    @Override
    public Drink pressButton(String drinkName) throws NotEnoughMoneyException, UnknownDrinkException {
        Drink drink = drinks.get(drinkName);
        if (drink == null) {
            throw new UnknownDrinkException();
        }
        if (moneyInserted < drink.getPrice()) {
            throw new NotEnoughMoneyException();
        }
        moneyInserted -= drink.getPrice();
        return drink;
    }
}
