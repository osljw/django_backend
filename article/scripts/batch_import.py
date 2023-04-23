#-*- utf-8 -*-
import os
import glob
from pathlib import Path


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_backend.settings")
import django
django.setup()

from article.models import Article, ArticleCategory
from user_auth.models import User

base_dir='E:\\git_code\\osljw_docs\\docs'
#base_dir='E:/workspace/vue_work/django_backend/osljw_docs/docs'

# for path in Path(base_dir).rglob('*'):
#     print(path.absolute(), path.relative_to(base_dir))

def dir_dfs(base_dir, cur_dir, cat_list, level):
    for path in Path(cur_dir).glob('*'):
        if not path.is_dir():
            continue
        if path.name == 'media':
            continue

        cat = ArticleCategory(
            title = path.name,
            parent_title = os.path.basename(cur_dir),
            path = path.relative_to(base_dir),
            level = level
        )
        cat_list.append(cat)
        dir_dfs(base_dir, path.absolute(), cat_list, level + 1)


def get_article_category(base_dir):
    cat_list = []
    level = 1
    dir_dfs(base_dir, base_dir, cat_list, level)
    return cat_list


def get_article():
    article_list = []
    user = User.objects.get(username="admin")
    cat = ArticleCategory.objects.get(title="algorithm")
    for path in Path(base_dir).rglob('*.md'):
        #old_article = Article.objects.get(title=path.name)

        article = Article(
            id = Article.objects.get(title=path.name).id,
            auth = user,
            category = cat,
            title = path.name,
            body = open(path, 'r', encoding='utf-8').read(),
        )
        # path.relative_to(base_dir)
        article_list.append(article)
        if len(article_list) > 4:
            break
    return article_list
    


if __name__ == '__main__':
    article_list = get_article()
    # Article.objects.bulk_create(article_list, ignore_conflicts=True)
    Article.objects.bulk_update(article_list, fields=["body"])

    # cat_list = get_article_category(base_dir)
    # for cat in cat_list:
    #     print(cat)
    # ArticleCategory.objects.bulk_create(cat_list)