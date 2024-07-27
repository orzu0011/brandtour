from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


class TourDetailView(DetailView):
    model = Tour
    template_name = "main/package_detail.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['tour_imgs'] = TourImg.objects.filter(tour_id=self.kwargs['pk'])
        context['recent_tours'] = Tour.objects.filter(status__in=["available", "discount"]).exclude(
            id=self.kwargs['pk']).order_by("-created_at")[:3]
        return context


class TourListView(ListView):
    model = Tour
    template_name = "main/package_list.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['tours'] = Tour.objects.filter(status__in=["available"]).order_by("-created_at")
        return context


class SpecialTourListView(ListView):
    model = Tour
    template_name = "main/special_package.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['special_tours'] = Tour.objects.filter(status__in=["discount"]).order_by("-created_at")
        return context