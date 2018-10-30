from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.NewsListView.as_view(),
        name='news_list'
        ),
    path(
        '<int:pk>/edit/',
        views.NewsUpdateView.as_view(), name='news_edit'
        ),
    path(
        '<int:pk>',
        views.NewsDetailView.as_view(),
        name='news_detail'
        ),
    path(
        '<int:pk>/delete/',
        views.NewsDeleteView.as_view(),
        name='news_delete'
        ),
]
