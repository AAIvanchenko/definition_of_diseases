from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from webapp.models import Images
# Create your views here.

import os
import shutil
from model.model import start_model


def index(request):
    Images.objects.all().delete()
    if os.path.isdir('media/images'):
        shutil.rmtree('media/images')
    return render(request, 'webapp/index.html')


def result(request):
    images = Images.objects.all()
    title_list, result_list = start_model()
    dict_el = []
    # print(title_list)
    for i in range(len(images)):
        dict_el.append(("media/"+images.values()[i]['image'], title_list[i], result_list[i]))

    return render(request, 'webapp/result.html', {"dict_el": dict_el})


def guide(request):
    return render(request, 'webapp/guide.html'),


def file_upload(request):
    if request.method == "POST":
        my_file = request.FILES.get('file')
        Images.objects.create(image=my_file)
        return HttpResponse('')

    return JsonResponse({'post': 'false'})



