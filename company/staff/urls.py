from django.conf.urls import url
from django.urls import path, include
from staff import views
from staff.views import EmployeeCreateView, EmployeeFormView, DepartmentListView, DepartmentDetailView
# from rest_framework import routers
from staff.models import Department, Employee

# router = routers.DefaultRouter()
# router.register(r'emp', views.UserViewSet)
# router.register(r'dept', views.DepartmentListView)
# # router.register(r'empdept', views.UserRemarkViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     ]

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    
    # without forms.py
    path('newemployee/', EmployeeCreateView.as_view(model=Employee, success_url="success/"), name='employeeCreate'),
    path('newemployee/success/', views.employeeCreated, name='employeeCreated'),

    # forms.py
    path('employee/thanks/', views.employeeRegistered, name='employeeRegistered'),
    path('employee/', EmployeeFormView.as_view(), name='newEmployee'),
]