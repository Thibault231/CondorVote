# coding: utf-8
"""Run the views for Account APP.
Views:
-myaccount(request):@login_required
-account_creation(request)
-connexion(request)
-deconnexion(request):@login_required
-delete_user(request):@login_required
-delete_confirmation(request):@login_required
-modify_account(request):@login_required
"""
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import Account
from .forms import ConnexionForm, CountCreationForm, CountModificationForm


@login_required
def myaccount(request):
    """Display the user saved substitutes.
    @login_required
    Arguments:
    -request {GET}
    Returns:
    -template -- myaccount.html
    """
    user = request.user
    try:
        1 == 1
        desk_list = True
    except IndexError:
        desk_list = False
    context = {
        'user': user,
        'desk_list': desk_list
    }
    return render(request, 'account/myaccount.html', context)


def account_creation(request):
    """Manage the account creation.
    Arguments:
    -request {POST}
    Returns:
    -template -- account_creation.html
    -template -- myaccount.html when done
    """
    error_password = False
    error_username = False
    error_email = False
    if request.method == "POST":
        form = CountCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            school = form.cleaned_data["school"]
            departement = form.cleaned_data["departement"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if password1 == password2:
                user_control = User.objects.filter(username=username)
                if not user_control:
                    useremail_control = User.objects.filter(email=email)
                    if not useremail_control:
                        user = User.objects.create_user(
                            username=username,
                            email=email,
                            password=password1,
                            first_name=first_name,
                            last_name=last_name
                        )
                        user.save()
                        Account.objects.create(
                            user=user,
                            school=school,
                            departement=departement,
                        )

                        login(request, user)

                        return render(request, 'account/myaccount.html')

                    error_email = True

                else:
                    error_username = True
            else:
                error_password = True
    else:
        form = CountCreationForm()

    context = {
        "error_password": error_password,
        "error_username": error_username,
        "error_email": error_email,
        "form": form
    }

    return render(request, 'account/account_creation.html', context)


def connexion(request):
    """Rule the login of an anonymous user
    on an account.
    Arguments:
    -request {POST}
    Returns:
    -template -- connexion.html
    """
    error = False
    user = 0
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    context = {
        "error": error,
        "user": user,
        "form": form
    }
    return render(request, 'account/connexion.html', context)


@login_required
def deconnexion(request):
    """Rule the deconnexion of an connected user.
    @login_required
    Arguments:
    -request {GET}
    Returns:
    -template -- index.html
    """
    logout(request)
    return render(request, 'common/index.html')


@login_required
def delete_confirmation(request):
    """Ask for confirmation user deleting
    account.
    Arguments:
    -request {POST}
    Returns:
    -template -- delete_confirmation.html
    """
    return render(request, 'account/delete_confirmation.html')


@login_required
def delete_user(request):
    """Delete User account.
    Arguments:
    -request {POST}
    Returns:
    -template -- delete_done.html
    """
    try:
        user = request.user
        user.delete()
        logout(request)
    except ValueError:
        print(request, "The user not found")
    return render(request, 'account/delete_done.html')


@login_required
def modify_account(request):
    """Manage the account modification.
    Arguments:
    -request {POST}
    Returns:
    -template -- account_modify.html
    -template -- myaccount.html when done
    """
    user = request.user
    error_username = False
    account_modificate = False

    if request.method == "POST":
        form = CountModificationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            school = form.cleaned_data["school"]
            departement = form.cleaned_data["departement"]

            user_control = User.objects.filter(username=username)
            if not user_control:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.account.school = school
                user.account.departement = departement
                user.save()

                account_modificate = True
            else:
                error_username = True
    else:
        form = CountModificationForm()

    context = {
        "account_modificate": account_modificate,
        "error_username": error_username,
        "form": form
    }

    return render(request, 'account/modify_account.html', context)
