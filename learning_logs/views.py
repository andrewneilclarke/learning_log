from django.shortcuts import render

def index(request):
    """The homepage for Learning Log"""
    return render(request, 'learning_logs/index.html')
