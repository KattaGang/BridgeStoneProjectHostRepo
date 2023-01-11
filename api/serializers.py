from rest_framework.serializers import ModelSerializer
from idea.models import Idea
from program.models import Program, BusinessUnit

class IdeaSerializer(ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'


class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class BusinessUnitSerializer(ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = '__all__'