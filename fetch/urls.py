from django.conf.urls import url

from fetch.views import GetProductScoreView, GetFullProductInfoView 

urlpatterns = [
    url(r'^product/overall-score/(?P<pk>\d+)/$', GetProductScoreView.as_view()),
    url(r'^product/full/(?P<pk>\d+)/$', GetFullProductInfoView.as_view()),
]
