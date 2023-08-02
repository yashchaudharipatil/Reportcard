import random
from Reportcard.models import Student, Subject, Subject_mark

def create_subject_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                Subject_mark.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0, 100)
                )
    except Exception as e:
        print("Error:", e)

# Call the function with the desired number of subject marks to create
create_subject_marks(10)
