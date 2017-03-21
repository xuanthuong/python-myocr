import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
#from django.urls import reverse
#from django.core.urlresolvers import reverse
#from django.template import loader # Step 2
from django.views import generic
#from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.files.storage import FileSystemStorage
from django.views.generic.base import RedirectView

from helper import helper
from django.http import JsonResponse


#def index(request):
    #context = {
        #'username': 'thuongtran this is',
    #}
    #return HttpResponse("Hello simple view") # Step 1
    #template = loader.get_template('ocr/index.html') # Step 2.1    
    #return HttpResponse(template.render(context, request)) # Step 2.2
    #return render(request, 'ocr/index.html', context) # Step 2.3 render #note: /ocr/index.html ->wrong

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

#class UploadView(generic.TemplateView):
    #template_name = 'ocr/upload.pug'
    #def get(self, request, *args, **kwargs):
        #response = TemplateResponse(request, self.template_name) # . vs render shortcut
        #return response
    
    #@ensure_csrf_cookie
    #def post(self, request, *args, **kwargs):
        #uploadDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.uploads')
        #print(uploadDir)
        #fs = FileSystemStorage(uploadDir)
        #uploadedFile = request.FILES['file']
        #filename = fs.save(uploadedFile.name, uploadedFile)
        #uploaded_file_url = fs.url(filename)
        #result = helper.handle_uploaded_file(os.path.join(uploadDir, uploaded_file_url))
        #print(result)

        #return HttpResponseRedirect('/ocr/result')    
        #return HttpResponseRedirect(reverse('ocr: result')) #same with shortcut redirect  
        #return redirect('result')
    
    #def get_context_data(self, **kwargs):
        #context = super(UploadView, self).get_context_data(**kwargs)
        #textimg = {'image': 'http://sachinchoolur.github.io/lightslider/img/cS-13.jpg'}
        #context['testimg'] = testimg
        #return context

    #@csrf_protect
    #def handler(request):
    # Process request    

#class ResultView(generic.TemplateView):
    #template_name = 'ocr/result.pug'    
    #def get(self, request, *args, **kwargs):
        #print 'show ocr result'
        #response = TemplateResponse(request, self.template_name)
        #return response

def Upload(request):
    if request.method == 'POST':
        uploadDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.uploads')
        print(uploadDir)
        fs = FileSystemStorage(uploadDir)
        uploadedFile = request.FILES['file']
        filename = fs.save(uploadedFile.name, uploadedFile)
        uploaded_file_url = fs.url(filename)
        # result = helper.handle_uploaded_file(os.path.join(uploadDir, uploaded_file_url))
        #print(result)
        return JsonResponse({'foo':'bar'})
    else:
        return render(request, 'ocr/upload.pug')
        # return redirect('/ocr/result/')

def Result(request):
    return render(request, 'ocr/result.pug')

class ResultRedirectView(RedirectView):
    permanent = False
    pattern_name = 'result'
    def get_redirect_url(self, *args, **kwargs):
        return super(ResultRedirectView, self).get_redirect_url(*args, **kwargs)
