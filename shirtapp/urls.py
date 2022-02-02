from django.urls import path
from .views import ShirtViews

urlpatterns = [
    path('shirts/', ShirtViews.as_view()),
    path('shirts/<int:id>', ShirtViews.as_view())
]