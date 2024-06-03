package com.progetto.progetto;
import java.util.List;


public class Professor extends Person {
    private int id;
    private List<String> subjects;

    public Professor() {
    }

    public Professor(int id, String name, String surname, int age, List<String> subjects) {
        super(name, surname, age);
        this.id = id;
        this.subjects = subjects;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<String> getSubjects() {
        return subjects;
    }

    public void setSubjects(List<String> subjects) {
        this.subjects = subjects;
    }
}