from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.views.generic import TemplateView
from .models import Mxene
from django.core.files import File
from django.conf import settings
import os
import ase.io
import ase.build
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import SearchForm

# Create your views here.

# These are the views

def index(request):

    template = loader.get_template('mxn_search/index.html')
    form = SearchForm()
    context = {'form':form}

    return HttpResponse(template.render(context, request))


def searchResults(request):

    template = loader.get_template('mxn_search/mxene_list.html')

    if request.method == 'POST':

        request.session['M1'] = request.POST['M1']
        request.session['M2'] = request.POST['M2']
        request.session['X']  = request.POST['X']
        request.session['T1'] = request.POST['T1']
        request.session['T2'] = request.POST['T2']


    M1 = request.session['M1']
    M2 = request.session['M2']
    X = request.session['X']
    T1 = request.session['T1']
    T2 = request.session['T2']

    mxenes = search_function(M1,M2,X,T1,T2)
    number_of_results = mxenes.count

    page = request.GET.get('page',1)

    paginator = Paginator(mxenes,15)
    try:
        mxenes = paginator.page(page)
    except PageNotAnInteger:
        mxenes = paginator.page(1)
    except EmptyPage:
        mxenes = paginator.page(paginator.num_pages)

    #return HttpResponse(template.render(context,request))
    return render(request, 'mxn_search/mxene_list.html', {'mxenes':mxenes, 'number_of_results':number_of_results})


def details(request,pk):

    template = loader.get_template('mxn_search/mxene_details.html')
    mxene = get_object_or_404(Mxene, pk=pk)
    poscar_file = mxene.poscar_file
    poscar_content = poscar_file.read()
    poscar_content = str(poscar_content)[2:-3].replace('\\n','\n').replace('\\t','\t')

    structure = ase.io.read(poscar_file.url)
    supercell = ase.build.make_supercell(structure,[[4,0,0],[0,4,0],[0,0,1]])
    ase.io.write('/home/abhishek/aNANt/abc.xyz',supercell,'xyz')
    os.system('babel -xyz /home/abhishek/aNANt/abc.xyz -mol /home/abhishek/aNANt/abc.mol')
    with open('/home/abhishek/aNANt/abc1.mol') as f:
        mol = f.read()

#    os.remove('abc.xyz')
#    os.remove('abc1.mol')

    context={'mxene':mxene, 'poscar_content':poscar_content, 'mol':mol}

    return HttpResponse(template.render(context,request))


def download_xyz(request,pk):

    mxene = get_object_or_404(Mxene, pk=pk)
    poscar_file = mxene.poscar_file
    poscar_content = poscar_file.read()
    poscar_content = str(poscar_content)[2:-3].replace('\\n','\n').replace('\\t','\t')

    structure = ase.io.read(poscar_file.url)
    ase.io.write('temp.xyz',structure,'xyz')

    #poscar_path = poscar_file.url
    #file_path = os.path.join(settings.MEDIA_ROOT,poscar_path)

    file_path='temp.xyz'
    mxene_name = mxene.name

    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'attachment;filename=' +mxene_name + '.xyz'
            os.remove('temp.xyz')
            return response

    raise Http404

def download_cif(request,pk):

    mxene = get_object_or_404(Mxene, pk=pk)
    poscar_file = mxene.poscar_file
    poscar_content = poscar_file.read()
    poscar_content = str(poscar_content)[2:-3].replace('\\n','\n').replace('\\t','\t')

    structure = ase.io.read(poscar_file.url)
    ase.io.write('/home/abhishek/aNANt/temp.cif',structure,'cif')

    #poscar_path = poscar_file.url
    #file_path = os.path.join(settings.MEDIA_ROOT,poscar_path)

    file_path='/home/abhishek/aNANt/temp.cif'
    mxene_name = mxene.name

    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'attachment;filename=' +mxene_name + '.cif'
            #os.remove('temp.cif')
            return response

    raise Http404

def download_poscar(request,pk):

    mxene = get_object_or_404(Mxene, pk=pk)
    poscar_file = mxene.poscar_file
    poscar_path = poscar_file.url
    file_path = os.path.join(settings.MEDIA_ROOT,poscar_path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'attachment;filename=' +os.path.basename(file_path)
            return response

    raise Http404

def testing(request,pk):

    template = loader.get_template('mxn_search/lite3.htm')

    mxene = get_object_or_404(Mxene, pk=pk)
    poscar_file = mxene.poscar_file
    poscar_content = poscar_file.read()
    poscar_content = str(poscar_content)[2:-3].replace('\\n','\n').replace('\\t','\t')

    structure = ase.io.read(poscar_file.url)
    supercell = ase.build.make_supercell(structure,[[4,0,0],[0,4,0],[0,0,1]])
    ase.io.write('abc.xyz',supercell,'xyz')
    os.system('babel -xyz abc.xyz -mol abc.mol')
    with open('abc1.mol') as f:
        mol = f.read()

    os.remove('abc.xyz')
    os.remove('abc1.mol')

    context={'mxene':mxene, 'poscar_content':poscar_content, 'mol':mol}
    #context = {}

    return HttpResponse(template.render(context,request))


# Functions to help views

def search_function(M1,M2,X,T1,T2):

    mxenes = Mxene.objects\
    .filter(M1__contains=M1)\
    .filter(M2__contains=M2)\
    .filter(X__contains=X)\
    .filter(T1__contains=T1)\
    .filter(T2__contains=T2)

    if T1 != '':
        mxenes = mxenes.filter(T1=T1)

    if T2 != '':
        mxenes = mxenes.filter(T2=T2)

    return mxenes
