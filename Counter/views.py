# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from Counter.models import Counter
from django.template import RequestContext
from django.core.context_processors import csrf
from django.template import Context, loader

def index(request):
    all = Counter.objects.all()
    c = RequestContext(request, {
        'counters' : all
    })
    return render_to_response('index.html', c)

def create(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        count = data.get('count')

        userInput = validate(title, count)

        if not userInput:
            title = 'Bad'
            count = 0
        else:
            title = userInput[0]
            count = userInput[1]

        new = Counter(title=title, count=count)

        try:
            uniqueTest = Counter.objects.get(title=title)
        except Counter.DoesNotExist:
            new.save()
        else:
            uniqueTest.count = count
            uniqueTest.save()


    all = Counter.objects.all()
    c = RequestContext(request, {'counters' : all })
    return render_to_response('index.html', c)

def update(request):
    message = "Updated"
    data = request.POST
    newTitle = data.get('title')
    newCount = data.get('count')
    objectToUpdate = Counter.objects.all().get(title=newTitle)
    objectToUpdate.count = int(newCount)
    objectToUpdate.save()
    return HttpResponse(message)

def remove(request):
    if request.POST:
        import HTMLParser
        data = request.POST
        title = data.get('title')
        objectToRemove = Counter.objects.all().get(title=title)
        objectToRemove.delete()
        return HttpResponse("Deleted")
    return HttpResponse("Not Deleted")

def validate(title, count):
    if title.strip() == "" or not title.isalpha() or not count.isdigit():
        return False
    return (title, int(count))