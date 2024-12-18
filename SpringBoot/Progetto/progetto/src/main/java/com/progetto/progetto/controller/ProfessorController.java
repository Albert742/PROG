package com.progetto.progetto.controller;

import com.progetto.progetto.Professor;
import com.progetto.progetto.repository.ProfessorRepository;

import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Arrays;

@RestController
@RequestMapping("/professors")
public class ProfessorController {

    @PostMapping("/add")
    public Professor addProfessor(@RequestBody Professor professor) {
        ProfessorRepository.addProfessor(professor);
        return professor;
    }

    @PostMapping("/test")
    public Professor createTestProfessor() {
        List<String> subjects = Arrays.asList("Math", "Science");
        Professor professor = new Professor(1, "Test Professor", "Test Surname", 40, subjects);
        ProfessorRepository.addProfessor(professor);
        return professor;
    }

    @GetMapping("/{id}")
    public Professor getProfessorById(@PathVariable int id) {
        return ProfessorRepository.getProfessorById(id);
    }

    @GetMapping("/{id}/subjects")
    public List<String> getProfessorSubjects(@PathVariable int id) {
        Professor professor = ProfessorRepository.getProfessorById(id);
        if (professor != null) {
            return professor.getSubjects();
        }
        return null;
    }

    @PutMapping("/{id}")
    public Professor updateProfessor(@PathVariable int id, @RequestBody Professor professor) {
        Professor existingProfessor = ProfessorRepository.getProfessorById(id);
        if (existingProfessor != null) {
            existingProfessor.setName(professor.getName());
            existingProfessor.setSurname(professor.getSurname());
            existingProfessor.setAge(professor.getAge());
            existingProfessor.setSubjects(professor.getSubjects());
            return existingProfessor;
        }
        return null;
    }

    @DeleteMapping("/{id}")
    public void deleteProfessor(@PathVariable int id) {
        ProfessorRepository.professors.remove(id);
    }
}