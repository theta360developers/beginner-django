from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Thetaimage


def home(request):
    images = Thetaimage.objects
    return render(
        request,
        'theta_images/home.html',
        {'images': images})


def details(request, image_id):
    theta_image = get_object_or_404(Thetaimage, pk=image_id)
    return render(
        request,
        "theta_images/details.html",
        {"theta_image": theta_image})
