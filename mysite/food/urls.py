from . import views
from django.urls import path

app_name = 'food' # NAMESPACING
urlpatterns = [
    #food
    path('', views.index, name ='index'),
    #food/1
    path('<int:item_id>/',views.detail,name='detail'),
    path('item/', views.item, name='item'),
    # add items
    path('add', views.create_item,name='create_item'), 
]