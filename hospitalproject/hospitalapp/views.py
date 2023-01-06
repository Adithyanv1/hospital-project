from django.shortcuts import render
from .models import DEPARTMENT,DOCTOR
from .forms import BookingForm

# Create your views here.
def index(request):
    person={
        'name':'abhin sir',
        'age':19
    }
    return render(request,'index.html',person)
def about(request):
    return render(request,'about.html')    
def contact(request):
    
    return render(request,'contact.html')   
def booking(request):
    if request.method=="POST":
      form=BookingForm(request.POST)
      if form.is_valid():
          form.save()
          return render(request,'confirmation.html')
    formvb=BookingForm()


    dict_book={
        'book': formvb
    }
    return render(request,'booking.html',dict_book)   
def doctors(request):
    dict_doc={
        'doc':DOCTOR.objects.all()
    }
    return render(request,'doctors.html',dict_doc)
def department(request):
    dict_dept={
        'dept':DEPARTMENT.objects.all()
    }
    
    return render(request,'department.html',dict_dept)          