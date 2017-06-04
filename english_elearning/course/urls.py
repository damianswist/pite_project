from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import CourseView, WordsCourseView, CourseResultsView

urlpatterns = [
url(r'^course/?$', login_required(CourseView.as_view()), name='Course'),
url(r'^course_words/?$', login_required(WordsCourseView.as_view()), name='Words Course'),
url(r'^course_results/?$', login_required(CourseResultsView.as_view()), name='Course Results'),
]


