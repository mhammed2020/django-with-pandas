from django.shortcuts import render

# Create your views here.

def upload_file_view(request):
    error_message = None
    success_message = None

    return render(request, 'csvs/upload.html', {})



