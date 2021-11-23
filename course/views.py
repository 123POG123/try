from django.shortcuts import render

# Create your views here.
def home(request, slug_template=None):

    return render(request, 'course/home.html')