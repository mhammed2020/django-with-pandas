from django.shortcuts import render
from . models import Product,Purchase
import pandas as pd
from .utils import get_simple_plot

from django.http import HttpResponse
import matplotlib.pyplot as plt 
import seaborn as sns 
from django.contrib.auth.decorators import login_required
from .forms import PurchaseForm
# Create your views here.

def home(request) :
    graph = None
    error_message = None
    df = None

    qs = pd.DataFrame(Product.objects.all().values())
    qs1 = pd.DataFrame(Purchase.objects.all().values())
    qs['product_id'] = qs['id']

    if qs1.shape[0] > 0 :

        df = pd.merge(qs1,qs,on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis = 1)

        price = df['price']
        if request.method =='POST' :
            chart_type = request.POST['sales']
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            
            df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            df2 = df.groupby('date', as_index = False)['total_price'].agg('sum')

            if chart_type != "":
                if date_from != "" and date_to !="" :
                    df = df[(df['date']>date_from) & (df['date']< date_to)]
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                graph = get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data=df)
            else:
                error_message = "Please select a chart type to continue"
          
    else :
        error_message = 'no records in the database'
      




    context ={
        'price' : price,
        'graph': graph, 
        'error_message' : error_message ,
        
    }

    return render(request,'products/main.html',context)




def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    added_message=None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.salesman = request.user
        obj.save()

        form = PurchaseForm()
        added_message = "The purchase has been added"

    context = {
        'form': form,
        'added_message': added_message,
    }
    return render(request, 'products/add.html', context)

