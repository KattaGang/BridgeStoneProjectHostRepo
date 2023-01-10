from django.forms import ModelForm
from .models import Program, BusinessUnit

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        exclude = ['coordinator']

class BusinessUnitForm(ModelForm):
    class Meta:
        model = BusinessUnit
        fields = '__all__'
        exclude = []
        