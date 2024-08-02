from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='main_home_view'),
    path("destinations", DestinationView.as_view(), name="main_destination"),
    path('destinations/<int:pk>/', DestinationDetailView.as_view(), name='destination_detail'),
    path("about-us", AboutUsView.as_view(), name="main_about"),
    path('contact-us', ContactView.as_view(), name="main_contact"),
    # path('search', FilterTourView.as_view(), name="search_page"),
]