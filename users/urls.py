from django.urls import path

from .views import UserLoginView, UserSignUpView

urlpatterns = [
    path('signup', UserSignUpView.as_view()),
    path('login', UserLoginView.as_view()),
]