#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/25 17:30
from django.http import JsonResponse
from django.views.decorators.http import require_GET,require_POST
from django.conf import settings
from .models import Account
from utils import restful
import requests,json

@require_POST
def auth_wx_login(request):
    code = request.POST.get("code",None)
    a = request
    pass
    if code:
        url = settings.AHEN_URL.format(settings.WEAPPID,settings.WEAPPSEC,code)
        resp = json.loads(requests.get(url).text)
        openid = resp.get("openid")
        session_key = resp.get("session_key")
        unionid = resp.get("unionid")
        # account = Account.objects.filter(openid=openid).first()
        print(openid,session_key,unionid)
    #     if account:
    #         return restful.paramerror(msg='已经注册了')
    #     else:
    #         Account.objects.create_user(openid)
    # else:
        return restful.paramerror(msg='请传递code参数')
