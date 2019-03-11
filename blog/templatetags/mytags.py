from django import template
from blog import models
from django.db.models import Count

register = template.Library()

@register.inclusion_tag("left_menu.html")
def get_left_menu(username):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    # 页面左侧分类栏
    # 我的文章分类及每个每类下的文章数
    # 将我的文章按照我的分类 分组，并 统计出每个分类下面的文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 我的标签
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 时间归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive_ym": "date_format(create_time, '%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")

    # return category_list,tag_list,archive_list,
    # 需要返回字典格式的
    return {
        "category_list": category_list,
        "tag_list": tag_list,
        "archive_list": archive_list,
    }