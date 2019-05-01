from django.shortcuts import render
from django import forms
from .models import Address, Entry
from django.contrib import messages


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
    context['form'].fields["entry"].query = Entry.objects.all()
    if request.method == "POST":
        context["form1"] = EntryForm(request.POST)
        context["form"] = AddressForm(request.POST)
        if context["form1"].is_valid():
            entry = context["form1"].save()
            messages.info(request,"Entry {} salvado".format(entry.id))
        if context["form"].is_valid():
            entry = context["form"].save()
            messages.info(request,"Address {} salvado".format(entry.id))

    context["addresses"] = Address.objects.all()
    return render(request, "base.html", context)