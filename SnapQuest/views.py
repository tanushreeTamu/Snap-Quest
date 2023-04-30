import os

from django.shortcuts import render
from query_search import Image_search
from DESM_query_serach import DESM_search
from positional_search import Pos_query_search
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def landing_page(request):
    return render(request, 'landing.html')

def search_results(request):
    results = []
    submitted = False
    if request.GET.get('query'):
        query = request.GET['query']
        #results = Image_search(query)
        results = Pos_query_search(query)
        submitted = True
    
    context = {
        'results': results,
        'query': query, 
        'submitted': submitted
    }

    return render(request, 'landing.html', context)

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage(os.path.join(settings.STATICFILES_DIRS[0], 'new_images'))
        filename = fs.save(myfile.name, myfile)
        return render(request, 'landing.html')
    return render(request, 'landing.html')