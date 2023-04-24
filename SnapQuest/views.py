from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing.html')


def search_results(request):
    query = request.GET.get('query')
    context = {'query': query}
    return render(request, 'search_results.html', context)
