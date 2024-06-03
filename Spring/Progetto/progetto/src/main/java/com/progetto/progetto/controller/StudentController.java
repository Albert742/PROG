package com.progetto.progetto.controller;

import com.progetto.progetto.Student;
import com.progetto.progetto.repository.StudentRepository;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Arrays;
import java.util.List;

@RestController
@RequestMapping("/students")
public class StudentController {

    @PostMapping
    public ResponseEntity<Student> addStudent(@RequestBody Student student) {
        StudentRepository.addStudent(student);
        return ResponseEntity.ok(student);
    }

    @PostMapping("/test")
    public ResponseEntity<Student> createTestStudent() {
        List<Integer> grades = Arrays.asList(90, 95, 98);
        Student student = new Student("Test Student", "Test Surname", 20, grades, 95.0, 1);
        StudentRepository.addStudent(student);
        return ResponseEntity.ok(student);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Student> getStudentById(@PathVariable int id) {
        Student student = StudentRepository.getStudentById(id);
        if (student == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(student);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Student> updateStudent(@PathVariable int id, @RequestBody Student student) {
        Student existingStudent = StudentRepository.getStudentById(id);
        if (existingStudent != null) {
            existingStudent.setName(student.getName());
            existingStudent.setSurname(student.getSurname());
            existingStudent.setAge(student.getAge());
            existingStudent.setGrades(student.getGrades());
            existingStudent.setAverageGrades(student.getAverageGrades());
            return ResponseEntity.ok(existingStudent);
        }
        return ResponseEntity.notFound().build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteStudent(@PathVariable int id) {
        StudentRepository.students.remove(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/{id}/average")
    public ResponseEntity<Double> calculateAverageGrades(@PathVariable int id) {
        Student student = StudentRepository.getStudentById(id);
        if (student != null && student.getGrades() != null && !student.getGrades().isEmpty()) {
            double sum = 0.0;
            for (int grade : student.getGrades()) {
                sum += grade;
            }
            return ResponseEntity.ok(sum / student.getGrades().size());
        }
        return ResponseEntity.notFound().build();
    }

    
}
