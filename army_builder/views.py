from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Roster
from .forms import RosterForm

# Create your views here.
def get_index(request):
    return render(request, "pages/index.html")

def get_dashboard(request):
    return render(request, "users/dashboard.html")

def list_roster(request):

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
            messages.success(request, "Roster created successfully.")
            form.save()
            return redirect("roster-list")

    context = {
        "form": form,
    }

    return render(request, "army_builder/rosters/create.html", context)

def edit_roster(request, id):
    roster = get_object_or_404(Roster, id = id)

    form = RosterForm(instance=roster)

    if request.POST:
        form = RosterForm(request.POST, instance=roster)
        print(form.errors)
        if form.is_valid():
            messages.success(request, "Roster edited successfully.")
            form.save()
            return redirect("roster-list")

    context = {
        "roster": roster,
        "form": form,
    }

    return render(request, "army_builder/rosters/edit.html", context)

def delete_roster(request, id):
    roster = get_object_or_404(Roster, id = id)

    if request.POST:
        messages.success(request, "Roster deleted successfully.")
        roster.delete()
        return redirect("roster-list")

    context = {
        "roster": roster,
    }

    return render(request, "army_builder/rosters/delete.html", context)

def get_about(request):
    return render(request, "pages/about.html")
