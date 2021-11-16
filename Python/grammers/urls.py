from django.urls import path

from grammers.views import GrammerView, ProgrammersExample2View

urlpatterns = [
    path('grammers', GrammerView.as_view()),
    path('programmers_example2', ProgrammersExample2View.as_view()),
]