from django.conf.urls import url, include
from blog import views

urlpatterns = [
    # 添加新文章，富文本编辑器
    url(r'backend/add_article/', views.add_article),
    # 点赞或反对
    url(r'up_down/', views.up_down),
    # 提交评论
    url(r'comment/', views.comment),
    url(r'comment_tree/(\d+)/', views.comment_tree),
    # 文章详情
    url(r'(\w+)/article/(\d+)/$', views.article_detail),
    # home(request, arg) arg捕获分组中的数据 arg名字可以改为username
    url(r'(\w+)', views.home),
    # 点赞或反对
    url(r'up_down/', views.up_down),
]