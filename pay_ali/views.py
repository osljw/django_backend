from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from alipay import AliPay

import json

with open("C:\\Users\\tests\\Documents\\alipay\\app_private_key.pem", 'r') as f:
    app_private_key_string = f.read()
    app_private_key_string = '-----BEGIN PRIVATE KEY-----\n' + app_private_key_string + '\n-----END PRIVATE KEY-----'

with open("C:\\Users\\tests\\Documents\\alipay\\alipay_public_key.pem", 'r') as f:
    alipay_public_key_string = f.read()
    alipay_public_key_string = '-----BEGIN PUBLIC KEY-----\n' + alipay_public_key_string + '\n-----END PUBLIC KEY-----'


def alipay_mobile(request):
    alipay = AliPay(
        appid="2021003197601960",
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或 RSA2
        debug=True  # False 表示在线支付环境，True 表示沙箱测试环境
    )
    order_data = {
        'out_trade_no': '20190901000000001',
        'total_amount': 98.00,
        'subject': '商品名称',
        'body': '商品详情说明',
        'product_code': 'QUICK_WAP_PAY',
    }
    order_string = alipay.api_alipay_trade_wap_pay(
        **order_data
    )
    # order_string = alipay.api_alipay_trade_page_pay(
    #     **order_data
    # )

    # https://openapi.alipaydev.com/gateway.do? + order_string
    # return HttpResponse(order_string)
    return JsonResponse({
        'order_string': order_string,
    })


def alipay_pc(request):
    value = request.GET.get('value')
    alipay = AliPay(
        appid="2021003197601960",
        app_notify_url=None,  # 默认回调地址
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type='RSA2',
        debug=False,  # 设置为True时会向沙箱环境发起请求
    )

    # 支付宝 API 所需参数，具体参考支付宝文档：
    subject = '测试订单'
    out_trade_no = '20210528000123912'  # 订单号，需要实际情况生成
    total_amount = value

    order_string = alipay.api_alipay_trade_precreate(
        subject=subject,
        out_trade_no=out_trade_no,
        total_amount=total_amount,
        notify_url=request.build_absolute_uri('/notify/'),  # 回调地址
    )
    print("order_string:", order_string)

    pay_url = json.loads(order_string)['alipay_trade_precreate_response']['qr_code']

    print("pay_url:", pay_url)

    return JsonResponse({'pay_url': pay_url})