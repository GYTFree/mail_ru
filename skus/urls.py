from django.urls import path, include
from skus import views


urlpatterns = [
    path('', views.search_by_sku),
    path('regist/', views.regist_user, name='regist'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('sku/<slug:sku_id>/', views.sku_detail, name='sku_detail'),
    path('buyer/<slug:id>/', views.buyer, name='buyer'),
    path('change_passwd', views.change_passwd, name='change_passwd'),
    path('search_by_sku', views.search_by_sku, name="search_by_sku"),
    path('search_by_spu', views.search_by_spu, name="search_by_spu"),
    path('search_orders', views.search_orders, name="search_orders"),
]