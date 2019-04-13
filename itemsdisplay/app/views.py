from django.shortcuts import render

# Create your views here.
from app.models import Items, Register


def index(request):
    it=Items.objects.all()
    return render(request,"index.html",{"it":it})


def select(request):
    type=request.GET.get('type')
    print("1",type)
    im=Items.objects.filter(Idno=type)
    print("4",im)
    return render(request,"show.html",{"type":type,"im":im})




def ulogin(request):
    type=request.POST.get("type")
    print("2",type)
    uname=request.POST.get("l1")
    upass=request.POST.get("l2")
    reg=Register.objects.filter(Name=uname,Password=upass)
    global regname
    regname = uname
    print("0",regname)
    if reg:
        reg=Register.objects.get(Name=uname)
        itt=Items.objects.all()
        print("2",itt)
        print("3",reg)
        return render(request,"display.html",{"type":type,"reg":reg,"itt":itt})
    else:
        return render(request,"login.html",{"mes":"invalid"})

def register(request):
    # type='ureg'
    return render(request,"register.html",)


def uregister(request):
    name=request.POST.get("r1")
    contact=request.POST.get("r2")
    password=request.POST.get("r3")
    reg=Register(Name=name,Password=password,Contact=contact)
    reg.save()
    return render(request,"login.html",{"reg":reg,"msg":"saved"})


def log(request):
    return render(request,"login.html")


def choose(request):
    type=request.GET.get("type")
    iti=Items.objects.filter(Idno=type)
    print("5",iti)
    return render(request,"choose.html",{ "type":type,"iti":iti})


def buy(request):
    type='buybuy'
    ty=request.GET.get("type")
    iit=Items.objects.filter(Idno=ty)
    print("6",iit)
    return render(request,"choose.html",{"iit":iit,"type":type})

import datetime
def pay(request):
    type="pyp"
    key=request.GET.get('type')
    print("8",key)
    ii=request.GET.get("idno")
    imt=Items.objects.filter(Idno=ii)
    print("7",imt)
    da=datetime.datetime.today()
    wa = request.GET.get("way")
    print("8", wa)
    return render(request,"choose.html",{"imt":imt,"key":key,"type":type,"da":da,"wa":wa})