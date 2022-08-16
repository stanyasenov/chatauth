import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import SignUpForm


def frontpage(request):

    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('frontpage')

    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form':form})


class ProfilePage(DetailView):
    model = User
    template_name = 'core/profilepage.html'
    context_object_name = 'profile'
