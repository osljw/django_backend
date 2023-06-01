from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from alipay import AliPay

import json

with open("C:\\Users\\tests\\Documents\\alipay\\app_private_key.pem", 'r') as f:
    app_private_key_string = f.read()
    # app_private_key_string = 'MIIEpAIBAAKCAQEAoHjuV5EdBvlbYMfazc1m+zG9CcS+/Kzyq+nqsqSNuN9S+zfZeER3zxX6JWJrCbLHifITqHd6ktmbctBNXKGg5WnKB0XPFkki+0iMUuWFd6Vx5E9oFgVSX64YvMpO4bOPj3qbdTNtg81f2YLvZNwNBVJmz3RGkS7hwmdZxPpSFRFGQXQWj/VJqkxXZu8zHqMCpN9d2bfEo7SoNXyr+Sin+2Rb7GEitpQnsng0Hnz3NueXUsZ783ArYxIO0jo7CcRonC3YVV2kl4mqIPQpLJnvnqAycv1kSY9jjwD4so1GUtfdeiUvMeatTKDVPn37xa2HkwyjsgxY9CmwsRJFjcCicQIDAQABAoIBADqYLZ8303uKbX1HPHPNPn8WSEpa1sn4dJulTBdy0nTgxrIIUJYDmiO5iJ9B8oeWChoqlFb9WXppjsM7oCPkuJVMLYK+UMF4bxeGBAb42+U2OgH9pKn1w4BAV7QHwwnSwObJBB6laqWnxgnsL3GKkA6TagryEBpPHgwYJMUyCeq60RUzum/LX4IA83SUyGGjegj1alUld2C6BYV5k7oH5TP6vNjQiJwp0qbXZpr5gO08dlu0xIU5XzyOTo93uqSD5cdETGku0PLqKE5DkpcyXTBOg7iEAn9AI1OJWeXOwUCkNlWYOM2Vyrgego8+7LDq56owTkW0F5FlslyFap1clkkCgYEA4qT4m4yyFs1jCtNgymxJAYBYCZssdeVaY16t26a54Ele2aGCNc4q/zDoHuKNFP26/1a8MjDdyUfvdxtMgdRXYeElRrdHs6zfrUoKA9K+fGN41NJPVfioQH1OohbYAyReJhO31+C8o2DRLL9KEN594dhM24WTd7a+Hlld85QW8NsCgYEAtUHXYQsd5FjlDBLAW5ObgBQ1pdH7/kskmxG9ypIcSUpsir+iS8pd1McIwsVcVvjShaAMQQ1UZRStsh6LiYlQEyCvDXCxNWLKC/ux+RMywxKiJ9PneKOtGwcesT/kV9W7TigS8JkiE4ddzeC652rRKFa5caC7lAG75NIiFu+jBaMCgYEA1hrQfGmaZ24ZTUXIXxGSmid7g3+irbFABTWQ+jpzx8yoHOG1V0zvU2oJLfwJGTZk7Ags+yEss5QQRS11xgQplF6Tz00fID6Eg3i5I0l4B5wUrsAKkIW5tEpr+TWpVLaLdl8UQoycx56TnDkNKAh3VN34JTz3xZTN32+/EHbqgRcCgYEAsi0Z8oxCAyEbbyXTr3HHTz0Oi4WCiDQHtOPYxJOieK1PS4kbmhNA75QD2aq2ncwU7kQpJ51Z089i+5ApLLctXtAnJDgeCtOkt+jgx26G3NmpSyt0A9Qpq0Lxed3Lskgoyqh8DcUKiVXs8R+zux72oge2XataGSEnOcUSu6cvgq8CgYB6FYZ1vv/cVdnatP3hTPXFMvCINcgtEoU30CIehsf2tK/T/zBTrXBWw7dOPdaUgUZKhiPQzfMdkE7pZ4WZJ78fpr+Y88idF9d2okDjFFA4iCOjA8tNKYftgMc3PDbmRq7263VWyiGNz/NU0J/1DhLkW1MwlNx4aF4FLoq2E6+9gA=='
    app_private_key_string = '-----BEGIN RSA PRIVATE KEY-----\n' + app_private_key_string + '\n-----END RSA PRIVATE KEY-----'

with open("C:\\Users\\tests\\Documents\\alipay\\alipay_public_key.pem", 'r') as f:
    alipay_public_key_string = f.read()
    # alipay_public_key_string = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAquP601PpMj0i6xi7EZTkXJNoLe+qK/GozDsq/h1zyDjtW3/LOG1WCBnPL7x656/m9XzCIONKQ+BnG/HMQQNkcJbhzF/vm+TIXSp5U3sDdgg2y83s0jJJSTqLM89ABMrBklQJUVan3+Cj365GnXY0ZbkPplqsccqnAJorBZdXj8bJiLgEZzM9WOIvH571M5hmYkkmpXg9LA4oC9fjbJ9hgrZfge7bJ4XPFc3H5uJy4unriz38SDwK9iHxxWjOLST1NiNqBd12ydOtJ2n2KggmB+JhDfcej2jzgkOJZaamIbWpBch6w476UymhW7o4cYoAMnG1DIcg+zCimLYxLdh7gQIDAQAB'
    alipay_public_key_string = '-----BEGIN PUBLIC KEY-----\n' + alipay_public_key_string + '\n-----END PUBLIC KEY-----'

print("app_private_key_string:", app_private_key_string)
print(alipay_public_key_string)


def alipay_mobile(request):
    alipay = AliPay(
        appid="2021000122675481",
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
        appid="2021000122675481",
        app_notify_url=None,  # 默认回调地址
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type='RSA2',
        debug=True,  # 设置为True时会向沙箱环境发起请求
    )

    # 支付宝 API 所需参数，具体参考支付宝文档：
    subject = '测试订单'
    out_trade_no = '20210528000123913'  # 订单号，需要实际情况生成
    total_amount = 0.1



    # # 发送 API 请求并获取响应结果
    # response = alipay.api_alipay_trade_precreate(
    #     subject=subject,
    #     out_trade_no=out_trade_no,
    #     total_amount=total_amount,
    # )

    # # 解析响应结果并检查是否请求成功
    # content = response["alipay_trade_precreate_response"]
    # if content["code"] != "10000":
    #     return HttpResponse("请求支付宝创建扫码付款订单失败！")
    
    # # 获取二维码链接并生成图片
    # qr_code = content["qr_code"]
    # print("content:", content, qr_code)

    order_string = alipay.api_alipay_trade_page_pay(
        subject=subject,
        out_trade_no=out_trade_no,
        total_amount=total_amount,
        notify_url=request.build_absolute_uri('/notify/'),  # 回调地址
    )

    print("notify_url:", request.build_absolute_uri('/notify/'))
    print("order_string:", order_string)

    alipay_gateway = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do?'
    return JsonResponse({
        'pay_url': alipay_gateway + order_string,
    })