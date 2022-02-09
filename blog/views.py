from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Index page view function.
    """
    text = "That's my new project index page!"
    return render(request,
                  'index.html',
                  context={
                      'text': text,
    })
