from django.shortcuts import render
from .models.hearthlight_member import Member
# Create your views here.

def member_profile(request,id):

    # Get the member id from the URL /member/id
    
    print(">>>"+str(id)+"<<<")
    member = Member.objects.get(id=id)
    return render(request, 'core/member_page.html', {'member': member})