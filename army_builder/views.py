from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Roster
from .forms import RosterForm

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

def create_roster(request):

    form = RosterForm()

    if request.method == "POST":
        form = RosterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            messages.success(request, 'Roster created successfully.')
            form.save()
            return redirect("roster-list")

    context = {
        "form": form,
    }

    return render(request, "army_builder/rosters/create.html", context)

def get_about(request):
    return render(request, "pages/about.html")
