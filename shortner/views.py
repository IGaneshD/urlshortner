from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Url
import json
# Create your views here.

def shortenLink(request):

    context = {'Link':None, 'labelPresent':False}
    if request.method == "POST":
        url = request.POST["actualUrl"]
        shortText = request.POST["urlLabel"]
        try:
            instance = Url(link=url, shortLink = shortText)
            instance.save()

            context = {
            'Link': request.build_absolute_uri('') + 'short/' + shortText,
        }
        except:
            context['labelPresent'] = True
        
    

    return render(request, 'index.html', context)


def redirecttoURL(request, pk):
    url_details = Url.objects.get(shortLink = pk)
    
    return redirect(url_details.link)


def checkUrlLabel(request, pk):
    try:
        label = Url.objects.get(shortLink = pk)
    except:
        label = None

    if label:
        isLabelnotPresent = False
    else:
        isLabelnotPresent = True

    return JsonResponse({'isLabelnotPresent':isLabelnotPresent}, safe=False)