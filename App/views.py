from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Store, Image, Shopping_Cart, Detailed_list
from django.contrib import auth
import hashlib
import csv
from django.db.models import Min, Max, Sum


def md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def index(request):
    try:
        value = request.session['name']
        if value:
            return render(request, 'test.html', {'user_list': value})
            return HttpResponseRedirect('/store_post')
    except:
        return render(request, 'test.html')


def index2(request):
    from . import models
    A = []
    all_content = models.Store.objects.order_by("-New_Store")
    try:
        value = request.session['name']
        if value:
            return render(request, 'index.html', {'content': all_content, 'user': value})
    except:
        return render(request, 'index.html', {'content': all_content})


def register(request):
    return render(request, 'zhuce.html')


def zhuce(request):
    from . import models
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_psd = request.POST['re_password']

        password_md5 = md5(password + 'the-Salt')

        try:
            if models.User.objects.get(username=username) != True:
                return HttpResponse(u'用户名已注册')
        except:
            if password != re_psd:
                    return HttpResponse(u'两次输入不一样')
                  
            data = User(username= username, password= password_md5)
            data.save()
            return HttpResponseRedirect('/store_post')


def log(request):
    return render(request, 'log.html')


def login(request):
    return render(request, 'login.html')


def denglu(request):

    if request.method == 'POST':
        user = request.POST['username']
        psd = request.POST['password']
        password = md5(psd + 'the-Salt')
        from . import models

        try:
            data = models.User.objects.get(username=user)

            if password != data.password:
                return HttpResponse(u'密码不正确')
            request.session['name'] = user
            response = HttpResponseRedirect('/store_post')
            # response.set_cookie('username', user)
            return response
        except:
            return HttpResponse(u'发生错误,可能是用户名填写不正确')

    else:
        return HttpResponse(u'Error: Not POST')


def store(request):
    if request.method == 'POST':
        context = request.POST['content']
        with open('test.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["commodity", "Unit Price"])

            writer.writerow([context, "3988"])
        return HttpResponse('测试')


def Administrators(request):
    return render(request, 'log.html')


def new(request):
    if request.method == 'POST':
        return render(request, 'div.html')
    return HttpResponseRedirect('/store_post')


def div(request):
    if request.method == 'POST':
        new_store = request.POST['new_store_name']
        unit = request.POST['unit']
        images = request.FILES.get('img')

        print(images)

        data = Store(New_Store= new_store, Unit= unit, Images= images)
        data.save()

        return HttpResponse(u'ok')


def img(request):
    return render(request, 'img.html')


def images(request):
    if request.method == 'POST':
        file = request.POST['file']
        file = 'C:/Users/Yenda/Pictures' + file
        data = Image(images= file)
        data.save()
        return HttpResponse(u'OK')


def id(request, page):
    page = int(page)
    data = Store.objects.get(id=page)
    Images = data.Images

    return render(request, 'details.html', {'Images': Images})


def ShoppingCart(request):
    if request.method == 'POST':
        image = request.POST['image']
        name = request.POST['name']
        unit = request.POST['unit']

        try:
            value = request.session['name']
            if value:
                print(image)
                Data = Detailed_list(UserName= value, Image=image, Store_Name=name, Unit=unit)
                Data.save()
        except:
            return HttpResponse(u'您需要登陆')

        return HttpResponse(u'OK')


def Car(request):
    if request.method == 'POST':
        try:
            value = request.session['name']
            Data = Detailed_list.objects.filter(UserName=value)
            ZJ = Detailed_list.objects.filter(UserName=value).aggregate(Sum('Unit'))
            return render(request, 'Car.html', {'Data': Data, 'ZJ': ZJ})
        except:
            return HttpResponse(u'购物车是空的')
    value = request.session['name']
    Data = Detailed_list.objects.filter(UserName=value)
    ZJ = Detailed_list.objects.filter(UserName=value).aggregate(Sum('Unit'))
    return render(request, 'Car.html', {'Data': Data, 'ZJ': ZJ})


def self(request):
    from . import models
    all_content = models.Store.objects.order_by("-New_Store")
    value = request.session['name']
    if value == 'Administrators':
        return render(request, 'Management.html', {'list': all_content})
    else:
        value = request.session['name']
        Data = Detailed_list.objects.filter(UserName=value)
        ZJ = Detailed_list.objects.filter(UserName=value).aggregate(Sum('Unit'))
        return render(request, 'Personal.html', {'Data': Data, 'ZJ': ZJ})


def delete(request):
    from . import models
    if request.method == 'POST':
        store = request.POST['store']
        models.Store.objects.filter(New_Store = store).delete()
        return HttpResponse(u'OK')
    return HttpResponse(u'发生错误')


def logout(request):
    auth.logout(request)
    try:
        del request.session['name']
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')


# Create your views here.
