from django.shortcuts import render
from datetime import datetime

from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from products.models import Product, Purchase
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        
        try:
            obj = Csv.objects.get(activated=False) 
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for row in reader:
                    
                    print(row)
                    print(row[0])
                    print(row[3])
                    user = User.objects.get(id=row[3])
                    print(user)
                    print(row[4])
                    print(row[0])
                    prod, _ = Product.objects.get_or_create(name=row[0])
                    Purchase.objects.create(
                            product=prod,
                            price = int(row[2]),
                            quantity = int(row[1]),
                            salesman = user,
                            date = datetime.strptime(row[4], '%d/%m/%y %H:%M:%S')

                           
                        )
                
                

            obj.activated=True
            obj.save()
            success_message= "Uploaded sucessfully"

        except :
            error_message = "Ups. Something went wrong...."

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
       
    }
    return render(request, 'csvs/upload.html', context)



