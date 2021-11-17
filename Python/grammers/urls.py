from django.urls import path

from grammers.views import GrammerView, ProgrammersExample2View, ProgrammersExample3View, ProgrammersExample4View 

urlpatterns = [
    path('grammers', GrammerView.as_view()),
    path('programmers_example2', ProgrammersExample2View.as_view()),
    path('programmers_example3', ProgrammersExample3View.as_view()),
    path('programmers_example4', ProgrammersExample4View.as_view()),
]