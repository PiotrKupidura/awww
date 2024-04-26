from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Comment
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import CreateForm

class IndexView(generic.ListView):
    template_name = "comments/index.html"
    context_object_name = "comment_list"

    def get_queryset(self):
        return Comment.objects.all()


class CreateView(generic.FormView):
    template_name = "comments/create.html"
    form_class = CreateForm
    success_url = "/comments"
    
    def form_valid(self, form) -> HttpResponse:
        form.create_comment()
        return super().form_valid(form)
    
    
class DetailView(generic.DetailView):
    model = Comment
    template_name = "comments/detail.html"
    def get_queryset(self):
        return Comment.objects.filter(published_from__lte=timezone.now())
    

class UpdateView(generic.UpdateView):
    model = Comment
    fields = ["text", "published_from"]
    success_url = "/comments"
    template_name = "comments/update.html"