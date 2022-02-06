from dataclasses import fields
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.base import TemplateView # <- View class to handle requests
from .models import Artist
from django.views.generic import DetailView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

 #adds artist class for mock database data


class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["artists"] = Artist.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["artists"] = Artist.objects.all()
            # default header for not searching 
            context["header"] = "Trending Artists"
        return context


class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})



class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_update.html"
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})

class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = "/artists/"