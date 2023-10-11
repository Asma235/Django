from django.urls import path
from . import views

urlpatterns = [
    # URL pattern to list employee names
    path('emp/', views.employee, name='employee'),

    # URL pattern to show employee details based on employee ID
    path('emp/<int:employee_id>/', views.get_employee_by_id, name='employee_detail'),
        
]
