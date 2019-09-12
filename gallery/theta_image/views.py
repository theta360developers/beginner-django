from django.shortcuts import render
from django.http import HttpResponse
from .models import Thetaimage


def home(request):
    images = Thetaimage.objects
    return render(
        request,
        'theta_images/home.html',
        {'images': images})
