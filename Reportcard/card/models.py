from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_mail = models.EmailField()
    student_age = models.IntegerField()

    def __str__(self):
        return self.student_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Subject_mark(models.Model):
    student = models.ForeignKey(Student, related_name='studentsmarks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta:
        unique_together = ['student', 'subject']
