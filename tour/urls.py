from django.urls import path
from .views import *

urlpatterns = [
    path("tour/<int:pk>/", TourDetailView.as_view(), name="tour_tour_detail"),
    path('all-tours/', TourListView.as_view(), name="tour_all_tours"),
    path("all-special-tour", SpecialTourListView.as_view(), name="tour_special_tours")
]