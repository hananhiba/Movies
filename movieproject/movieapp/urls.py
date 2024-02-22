
from django.urls import path

from .  import views
app_name='movieapp'

urlpatterns = [
    path('',views.fun,name='fun'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]
