from django.shortcuts import render
from django import forms
from .models import Address, Entry



class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ()

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ()

def home(request):
    context = {
        'form': AddressForm(),
        'form1': EntryForm()
    }
    if request.POST and context["form1"].is_valid() \
                and context["form"].is_valid():
        pass

    return render(request, "base.html", context)