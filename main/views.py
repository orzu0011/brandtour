from typing import Any
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import Post
from tour.models import Tour, Destination
from user.models import Testimonial
from user.forms import TestimonialForm
from django.views.generic import TemplateView
from .forms import ContactForm
from django.shortcuts import HttpResponse
from django.views.generic import DetailView

class HomeView(View):
    def get(self, request):
        last_two_posts = Post.objects.all().order_by("-created_at")[:2]
        last_three_tours_disc = Tour.objects.filter(status="discount").order_by("-created_at")[:2]
        last_three_tours = Tour.objects.filter(status="available").order_by("-created_at")[:3]
        last_three_dests = Destination.objects.all().order_by("-created_at")[:5]
        last_five_testimonials = Testimonial.objects.all().order_by("-created_at")[:5]
        context = {
            "last_two_posts": last_two_posts,
            "last_three_tours": last_three_tours,
            "last_three_dests": last_three_dests,
            "last_three_tours_disc": last_three_tours_disc,
            "last_five_testimonials": last_five_testimonials
        }
        return render(request, "index.html", context)


class DestinationView(TemplateView):
    template_name = "main/destinations.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['dests'] = Destination.objects.all()
        return context

class DestinationDetailView(DetailView):
    model = Destination
    template_name = "main/destination_detail.html"
    context_object_name = "destination"

class AboutUsView(View):
    def get(self, request):
        return render(request, 'main/about.html')

    def post(self, request):
        form = TestimonialForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('main_about')
        return HttpResponse('ERROR!')


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html')

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_contact')
        return HttpResponse('Error!')

