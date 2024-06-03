package com.progetto.progetto.repository;

import java.util.*;
import com.progetto.progetto.Professor;

public class ProfessorRepository {
    public static Map<Integer, Professor> professors = new HashMap<>();

    public static void addProfessor(Professor professor) {
        professors.put(professor.getId(), professor);
    }

    public static Professor getProfessorById(int id) {
        return professors.get(id);
    }

    public static List<String> getProfessorSubject(int id) {
        Professor professor = professors.get(id);
        return professor != null ? professor.getSubjects() : null;
    }
}