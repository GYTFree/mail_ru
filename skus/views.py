from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from skus.tools import ShopSession
from skus.models import Client
from skus.models import Spu, Sku
from skus.myForms import DemoForms


# Create your views here.

def regist_user(request):
    if request.method == 'POST':
        regist_form = DemoForms(request.POST)
        if regist_form.is_valid():
            err_msg = {}
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            re_password = request.POST.get('re_password')
            has_user = User.objects.filter(username=username)
            has_email = User.objects.filter(email=email)
            if has_user:
                err_msg['username'] = "该用户名已被注册"
            if has_email:
                err_msg['email'] = "该邮箱已被注册"
            if password != re_password:
                err_msg['passwd'] = '两次输入的密码不一致！'
            if not has_user and not has_email and password == re_password:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect(reverse('login'))
            return render(request, 'regist.html', context={'err_msg': err_msg})
        else:
            return render(request, 'regist.html', context={'forms': regist_form})
    return render(request, 'regist.html')


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('search_by_sku'))
    return render(request, 'login.html')


def my_logout(request):
    logout(request)
    return redirect(reverse('login'))


def sku_detail(request, sku_id):
    sku = Sku.objects.get(id=sku_id)
    sku_all_images = sku.all_images
    sku_all_images = sku_all_images[1:len(sku_all_images) - 1]
    sku_all_images.replace("'", "")
    sku_all_images = sku_all_images.split(',')
    sku_all_images = [img.strip("'").strip().strip("'") for img in sku_all_images]
    return render(request, 'sku_detail.html', context={'sku': sku, 'all_images': sku_all_images})


def search_by_sku(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    else:
        username = request.user
    shops = Client.objects.values('shop')
    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        item = request.POST.get('item')
        session = ShopSession(shopname)
        params = {}
        params['sku'] = item
        resp = session.get_sku_by_name(params)
        if resp:
            all_images = resp.get('all_images')
            sku = Sku.objects.filter(id=resp['id'])
            if sku:
                sku.update(**resp)
            else:
                Sku.objects.create(**resp)
            return render(request, 'sku_info.html',
                          context={'sku': resp, 'all_images': all_images, 'username': username})
        else:
            return render(request, 'sku_info.html', context={'shops': shops, 'username': username})
    return render(request, 'search_by_sku.html', context={'shops': shops, 'username': username})


def search_by_spu(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    else:
        username = request.user
    shops = Client.objects.values('shop')
    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        item = request.POST.get('item')
        session = ShopSession(shopname)
        params = {}
        if int(request.POST.get('spu_target')) == 0:
            params['id'] = item
        else:
            params['parent_sku'] = item
        resp = session.get_skus(params)
        if resp:
            product = resp.json()['data']['Product']
            product['shop'] = shopname
            spu_keys = ['id', 'shop', 'name', 'parent_sku', 'num_sold', 'num_saves', 'review_status',
                        'description', 'brand', 'upc', 'landing_page_url', 'main_image', 'enabled',
                        'is_promoted', 'original_image_url', 'date_uploaded', 'last_updated',
                        'wish_express_country_codes', 'shipping_category', ]
            spu = {}
            for key in spu_keys:
                spu[key] = product[key]
            spu_id = spu.get('id')
            if not Spu.objects.filter(id=spu['id']):
                Spu.objects.create(**spu)
            else:
                spu.pop('id')
                Spu.objects.update(**spu)
            for variant in product['variants']:
                variant['Variant']['product_id'] = spu_id
                sku = Sku.objects.filter(id=variant['Variant']['id'])
                if not sku:
                    Sku.objects.create(**variant['Variant'])
                else:
                    sku.update(**variant['Variant'])
            context = {'shops': shops, 'product': product, 'username': username}
        else:
            context = {'shops': shops, 'product': None, 'username': username}
        return render(request, 'spu_info.html', context=context)
    return render(request, 'search_by_spu.html', context={'shops': shops, 'username': username})
