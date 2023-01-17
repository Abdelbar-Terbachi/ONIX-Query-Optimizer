from django.urls import path
from .views import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    # path("handle_form_submission/", OptimizationView.as_view(), name='optimization'),
]