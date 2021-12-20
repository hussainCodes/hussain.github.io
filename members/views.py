from django.shortcuts import render
from .models import Member
from .forms import MemberForm
from django.http import HttpResponseRedirect

def viewMembers(request):
    members = Member.objects.all()
    return render(request, 'viewMembers.html', {'members': members})

def addMember(request):

    form = MemberForm(request.POST or None)
    if form.is_valid():
            form.save()
    return render(request, 'addmember.html', {'form': form})


def updateMember(request, id):
    member = Member.objects.get(id=id)
    form = MemberForm(request.POST, instance=member)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/members')
    return render(request, 'updatemember.html', {'member': member})

def deleteMember(request, id):
    form = Member.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/members')
# Create your views here.
