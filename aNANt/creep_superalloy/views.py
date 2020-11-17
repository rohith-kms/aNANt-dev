from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import CreepForm 
import joblib
import pandas as pd




# Create your views here.

def index(request):

    template = loader.get_template('creep_superalloy/index.html')
    form=CreepForm()
    context={'form':form}
    return HttpResponse(template.render(context, request))

def creepResults(request):

    template = loader.get_template('creep_superalloy/result.html')

    if request.method == 'POST':
       form1= CreepForm(request.POST)  
       Al=form1['Al'].value()

       Co=form1['Co'].value()
       Nb=form1['Nb'].value()
       Mo=form1['Mo'].value()
       Hf=form1['Hf'].value()
       Ta=form1['Ta'].value()
       W=form1['W'].value()
       B=form1['B'].value()
       Ru=form1['Ru'].value()
       Ti=form1['Ti'].value()
       V=form1['V'].value()
       Cr=form1['Cr'].value()
       Mn=form1['Mn'].value()
       Fe=form1['Fe'].value()
       Ni=form1['Ni'].value()
       Cu=form1['Cu'].value()
       Zn=form1['Zn'].value()
       Zr=form1['Zr'].value()
       Rh=form1['Rh'].value()
       C=form1['C'].value()
       Re=form1['Re'].value()
       Si=form1['Si'].value()
       P=form1['P'].value()
       S=form1['S'].value()
       N=form1['N'].value()
       ann_temp1=form1['ann_temp1'].value()
       ann_temp2=form1['ann_temp2'].value()
       ann_time1=form1['ann_time1'].value()
       ann_time2=form1['ann_time2'].value()
       stress=form1['stress'].value()
       temperature=form1['temperature'].value()

       # all_comp to calculate the elemental features
       #all_comp=pd.DataFrame([Al,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Zr,Nb,Mo,Rh,Hf,Ta,W,Re,C,B,Si,P,S,Ru,N],index=['Al','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Zr','Nb','Mo','Rh','Hf','Ta','W','Re','C','B','Si','P','S','Ru','N'])
       all_comp=[Al,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Zr,Nb,Mo,Rh,Hf,Ta,W,Re,C,B,Si,P,S,Ru,N]
 
       thermal_cond=prediction_thermalcond(all_comp)          ##fnc defined below


       # this is the testing data for prediction
       all_feat=[Al,Co,Nb,Mo,Hf,Ta,W,B,Ru,ann_temp1,ann_time1,ann_temp2,ann_time2,thermal_cond,stress,temperature]
       

       ## Predition model applied
       creep_time_log=creeptime(all_feat)
       creep_time=pow(2.7,creep_time_log)


       context={'creep_time':creep_time} 
       #context={'C':C,'Al':Al,'Co':Co,'Nb':Nb,'Mo':Mo,'Hf':Hf,'Ta':Ta,'W':W,'B':B,'Ru':Ru,'Ti':Ti,'V':V,'Cr':Cr,'Mn':Mn,'Fe':Fe,'Ni':Ni,'Cu':Cu,'Zn':Zn,'Zr':Zr,'Rh':Rh,'Re':Re,'Si':Si,'P':P,'S':S,'N':N,'ann_temp1':ann_temp1,'ann_temp2':ann_temp2,'ann_time1':ann_time1,'ann_time2':ann_time2,'stress':stress,'thermal_cond':thermal_cond,'temperature':temperature}
    return HttpResponse(template.render(context, request))


def prediction_thermalcond(df1):
    
    name='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/creep_superalloy/elemental_features.xlsx'
    data = pd.read_excel(name,sheet_name='Sheet1',index_col=0)    
    sum1=0
    for j in range(0,25,1):
        #print(df1[j]) 
        sum1=sum1+float(data.iloc[9,j])*float(df1[j])
    sum1=sum1/100
    #print(sum1)
    return(sum1)
    
def creeptime(df1):
    name='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/creep_superalloy/finalized_model.sav'
    name2='/home/hp/Desktop/nikhil/anant/mxsearch_nikhil_sucheta_2.7_beta/creep_superalloy/scalarmodel.sav'
    loadscaler=joblib.load(name2)   # loading scalar
    loaded_model = joblib.load(name)   # loading GPR model
    df1=pd.DataFrame(df1)
    df1=df1.T	
    print(df1.shape)	
    df2=pd.DataFrame(loadscaler.transform(df1))      # data transformed by scalar and converted to dataframe


    predval=loaded_model.predict(df2)          # value in log form predictied by GPR model
    print(predval,pow(2.71,predval))
    return(predval)
