from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeeList.as_view(), name='employee_list'),
    path('view/<int:pk>', views.employeeDetail.as_view(), name='employee_detail'),
    path('new', views.employeeCreate.as_view(), name='employee_new'),
    path('edit/<int:pk>', views.employeeUpdate.as_view(), name='employee_edit'),
    path('delete/<int:pk>', views.employeeDelete.as_view(), name='employee_delete'),
]