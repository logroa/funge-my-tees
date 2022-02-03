from django.urls import path
from .views import ShirtViews, OrderViews

urlpatterns = [
    path('shirts/', ShirtViews.as_view()),
    path('shirts/<int:id>', ShirtViews.as_view()),
    path('order/', OrderViews.as_view())
]