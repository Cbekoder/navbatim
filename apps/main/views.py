from django.shortcuts import render


def coming_soon(request):
    """
    Render the "Coming Soon" page.
    """
    return render(request, 'coming_soon/count_down.html')