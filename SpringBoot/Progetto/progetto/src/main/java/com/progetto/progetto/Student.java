package com.progetto.progetto;

import java.util.List;

public class Student extends Person {
	private List<Integer> grades;
    private double averageGrades;
    private int id;

    public Student(String name, String surname, int age, List<Integer> grades, double averageGrades, int id) {
        super(name, surname, age);
        this.grades = grades;
        this.averageGrades = averageGrades;
        this.id = id;
    }

    // Getters and setters
    public List<Integer> getGrades() {
        return grades;
    }

    public void setGrades(List<Integer> grades) {
        this.grades = grades;
    }

    public double getAverageGrades() {
        return averageGrades;
    }

    public void setAverageGrades(double averageGrades) {
        this.averageGrades = averageGrades;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}