from django.urls import path
from .views import Home, Add_Student, Delete_Student,Edit_Student

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('addstudent', Add_Student.as_view(),name='addstudent'),
    path('deletestudent', Delete_Student.as_view(),name='deletestudent'),
    path('editstudent/<int:id>/', Edit_Student.as_view(),name='editstudent'),
]