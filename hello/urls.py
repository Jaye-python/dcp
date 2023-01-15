from django.urls import path
from hello import views
from .views import ArticleListView

urlpatterns = [
    # path("", views.home, name="home"),
    path('', ArticleListView.as_view(), name='article-list'),
]