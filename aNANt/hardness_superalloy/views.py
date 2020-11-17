from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import HardnessForm 
from django.core.files.uploadedfile import SimpleUploadedFile
import numpy as np
from .models import Image
import os
import cv2
import joblib
import matplotlib.pyplot as plt
import pandas as pd

# Create your views here.

def index(request):

    template = loader.get_template('hardness_superalloy/index.html')
    form=HardnessForm()
    context={'form':form}
    return HttpResponse(template.render(context, request))


def img_proc(request):

    template = loader.get_template('hardness_superalloy/result.html')
    

    if request.method =='POST':
         form1= HardnessForm(request.POST,request.FILES)
         if form1.is_valid():          
              form1.save()
              print("Valid")
              Al=form1['Al'].value()
              Mo=form1['Mo'].value()
              Hf=form1['Hf'].value()
              Ta=form1['Ta'].value()
              Ti=form1['Ti'].value()
              V=form1['V'].value()
              Cr=form1['Cr'].value()
              Mn=form1['Mn'].value()
              Fe=form1['Fe'].value()
              Ni=form1['Ni'].value()
              Cu=form1['Cu'].value()
              Zr=form1['Zr'].value()
              Si=form1['Si'].value()

              Co=form1['Co'].value()
              Nb=form1['Nb'].value()
              W=form1['W'].value()

              Re=form1['Re'].value()
              C=form1['C'].value()
              B=form1['B'].value()
              P=form1['P'].value()
              S=form1['S'].value()

              ann_time=form1['ann_time'].value()
              ann_temp=form1['ann_temp'].value()
 
         
              ### Nikhil ML model
              all_comp=np.array([Al,Ti,V,Cr,Mn,Fe,Ni,Cu,Zr,Mo,Hf,Ta,Si])
              all_comp=all_comp.reshape(1,13)
 
              all_comp=standard(all_comp) 

              image=Image.objects.last()
              imagefile=image.imagefile
              #print('------------------------')
              #print(str(imagefile))
              #print('-------------------------')
              fullfile='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/media/'+str(imagefile)
              image = cv2.imread(fullfile,cv2.IMREAD_GRAYSCALE)
              #print(image.shape)
              
              topca=binarization(image)
              pca_coefficients=pca_model(topca)
              pca_feat=pca_coefficients[0,[0,1,3,9,11,18]]
              pca_feat=np.array(pca_feat)
              pca_feat=pca_feat.reshape(1,6)    
              #print(pca_feat) 
              #print(pca_feat.shape)   
              final_features=np.concatenate((pca_feat,all_comp),axis=1)
              
              value_hardness1=ml_model(final_features)[0]
              ####--------------------------------------------------------


              ###-----Sucheta ML Model------------------------------------
              sum1=0

              image=sucheta_binarization(image)   
              contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
              for c in contours:    
                  area = cv2.contourArea(c)
                  if area >=5:                         # to exclude area less than 5 pixels
                      sum1=sum1+area
              area_avg = sum1/((len(contours)))            ### This is the A_eff feature
              cont=len(contours)                           ### this is the Nobj feature

              all_comp1=[Al,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zr,Nb,Mo,Hf,Ta,W,Re,C,B,Si,P,S]
              boiling_p=prediction_boiling(all_comp1)
              sp_heat=prediction_sph(all_comp1)
              print("-----------------------------------------------------------------------")
              print(area_avg,cont,Fe,Ni,V,boiling_p,sp_heat,ann_temp,ann_time)
              print("-----------------------------------------------------------------------")
             
              feature_s=np.array([area_avg,cont,boiling_p,sp_heat,ann_temp,ann_time,V,Fe,Ni])
              feature_s=feature_s.reshape(1,9)

              feature_s=standard_sucheta(feature_s)   
              print(feature_s)
              value_hardness2=ml_model_sucheta(feature_s)[0]
              print("Sucheta harndess = ", value_hardness2)
              print("Sucheta harndess type ", type(value_hardness2))
              ######------------------------------------------------------      


              context={'hardness_Nikhil':"{:10.2f}".format(value_hardness1),'hardness_Sucheta':"{:10.2f}".format(value_hardness2)}
         else:
              context={}
              print("Not valid")  
        
    return HttpResponse(template.render(context, request))


def sucheta_binarization(image):
    img1=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,39,3)
    img1=cv2.resize(img1,(200,200))
    return(img1)


def binarization(image):
    img1=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,39,3)
    img1=cv2.resize(img1,(200,200))
    img1[img1>1]=1               # binarization of image to range (0 to 1)
    img1=img1.reshape((1,200,200))
    return(img1)

def pca_model(image):
    name='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/hardness_superalloy/mksmodel.sav'
    pymks_model=joblib.load(name)
    pca_all=pymks_model.transform(image)
    #print(pca_all.shape)
    return(pca_all)



def ml_model(features):
    name2='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/hardness_superalloy/GPR-and-lasso-Hv-model.sav'
    mlmodel=joblib.load(name2)
    features=pd.DataFrame(features)
    hardness=mlmodel.predict(features)
    # print("*************Hardness is =", hardness)
    return(hardness)


def ml_model_sucheta(features):
    name2='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/hardness_superalloy/gprlassobest_model_sucheta.sav'
    mlmodel=joblib.load(name2)
    features=pd.DataFrame(features)
    hardness=mlmodel.predict(features)
    # print("*************Hardness is =", hardness)
    return(hardness)


def standard(feature):
    name='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/hardness_superalloy/scalar.sav'
    scalar=joblib.load(name)
    feat=scalar.transform(feature)
    return(feat)


def standard_sucheta(feature):
    name='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/hardness_superalloy/standardscalar_model_sucheta.sav'
    scalar=joblib.load(name)
    feat=scalar.transform(feature)
    return(feat)


def prediction_boiling(df1):
    name='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/hardness_superalloy/elemental_features.xlsx'
    data = pd.read_excel(name,sheet_name='Sheet1',index_col=0)
    sum1=0
    for j in range(0,21,1):
        #print(df1[j]) 
        sum1=sum1+float(data.iloc[1,j])*float(df1[j])
    sum1=sum1/100
    #print(sum1)
    return(sum1)



def prediction_sph(df1):
    name='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/hardness_superalloy/elemental_features.xlsx'
    data = pd.read_excel(name,sheet_name='Sheet1',index_col=0)
    sum1=0
    for j in range(0,21,1):
        #print(df1[j]) 
        sum1=sum1+float(data.iloc[10,j])*float(df1[j])
    sum1=sum1/100
    #print(sum1)
    return(sum1)
