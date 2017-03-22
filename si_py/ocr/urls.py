from django.conf.urls import url
from . import views
app_name = 'ocr'
urlpatterns = [
    # ex: /ocr/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /ocr/upload/
    # url(r'^upload/$', views.Upload, name='upload'),
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    # ex: /ocr/result/
    # url(r'^result/$', views.Result, name='result'),
    url(r'^result/$', views.ResultView.as_view(), name='result'),
    # # ex: /polls/5/results/
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]