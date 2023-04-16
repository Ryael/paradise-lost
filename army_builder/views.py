from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Roster
from .forms import RosterForm


def get_index(request):
    """
    Fetches the Home page.
    """
    return render(request, "pages/index.html")


@login_required
def get_dashboard(request):
    """
    Fetches the Dashboard page.
    """
    return render(request, "users/dashboard.html")


@login_required
def list_roster(request):
    """
    Fetches the My Roster page and all the user's rosters
    and orders by name. If the user is not logged in,
    they are redirected to the login page.
    """
    rosters = Roster.objects.filter(user=request.user).order_by("name")

    context = {
        "rosters": rosters,
    }

    return render(request, "army_builder/rosters/roster-list.html", context)


@login_required
def create_roster(request):
    """
    Fetches the Create Roster page. If the user is not logged in,
    they are redirected to the login page.
    """
    form = RosterForm()

    if request.method == "POST":
        form = RosterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            roster = form.save(commit=False)
            roster.user = request.user
            roster.save()
            messages.success(request, 'Roster created successfully.')
            return redirect("roster-list")

    context = {
        "form": form,
    }

    return render(request, "army_builder/rosters/create.html", context)


@login_required
def view_roster(request, id):
    """
    Fetches the View Roster page. If the user is not logged in,
    they are redirected to the login page.
    """
    context = {}

    context["data"] = get_object_or_404(Roster, id=id)

    return render(request, "army_builder/rosters/view.html", context)


@login_required
def edit_roster(request, id):
    """
    Fetches the Edit Roster page. If the user is not logged in,
    they are redirected to the login page.
    """
    roster = get_object_or_404(Roster, user=request.user, id=id)

    form = RosterForm(instance=roster)

    if request.POST:
        form = RosterForm(request.POST, instance=roster)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Roster edited successfully.")
            return redirect("roster-list")

    context = {
        "roster": roster,
        "form": form,
    }

    return render(request, "army_builder/rosters/edit.html", context)


@login_required
def delete_roster(request, id):
    """
    Fetches the Delete Roster page. If the user is not logged in,
    they are redirected to the login page.
    """
    roster = get_object_or_404(Roster, user=request.user, id=id)

    if request.POST:
        roster.delete()
        messages.success(request, "Roster deleted successfully.")
        return redirect("roster-list")

    context = {
        "roster": roster,
    }

    return render(request, "army_builder/rosters/delete.html", context)


def get_about(request):
    """
    Fetches the About page.
    """
    return render(request, "pages/about.html")
