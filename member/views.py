from django.shortcuts import render, redirect
from django.http import JsonResponse
from member.models import Member 
from member.forms import MemberForm
from django.utils import timezone

def write(request):
    return render(request, "member\member_write.html")

def logon(request):
    return render(request, "member\logon.html")

def logout(request):
    return render(request, "member\logout.html")

def save(request):
    try:
        memberForm = MemberForm(request.POST)
        member = memberForm.save(commit=False) 
        member.wdate = timezone.now()
        member.save()
        result = {"result":"success"}
    except Exception as ex:
        print(ex)
        result = {"result":"fail"}

    return JsonResponse(result)

def logon_proc(request):
    try:
        userid = request.POST.get("userid")
        password = request.POST.get("password")
        member = Member.objects.get(userid=userid, password=password) #이미 사용중인 아이디임 사용못함
        request.session["userid"] = member.userid
        request.session["username"] = member.username
        request.session["email"] = member.email
        
        #세션에 저장해야 한다 
        result = {"result":"success"}
    except:
        result = {"result":"fail"} #아이디 안쓰고 있음 사용가능 
    return JsonResponse(result)

def logout_proc(request):
    request.session["userid"] = None
    request.session["username"] = None
    request.session["email"] = None
    result = {"result":"success"}
    return redirect("index:index")
 

def idcheck(request):
    userid = request.POST.get("userid")
    print(userid)
    #디비에가서 확인 
    try:
        Member.objects.get(userid=userid) #이미 사용중인 아이디임 사용못함
        result = {"result":"fail"}
    except:
        result = {"result":"success"} #아이디 안쓰고 있음 사용가능 
    return JsonResponse(result)

