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

def show_entries(request):
    context = dict(entries=Entry.objects.all().order_by("-id"))
    return render(request, "entries.html", context)

def show_addresses(request):
    context = {
        'addresses': Address.objects.all()
    }
    return render(request, "addresses.html",context)

# fix the contrib.messages update
def show_messages(request):
    return render(request, "_messages.html")

def save_entry(request, form=EntryForm, model="entry"):
    context = {}
    import time
    time.sleep(2)
    if request.method == "POST":
        context["form"] = form(request.POST)
        if context["form"].is_valid():
            entry = context["form"].save()
            messages.info(request,"{} {} salvado".format(model, entry.id))
    return render(request,"form.html", context)

def home(request):
    context = {
        'form': AddressForm(),
        'form1': EntryForm()
    }
    context['form'].fields["entry"].query = Entry.objects.all()
    if context["form"].is_valid():
        entry = context["form"].save()
        messages.info(request,"Address {} salvado".format(entry.id))

    context["addresses"] = Address.objects.all()
    return render(request, "base.html", context)