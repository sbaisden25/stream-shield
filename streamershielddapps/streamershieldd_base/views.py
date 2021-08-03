from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def diamond_view(request):
    return render(request, 'pay_pages/diamond.html')

def gold_view(request):
    return render(request, 'pay_pages/gold.html')

def privpol_view(request):
    return render(request, 'legal_pages/privpol.html')

def terms_view(request):
    return render(request, 'legal_pages/terms.html')

def about_view(request):
    return render(request, 'misc_pages/about.html')   
