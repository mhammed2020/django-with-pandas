from django.shortcuts import render

from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from products.models import Product, Purchase
from django.contrib.auth.decorators import login_required

# Create your views here.

def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()

        # obj = Csv.objects.filter(activated=False) 
        # with open(obj.file_name.path, 'r') as f:
        #         reader = csv.reader(f)

        #         for row in reader:
        #             print(row)
               

        # obj.activated=True
        # obj.save()
        success_message= "Uploaded sucessfully"
    context = {
        'form': form,
       
    }
    return render(request, 'csvs/upload.html', context)



