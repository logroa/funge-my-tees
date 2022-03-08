from django.urls import path
from .views import ShirtViews, OrderViews, AdvocateViews

urlpatterns = [
    path('shirts/', ShirtViews.as_view(), name='shirt-guy'),
    path('shirts/<int:id>', ShirtViews.as_view()),
    path('order/', OrderViews.as_view(), name='order-shirt'),
    path('advocates/', AdvocateViews.as_view(), name='advocate-view')
]