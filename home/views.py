from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def handler404(request, exception):
    """
    Custom 404 page handler.
    Renders templates/errors/404.html with a 404 status.
    """
    return render(request, "errors/404.html", status=404)