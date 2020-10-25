from django.shortcuts import render
from . models import Product
import pandas as pd
# Create your views here.

def home(request) :

    qs = pd.DataFrame(Product.objects.all().values())
    print(qs)
   

    return render(request,'products/main.html',{})
