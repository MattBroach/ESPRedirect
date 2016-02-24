from django.conf.urls import url

from fetch.views import GetProductView

urlpatterns = [
    url(r'^product/(?P<product>[\w-]+)/$', GetProductView.as_view()),
]
