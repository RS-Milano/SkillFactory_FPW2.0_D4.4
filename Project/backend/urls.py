from django.urls import path
from .views import PostList, PostDetail, PostSearch, AddPost, PostEdit, DeletPost

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search', PostSearch.as_view()),
    path('addpost', AddPost.as_view()),
    path('<int:pk>/edit', PostEdit.as_view()),
    path('<int:pk>/delet', DeletPost.as_view()),
]
