from django.forms import ModelForm
from .models import Profile, Invitation


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'is_jury', 'is_admin', 'jury_programs', 'jury_business_unit']

class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        fields = '__all__'
        exclude = ['admin', 'post']