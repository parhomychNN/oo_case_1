package ru.parhomych.case1.controllers;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

import java.net.URL;
import java.util.ResourceBundle;

public class Controller implements Initializable {


    @FXML
    private TextField m1TextField;

    @FXML
    private TextField n1TextField;

    @FXML
    private TextField c1TextField;

    @FXML
    private TextField c2TextField;

    @FXML
    private TextField m2TextField;

    @FXML
    private TextField n2TextField;

    @FXML
    private TextField rTextField;

    @FXML
    private Label debugLabel1;

    @FXML
    private Label debugLabel2;

    @FXML
    private Label debugLabel3;

    @FXML
    private Label debugLabel4;

    @FXML
    private Button calculateButton;

    private Double k;
    private Double b;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        calculateButton.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                calculate();
            }
        });
    }

    private void calculateCircleEquasion() {
        Double c1 = Double.valueOf(c1TextField.getText());
        Double c2 = Double.valueOf(c2TextField.getText());
        Double r = Double.valueOf(rTextField.getText());

        Double aEq, bEq, cEq;

        debugLabel2.setText("Окружность радиусом " + r + " и координатами (" + c1 + ", " + c2 + ")");

        if (k != null && b != null) {
            aEq = roundDoubleValue(Math.pow(k, 2) + 1, 4);
            bEq = roundDoubleValue(2 * k * b - 2 * c1 - 2 * c2 * k, 4);
            cEq = roundDoubleValue(Math.pow(b, 2) - 2 * c2 * b + Math.pow(c1, 2) + Math.pow(c2, 2) - Math.pow(r, 2), 4);
            debugLabel3.setText(aEq + "x^2 + " + bEq + "x + " + cEq);

            // quadratic equation

            Double d = Math.pow(bEq, 2) - 4 * aEq * cEq;
            if (d > 0) {
                // 2 roots
                Double x1 = (-bEq + Math.sqrt(d)) / (2 * aEq);
                Double y1 = k * x1 + b;

                Double x2 = (-bEq - Math.sqrt(d)) / (2 * aEq);
                Double y2 = k * x2 + b;

                debugLabel4.setText("Прямая и окружность пересекаются в точках " +
                        "(" + String.format("%.3f", x1) + ", " + String.format("%.3f", y1) + ") и ("
                        + String.format("%.3f", x2) + ", " + String.format("%.3f", y2) + ")");

            } else if (d.equals(0.0)) {
                // 1 root
                Double x = -bEq / 2 * aEq;
                Double y = k * x + b;
                debugLabel4.setText("Прямая и окружность пересекаются в точке (" + x + ", " + y + ")");
            } else {
                // no roots
                debugLabel4.setText("Прямая и окружность не пересекаются");
            }

        }
    }

    private void calculate() {
        Double m1 = Double.valueOf(m1TextField.getText());
        Double m2 = Double.valueOf(m2TextField.getText());
        Double n1 = Double.valueOf(n1TextField.getText());
        Double n2 = Double.valueOf(n2TextField.getText());
        Double c1 = Double.valueOf(c1TextField.getText());
        Double c2 = Double.valueOf(c2TextField.getText());
        Double r = Double.valueOf(rTextField.getText());

        if (m1.equals(n1)) {
            debugLabel1.setText("Вертикальная прямая x = " + m1);
            Double distanceBetweenCircleCenterAndLine = roundDoubleValue(Math.abs(m1 - c1), 6);
            if (distanceBetweenCircleCenterAndLine > r) {
                // no roots
                debugLabel4.setText("Прямая и окружность не пересекаются");
            } else if (distanceBetweenCircleCenterAndLine.equals(r)) {
                // 1 root
                debugLabel4.setText("Прямая и окружность пересекаются в точке (" + m1 + ", " + c2 + ")");
            } else {
                // 2 roots
                Double aEq = 1.0;
                Double bEq = -(2 * c2);
                Double cEq = Math.pow(c2, 2) + Math.pow(m1 - c1, 2) - Math.pow(r, 2);
                Double d = Math.pow(bEq, 2) - 4 * aEq * cEq;
                Double x1 = (-bEq + Math.sqrt(d)) / (2 * aEq);
                Double x2 = (-bEq - Math.sqrt(d)) / (2 * aEq);
                debugLabel4.setText("Прямая и окружность пересекаются в точках " +
                        "(" + String.format("%.3f", x1) + ", " + String.format("%.3f", m1) + ") и ("
                        + String.format("%.3f", x2) + ", " + String.format("%.3f", m1) + ")");
            }
        } else if (m2.equals(n2)) {
            debugLabel1.setText("Горизонтальная прямая y = " + m2);
            Double distanceBetweenCircleCenterAndLine = roundDoubleValue(Math.abs(m2 - c2), 6);
            if (distanceBetweenCircleCenterAndLine > r) {
                // no roots
                debugLabel4.setText("Прямая и окружность не пересекаются");
            } else if (distanceBetweenCircleCenterAndLine.equals(r)) {
                // 1 root
                debugLabel4.setText("Прямая и окружность пересекаются в точке (" + c1 + ", " + m2 + ")");
            } else {
                // 2 roots
                Double aEq = 1.0;
                Double bEq = -(2 * c1);
                Double cEq = Math.pow(c1, 2) + Math.pow(m2 - c2, 2) - Math.pow(r, 2);
                Double d = Math.pow(bEq, 2) - 4 * aEq * cEq;
                Double x1 = (-bEq + Math.sqrt(d)) / (2 * aEq);
                Double x2 = (-bEq - Math.sqrt(d)) / (2 * aEq);
                debugLabel4.setText("Прямая и окружность пересекаются в точках " +
                        "(" + String.format("%.3f", x1) + ", " + String.format("%.3f", m2) + ") и ("
                        + String.format("%.3f", x2) + ", " + String.format("%.3f", m2) + ")");
            }
        } else {
            k = (m2 - n2) / (m1 - n1);
            b = m2 - k * m1;
            debugLabel1.setText("Уравнение прямой: y = " + k + "x + " + b);
            calculateCircleEquasion();
        }

    }

    private Double roundDoubleValue(Double value, int decimalPlaces) {
        Double multiplier = Math.pow(10d, decimalPlaces);
        return (double) Math.round(value * multiplier) / multiplier;
    }

}
