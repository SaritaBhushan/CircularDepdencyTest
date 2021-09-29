from django import forms
from django.forms import fields  
from staff.models import Employee, Department

# class EmployeeCreateForm(forms.ModelForm):
#     model = Employee
#     fields = ['name', 'department']
#     name =forms.CharField(max_length=100, help_text='100 characters max.')
#     department = forms.ModelMultipleChoiceField(queryset=Department.objects.all())

# 6. forms.py - Create a ModelForm class to create an Employee object only entering the Employee name and Department fields.
class EmployeeForm(forms.ModelForm):  
    name =forms.CharField(max_length=100, help_text='100 characters max.')
    # dept1=Department.objects.all().order_by("name").values_list("name", "name")
    # print("***********",dept1, type(dept1))
    
    dept=Department.objects.all().order_by("name")
    # print("***********",dept, type(dept))
    deptList=[]
    deptList.append(['', "Choose..."])
    
    for item in dept:  # self.roles:
        deptList.append([item.name, item.name])# #Populating the list

    print("***********",deptList, type(deptList))
    department = forms.ChoiceField(choices=deptList)
    # department =forms.CharField(max_length=100, help_text='100 characters max.')
    # department = forms.ModelMultipleChoiceField(queryset=Department.objects.all())
    
    class Meta:  
        # To specify the model to be used to create form  
        model = Employee  
        # It includes all the fields of model  
        fields =['name', 'department']