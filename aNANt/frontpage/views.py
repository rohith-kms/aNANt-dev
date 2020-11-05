from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.views.generic import TemplateView

# Create your views here.

def index(request):

    template = loader.get_template('frontpage/index.html')
    context={}

    return HttpResponse(template.render(context, request))

def standard_page(request,heading,content):

    template = loader.get_template('frontpage/template.html')
    context={"heading":heading, "content":content}

    return HttpResponse(template.render(context, request))

def about(request):

    template = loader.get_template('frontpage/about.html')
    context={}

    return HttpResponse(template.render(context, request))

def contact(request):

    template = loader.get_template('frontpage/contact.html')
    context={}

    return HttpResponse(template.render(context, request))

def publications(request):

    template = loader.get_template('frontpage/publications.html')
    context={}

    return HttpResponse(template.render(context, request))

def acknowledgements(request):

    template = loader.get_template('frontpage/acknowledgements.html')
    context={}

    return HttpResponse(template.render(context, request))
