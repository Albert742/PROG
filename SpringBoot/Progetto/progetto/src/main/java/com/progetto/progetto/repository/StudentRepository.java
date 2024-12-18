package com.progetto.progetto.repository;

import java.util.*;
import com.progetto.progetto.Student;

public class StudentRepository {
    public static Map<Integer, Student> students = new HashMap<>();

    public static void addStudent(Student student) {
        students.put(student.getId(), student);
    }

    public static Student getStudentById(int id) {
        return students.get(id);
    }

    public static Map<Integer, Student> getStudents() {
        return students;
    }
}