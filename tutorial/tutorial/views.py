from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


def base_redirect(request):
    #return redirect('accounts/')
    return HttpResponseRedirect(reverse('accounts:home'))
