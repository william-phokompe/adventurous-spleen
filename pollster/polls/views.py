from django.shortcuts import render

# Create your views here.
from .models import Question, Choice

def index(request):
    return render(request, 'polls/index.htm')