from django.shortcuts import render
from .models import Roster

# Create your views here.
def get_index(request):
    return render(request, "pages/index.html")

def get_dashboard(request):
    return render(request, "users/dashboard.html")

def get_roster_list(request):

    rosters = Roster.objects.all()

    context = {
        "rosters": rosters,
    }

    return render(request, "army_builder/rosters/view.html", context)

def get_about(request):
    return render(request, "pages/about.html")

