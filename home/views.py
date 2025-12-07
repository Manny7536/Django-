from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'page':'home'}
    return render(request, 'index.html', context)

def results(request):
    students=[
        {'name':'Subash Shah', 'age':23, 'ID':'10063','Marks': 86 },
        {'name':'Prasun Sedai', 'age': 21, 'ID':'10043','Marks': 78 },
        {'name':'Prasanna Karn', 'age': 19, 'ID':'10098','Marks': 80 },
        {'name': 'Shashwat Adhakari', 'age': 25, 'ID': '10033','Marks': 91 },
        {'name': 'Priyanshu Gajurel', 'age': 20, 'ID': '10078','Marks': 75 },
        {'name': 'Ram ', 'age': 23, 'ID': '10099','Marks': 39 },
    ]
    return render(request, 'dt.html', context={'students':students, 'page':'results'} )