from django.shortcuts import render
from query_search import Image_search


def landing_page(request):
    return render(request, 'landing.html')

def search_results(request):
    #results = [] #just for testing git push
    query = request.GET.get('query')
    print(query)
    Image_search(query)
    context = {'query': query}
    return render(request, 'search_results.html', context)
