from django.shortcuts import render,redirect
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from df_user.models import Passport
from django.http import JsonResponse,HttpResponseNotAllowed
from hashlib import sha1
# Create your views here.

@require_http_methods(['GET','POST'])
def register(request):
    '''
    展示用户注册页面
    '''
    return render(request, 'register.html')

@require_POST
def register_handle(request):
    '''
    注册用户信息
    '''
    # 1：接收用户的注册信息
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    # 2：Passport的add_one_passport方法来创建新用户。
    # 让视图view函数只处理业务逻辑
    Passport.objects.add_one_passport(username=username,password=password,email=email)
    # 重定向到首页
    return redirect('/')

def check_username_exist(request):
    '''
    校验用户名是否已经被注册
    '''
    # 1：接收用户名
    username = request.GET.get('username')
    # 2：调用get_one_passport方法来校验用户名；拿到返回值来判断是否已经被注册
    #    操作Passport.object.get是可能出现异常的。
    passport = Passport.objects.get_one_passport(username = username)

    if passport:
        # 用户名已经被注册
        return JsonResponse({'res':0})
    else:
        # 用户名可用
        return JsonResponse({'res':1})









