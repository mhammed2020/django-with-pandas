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

        obj = Csv.objects.get(activated=False) 
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                
                # row = "".join(row)
                # row = row.replace(";", " ")
               
                # row = row.split()
                print(row)
                # user = User.objects.get(id=row[1])
                # print(user)
                # prod, _ = Product.objects.get_or_create(name=row[0])
                # Purchase.objects.create(
                #         product=prod,
                #         price = int(row[2]),
                #         quantity = int(row[1]),
                #         salesman = user,
                #         date = row[4]+ " "+ row[5]
                #     )
               
               

        obj.activated=True
        obj.save()
        success_message= "Uploaded sucessfully"
    context = {
        'form': form,
       
    }
    return render(request, 'csvs/upload.html', context)



