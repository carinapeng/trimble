
/* id, name, grade of student with highest average grade */
SELECT student_id, name, grade 
FROM students JOIN assignments ON students.id = assignments.student_id
WHERE student_id = 
(
    SELECT MAX(avg_grade) FROM
        (SELECT
            AVG(grade),
            student_id
        AS avg_grade
        FROM assignments
        GROUP BY student_id)
    AS max_grade
);


/* Names of students who have not submitted an assignment */
SELECT name FROM students WHERE id NOT IN (SELECT student_id FROM assignments);