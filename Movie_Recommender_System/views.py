from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

from . import code
import pandas as pd


# Create your views here.


def indexpage(request):
    print("hello world")
    return render(request, 'index.html')


def homepage(request):
    data = code.collect_movies()
    # print(data)
    table_html = data.to_html(classes='table table-striped')

    romance = code.romantic()
    romance_table = romance.to_html(classes='table table-striped')

    context = {
        'data': table_html,
        'romantic': romance_table
    }

    return render(request, 'home.html', context)




def plotpage(request):
    data1 = code.similar1()
    df1 = pd.DataFrame(data1)
    table_html1 = df1.to_html(classes='table table-striped')

    data2 = code.similar2()
    df2 = pd.DataFrame(data2)
    table_html2 = df2.to_html(classes='table table-striped')

    context = {
        'data': table_html1,
        'romantic': table_html2
    }

    return render(request, 'plot.html', context)


def hybridpage(request):
    data = code.print1()
    table_html = data.to_html(classes='table table-striped')

    romance = code.print2()
    romance_table = romance.to_html(classes='table table-striped')

    p3 = code.print3()
    table3 = p3.to_html(classes='table table-striped')

    p4 = code.print4()
    table3 = p4.to_html(classes='table table-striped')

    context = {
        'data': table_html,
        'romantic': romance_table,
        'p3': p3,
        'p4': p4
    }

    return render(request, 'hybrid.html', context)