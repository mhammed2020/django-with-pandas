from django.shortcuts import render
from . models import Product,Purchase
import pandas as pd
# Create your views here.

def home(request) :

    qs = pd.DataFrame(Product.objects.all().values())
    qs1 = pd.DataFrame(Purchase.objects.all().values())
    qs['product_id'] = qs['id']
    df = pd.merge(qs1,qs,on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis = 1)

    context ={
        'products':qs.to_html(),
         'purchase':qs1.to_html(),

         'df' : df.to_html
    }

    return render(request,'products/main.html',context)
