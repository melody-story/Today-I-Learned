from django.urls import path

from grammers.views import GrammerView, ProgrammersExample2View, ProgrammersExample3View

urlpatterns = [
    path('grammers', GrammerView.as_view()),
]