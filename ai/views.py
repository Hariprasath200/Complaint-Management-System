from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint
from .models import Complaint

from django.shortcuts import redirect
from django.http import HttpResponse

from ai.forms import ComplaintForm

def index(request):
    return render(request,('ai/index.html'))

def check(request):
    complaints = Complaint.objects.all()
    return render(request, 'ai/check.html',{'complaints': complaints})



def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            form = ComplaintForm()  
            return redirect('success_page')  
    else:
        form = ComplaintForm()

    return render(request, "ai/complaint.html", {'form': form})


def success_page(request):
    return render(request, "ai/success.html")   


def status(request):
    complaints = Complaint.objects.all()
    return render(request, "ai/status.html", {'complaints': complaints})


# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Complaint

def update_status(request):
    if request.method == 'POST':
        complaint_id = request.POST.get('complaint_id')
        status = request.POST.get('status')

        try:
            complaint = Complaint.objects.get(pk=complaint_id)
            complaint.status = status
            complaint.save()
            messages.success(request, 'Status updated successfully.')
        except Complaint.DoesNotExist:
            messages.error(request, 'Complaint does not exist.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return redirect('check')
