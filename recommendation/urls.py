# recommendation/urls.py
from django.urls import path
from .views import RecommendView
from .auth_views import RegisterView, LoginView

urlpatterns = [
    path('recommend/', RecommendView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]