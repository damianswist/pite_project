from django.conf.urls import url

from . import views
from django.contrib.auth.decorators import login_required

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', login_required(views.home), name='home'),
]
