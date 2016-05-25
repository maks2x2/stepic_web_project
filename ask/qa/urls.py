from django.conf.urls import url
from qa.views import question

urlpatterns = [

    url(r'^(?P<num>\d+)/$', question),


]
