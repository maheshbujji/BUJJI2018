from django.shortcuts import render
from .models import Employee



# Create your views here.
def showindex(request):
    return render(request,"index.html")


def showdetails(request):
    try:
        fe=request.session['status']
        if fe:
            return render(request,"index.html",{"msg":"only onetime"})
        else:
            return render(request,"details.html")
    except KeyError as ke:
        return render(request,"details.html")



def details(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    cmmnt=request.POST.get("t3")

    f=Employee(name=name,cno=cno,cmmnt=cmmnt)
    f.save()
    request.session['status']=True
    return render(request,"index.html",{"msg":"datasved"})


