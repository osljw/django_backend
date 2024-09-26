
# 安装

```
pip install -r requirements.txt
```

```
python manage.py makemigrations
python manage.py migrate
```

# 运行
```
python manage.py runserver

python manage.py runserver 0.0.0.0:8000

uvicorn django_backend.asgi:application --host 192.168.0.106 --reload 

uvicorn django_backend.asgi:application --host 192.168.0.103 --workers 4
```

# 新建app
```
python manage.py startapp user_chat
```

```
python manage.py makemigrations
python manage.py migrate
```

# app

article: 文章
upload: 图片上传(tinymce upload)


# 用户管理

`pip install djangorestframework`

# websocket

```
pip install channels
```

# 数据

扫描mkdocs目录， 生成Article数据库
Article数据库


# markdown

数学公式
```
pip install python-markdown-math
```