from django.shortcuts import render

from django.views.generic import ListView, DetailView
# from django.shortcuts import render
from staff.models import Department, Employee
# from staff.forms import EmployeeCreateForm
from django.db import transaction
from django.utils import timezone
from django.http import Http404
from django.http import HttpResponse
# from django.views import View
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse

from .forms import EmployeeForm

# 5. views.py (Department) - Using generic class-based views please write the following views for the Department objects: list and detail

# Using generic class-based views for the Department objects: list
class DepartmentListView(ListView):
    model = Department
    context_object_name = 'my_favorite_departments'
    template_name = 'staff/department_list.html'

# Using generic class-based views for the Department objects: detail
class DepartmentDetailView(DetailView):
    # context_object_name = 'department'
    queryset = Department.objects.all()
    # model = Department
    def get_object(self):
        try:
            obj = super().get_object()
            # Record the last accessed date
            obj.now = timezone.now()
            obj.save()
            return obj
        except Exception:
            raise Http404('Note: Department does not exist.')

def department(request):
    return render(request, "staff/department.html")

# _______________________________________________

# 7. views.py (Employee) - Using a generic class-based view use the form in #6 in a create view for Employee objects. Is your models.py class for Employee compatible with the form and view?

# A generic class-based Createview to create view for Employee objects
class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'department']
    # return HttpResponse('result')

# Render to employee create sucess message
def employeeCreated(request):
    return render(request,'staff/sucess.html')


# A generic class-based formview to create view for Employee objects
class EmployeeFormView(FormView):
    # specify the Form
    form_class = EmployeeForm
    
    # specify name of template
    template_name = "staff/employee_form.html"
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
         
        # perform a action here
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)

# Render to employee create sucess message
def employeeRegistered(request):
    return render(request,'staff/thanks.html')