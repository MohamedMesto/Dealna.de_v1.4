from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'ec_home/index.html')


def error_500(request):
    """Render custom 500 internal server error page."""
    return render(request, "500.html", status=500)
