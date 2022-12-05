from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,DeleteView,ListView,CreateView,UpdateView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django import forms
# Create your views here.
class SnackList(ListView):

    template_name='snack_list.html'
    model=Snack

class SnackDetail(DetailView):

    template_name='snack_detail.html'
    model=Snack


   


class SnackForm(forms.ModelForm):

    class Meta:
        model =Snack
        fields = ['title','description','purchaser']
        widgets = {
        'title': forms.TextInput(attrs={'class':"form-control", 'type':"text" ,}),
        'description': forms.TextInput(attrs={'class':"form-control", 'type':"text" ,}),
           }

class SnackCreate(CreateView):

    template_name='snack_create.html'
    model=Snack
    form_class = SnackForm

    

class SnackUpdate(UpdateView):
 
    template_name='snack_update.html'
    model=Snack
    form_class = SnackForm
   
class SnackDelete(DeleteView):

    template_name='snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snacks_list')
    
   