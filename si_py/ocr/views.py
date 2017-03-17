from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
#from django.template import loader # Step 2
from django.views import generic
#from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from django.views.decorators.csrf import ensure_csrf_cookie

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
    template_name = 'ocr/index.pug'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        images = [
        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-1.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-1.jpg',
        },
        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-2.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-2.jpg',
        },
        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-3.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-3.jpg',
        },
        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-4.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-4.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-5.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-5.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-6.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-6.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-7.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-7.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-8.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-8.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-9.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-9.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-10.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-10.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-11.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-12.jpg',
        },

        {
          'thumbnail': 'http://sachinchoolur.github.io/lightslider/img/thumb/cS-13.jpg',
          'image': 'http://sachinchoolur.github.io/lightslider/img/cS-13.jpg',
        },
        ]
        context['images'] = images
        return context

class UploadView(generic.TemplateView):
    template_name = 'ocr/upload.pug'
    def get(self, request, *args, **kwargs):
        #print 'Handling get request'
        response = TemplateResponse(request, self.template_name) # . vs render shortcut
        return response
    
    #@ensure_csrf_cookie
    def post(self, request, *args, **kwargs):
        print 'Handling post request'
        return HttpResponse('Processing uploaded file')
        #response = TemplateResponse(request, self.template_name)
        #return response 
    
    #@csrf_protect
    #def handler(request):
    # Process request
