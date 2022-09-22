from django.urls import path
from .views import indexfunc, goodfunc,DodemoCreate,detailfunc

urlpatterns = [
    path('index/', indexfunc, name='index'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('create/', DodemoCreate.as_view(), name='create'),
]