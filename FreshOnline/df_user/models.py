from django.db import models
from db.base_model import BaseModel # 导入抽象模型类
# Create your models here.



class Passport(BaseModel):
    '''
    账户类
    '''
    username = models.CharField(max_length=20, help_text='用户名')
    password = models.CharField(max_length=40, help_text='密码')
    email = models.EmailField(help_text='邮箱')


    class Meta:
        db_table = 's_user_account' # 修改默认表名
