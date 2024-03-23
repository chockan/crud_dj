from django import forms  
from app1.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__" 