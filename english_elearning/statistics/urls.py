from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import StatisticsView

urlpatterns = [
    url(r'^statistics/?$', login_required(StatisticsView.as_view()), name='Statistics'),
]


