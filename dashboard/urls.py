from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('input', views.input_data, name='input_data'),
    path('list', views.employeelist, name='employee_list'),
    path('detail/<int:_id>', views.detail_employee, name='employee_detail'),

]