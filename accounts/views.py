from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'accounts/home.html')
def contact(request):
    return render(request,'accounts/basic.html',{'content':['if you world like to contact ,please email ','ford@gmail.com']})
