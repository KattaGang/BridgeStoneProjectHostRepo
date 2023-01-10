from django.forms import ModelForm
from .models import Idea, BusinessUnit


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'
        exclude = ['ideator', 'status', 'program', 'business_unit',
                   'is_accepted', 'is_rejected', 'is_on_hold', 'is_pending', 'projected_revenue', 'actual_net_revenue', 'score']


class BusinessUnitForm(ModelForm):
    class Meta:
        model = BusinessUnit
        fields = '__all__'
