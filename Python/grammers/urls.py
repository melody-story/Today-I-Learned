from django.urls import path

from grammers.views import GrammerView

urlpatterns = [
    path('grammers', GrammerView.as_view()),
]