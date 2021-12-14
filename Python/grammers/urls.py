from django.urls import path

from grammers.views import GrammerView, ProgrammersExample10_1View, ProgrammersExample10_2View, ProgrammersExample10_3View, ProgrammersExample10_4View, ProgrammersExample11View, ProgrammersExample12View, ProgrammersExample2View, ProgrammersExample3View, ProgrammersExample4View, ProgrammersExample5View, ProgrammersExample7View, ProgrammersExample8View, ProgrammersExample9View 

urlpatterns = [
    path('grammers', GrammerView.as_view()),
    path('programmers_example2', ProgrammersExample2View.as_view()),
    path('programmers_example3', ProgrammersExample3View.as_view()),
    path('programmers_example4', ProgrammersExample4View.as_view()),
    path('programmers_example5', ProgrammersExample5View.as_view()),
    path('programmers_example7', ProgrammersExample7View.as_view()),
    path('programmers_example8', ProgrammersExample8View.as_view()),
    path('programmers_example9', ProgrammersExample9View.as_view()),
    path('programmers_example10_1', ProgrammersExample10_1View.as_view()),
    path('programmers_example10_2', ProgrammersExample10_2View.as_view()),
    path('programmers_example10_3', ProgrammersExample10_3View.as_view()),
    path('programmers_example10_4', ProgrammersExample10_4View.as_view()),
    path('programmers_example11', ProgrammersExample11View.as_view()),
    path('programmers_example12', ProgrammersExample12View.as_view()),
]