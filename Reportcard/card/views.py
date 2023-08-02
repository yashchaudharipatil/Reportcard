from django.shortcuts import render
from .models import Student, Subject_mark

def see_marks(request, student_id):
    try:
        # Get the student object using the provided student_id
        student = Student.objects.get(pk=student_id)

        # Get all subject marks for the student
        marks = Subject_mark.objects.filter(student=student)

        # Calculate the total marks for the student
        total_marks = marks.aggregate(total_marks=models.Sum('marks'))

        # Create the context dictionary to be passed to the template
        context = {
            'student': student,
            'marks': marks,
            'total_marks': total_marks['total_marks'],
        }

        # Render the template with the provided context
        return render(request, 'see_marks.html', context)

    except Student.DoesNotExist:
        # Handle the case where the student with the provided ID does not exist
        return HttpResponse("Student not found.", status=404)
