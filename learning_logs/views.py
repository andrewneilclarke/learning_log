from django.shortcuts import render

def index(request):
    """The homepage for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
