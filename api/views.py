from rest_framework.decorators import api_view
from rest_framework.response import Response
from idea.models import Idea
from program.models import Program, BusinessUnit
from .serializers import IdeaSerializer, BusinessUnitSerializer, ProgramSerializer
from django.http import JsonResponse
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/programs/',
        'GET /api/ideas/',
        'GET /api/business_units/',
        'GET /api/program/<int:pk>/',
        'GET /api/idea/<int:pk>/',
        'GET /api/business_unit/<int:pk>/',
        'GET /api/get-idea-activity/',
    ]
    return Response(routes)
# --------------- Idea -------------

@api_view(['GET'])
def getIdeas(request):
    ideas = Idea.objects.all()
    serializer = IdeaSerializer(ideas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getIdea(request, pk):
    idea = Idea.objects.get(id=pk)
    serializer = IdeaSerializer(idea)
    return Response(serializer.data)

# --------------- Idea -------------



# --------------- BusinessUnit -------------

@api_view(['GET'])
def getBusinessUnits(request):
    programs = BusinessUnit.objects.all()
    serializer = BusinessUnitSerializer(programs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBusinessUnit(request, pk):
    program = BusinessUnit.objects.get(id=pk)
    serializer = BusinessUnitSerializer(program)
    return Response(serializer.data)

# --------------- BusinessUnit -------------
# --------------- Program -------------

@api_view(['GET'])
def getPrograms(request):
    business_units = Program.objects.all()
    serializer = ProgramSerializer(business_units, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProgram(request, pk):
    business_unit = Program.objects.get(id=pk)
    serializer = ProgramSerializer(business_unit)
    return Response(serializer.data)

# --------------- Program -------------

@api_view(['GET'])
def getIdeaActivity(request):
    data = {}
    for idea in Idea.objects.all():
        date = idea.created.strftime('%d %m %y')
        data.setdefault(date, 0)
        data[date] += 1
    response = {}
    myKeys = list(data.keys())
    myKeys.sort()
    sortedData = {i : data[i] for i in myKeys}
    data = sortedData
    response['dates'] = []
    response['freq'] = []
    for key in data:
        response['dates'].append(key)
        response['freq'].append(data[key])
    return Response(response)