from django.forms import ModelForm
from idea.models import Idea


class IdeaStatusForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['projected_revenue', 'actual_net_revenue', 'status', 'score']
