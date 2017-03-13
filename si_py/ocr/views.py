from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.template import loader # Step 2
from django.views import generic

#def index(request):
    #context = {
        #'username': 'thuongtran this is',
    #}
    #return HttpResponse("Hello simple view") # Step 1
    #template = loader.get_template('ocr/index.html') # Step 2.1    
    #return HttpResponse(template.render(context, request)) # Step 2.2
    #return render(request, 'ocr/index.html', context) # Step 2.3 render

# generic views # Step 3
class IndexView(generic.TemplateView):
    template_name = 'ocr/index.html'
