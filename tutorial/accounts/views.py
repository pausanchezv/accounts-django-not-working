# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)


def home(request):
    return render(request, 'accounts/home.html')


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            #return redirect('accounts')
            return HttpResponseRedirect(reverse('accounts:profile'))

        else:
            return HttpResponseRedirect(reverse('accounts:home'))


    else:
        form = UserCreationForm()

        args = {
            'form': form
        }

        return render(request, 'accounts/register.html', args)


def view_profile(request):

    args = {
        'user': request.user
    }
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:view_profile'))

    else:
        form = EditProfileForm(instance=request.user)
        args = {
            'form': form
        }
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('accounts:view_profile'))
        else:
            return HttpResponseRedirect(reverse('accounts:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)
        args = {
            'form': form
        }
        return render(request, 'accounts/change_password.html', args)