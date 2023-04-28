from django.shortcuts import render
from query_search import Image_search


def landing_page(request):
    return render(request, 'landing.html')

def search_results(request):
    results = []
    submitted = False
    if request.GET.get('query'):
        query = request.GET['query']
        results = Image_search(query)
        submitted = True
    
    context = {
        'results': results,
        'query': query, 
        'submitted': submitted
    }

    return render(request, 'landing.html', context)
