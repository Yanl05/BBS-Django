import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs.settings")
    import django
    django.setup()

    from blog import models
    from django.db.models import Count
    # 查询某个分类对应的文章
    user = models.UserInfo.objects.filter(username="yanlei").first()
    print(user)
    blog = user.blog
    print(blog)
    # yanlei站点下 所有的分类

    # ret = models.Category.objects.filter(blog=blog)
    # for i in ret:
    #     print(i.title, i.article_set.all().count())

    ret = models.Category.objects.all().annotate(c=Count("article")).values("title", "c")#filter(blog=blog)# .annotate(c=Count("article__category"))
    print(ret)
