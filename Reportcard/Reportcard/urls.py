from django.contrib import admin
from django.urls import path
from card.views import get_students, see_marks  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', get_students, name="success_page"),
    path('see_marks/<student_id>/', see_marks, name="see_marks"),
]
