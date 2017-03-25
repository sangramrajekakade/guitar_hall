from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
class HomePage(TemplateView):
    template_name = 'guitar/homepage.html'

    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['guitar'] = AboutGuitar.objects.all()
        return context


class VideosPage(TemplateView):
    template_name = 'guitar/videos.html'

    def get_context_data(self, **kwargs):
        context = super(VideosPage, self).get_context_data(**kwargs)
        context['videos'] = YoutubeVideos.objects.all()
        return context

class Guitardetails(ListView):
    template_name = 'guitar/abtguitar.html'
    model = AboutGuitar

    def get_context_data(self, **kwargs):
        context = super(Guitardetails, self).get_context_data(**kwargs)
        context['guitar'] = AboutGuitar.objects.all()
        return context


class Detail_Guitar(DetailView):
    model = AboutGuitar
    #template_name = 'guitar/aboutguitar_detail.html'



class Admission(TemplateView):
    template_name = 'guitar/admission.html'



class BatchesPage(ListView):
    template_name = 'guitar/batches.html'
    model = Batches
    def get_context_data(self, **kwargs):
        context = super(BatchesPage, self).get_context_data(**kwargs)
        context['Batches'] = Batches.objects.all()
        return context



class ContactPage(TemplateView):
    template_name = 'guitar/contact.html'

class AboutPage(TemplateView):
    template_name = 'guitar/aboutus.html'


class feestructurePage(ListView):
    model = Feestructure
    template_name = 'guitar/feestructure.html'

    def get_context_data(self, **kwargs):
        context = super(feestructurePage, self).get_context_data(**kwargs)
        context['Feestructure'] = Feestructure.objects.all()
        return context


class BuyguitarPage(ListView):
    template_name = 'guitar/buyguitar.html'
    model = Buyguitar

    def get_context_data(self, **kwargs):
        context = super(BuyguitarPage, self).get_context_data(**kwargs)
        context['buyguitar'] = Buyguitar.objects.all()
        return context


class Buyguitar_details(DetailView):
    model = Buyguitar
    #template_name = 'guitar/aboutguitar_detail.html'


class PostPage(TemplateView):
    template_name = 'guitar/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostPage, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context


class Post_details(DetailView):
    model = Post
    #template_name = 'guitar/aboutguitar_detail.html'

