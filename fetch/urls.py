from django.conf.urls import url

from fetch.views import GetProductView

urlpatterns = [
    url(r'^product/$', GetProductView.as_view()),
]
