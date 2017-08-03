from django.db import models
from db.base_model import BaseModel # 导入抽象模型类
# Create your models here.

# 继承于models.Manager
class PassportManager(models.Manager):
    # 账户模型管理器类,(抽取方法)
    # add_one_passport方法的作用是创建一个新用户，用于接收用户传进来的信息
    def add_one_passport(self, username, password, email):
        # 获取模型管理器对象所在模型类的名字
        cls = self.model
        # 创建模型passwort所对应的对象
        obj = cls()
        # 给obj对象创建对象属性并赋值
        obj.username = username
        obj.password = password
        obj.email = email

        # 保存进数据库
        obj.save()
        return obj

    # 在校验用户名的时候只需要传进来用户名即可
    # 但是在登录的时候，需要用户名和密码来查
    # 一个函数做两件事：1：校验用户名（这时的password不需要管），2：登录验证
    def get_one_passport(self, username, password = None):
        # 根据用户名和密码查找账户信息
        # 操作passport.objects.get 是可能会出现异常的。
        # 当查找不到的时候会抛出DoesNotExist异常
        try:
            if password:
                # 根据用户名和密码来查
                obj = self.get(username = username, password = password)
            else:
                # 只根据用户名来查，password为None
                obj = self.get(username = username)
        # 找不到passport类时会报异常。
        except self.model.DoesNotExist:
            # 代表什么都没有
            obj = None
        # 调用这个方法拿到返回值来验证用户名或者验证登录
        return obj


class Passport(BaseModel):
    '''
    账户类
    '''
    username = models.CharField(max_length=20, help_text='用户名')
    password = models.CharField(max_length=40, help_text='密码')
    email = models.EmailField(help_text='邮箱')


    class Meta:
        db_table = 's_user_account' # 修改默认表名
