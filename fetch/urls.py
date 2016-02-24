from django.conf.urls import url

from fetch.views import GetProductScoreView

urlpatterns = [
    url(r'^product/overall-score/(?P<pk>\d+)/$', GetProductScoreView.as_view()),
]
