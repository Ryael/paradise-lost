from django.shortcuts import render

# Create your views here.
def get_index(request):
    return render(request, "pages/index.html")

def get_dashboard(request):
    return render(request, "users/dashboard.html")
