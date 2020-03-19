from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('leprechauns/', views.leprechauns_index, name='index'),
    path('leprechauns/<int:leprechaun_id>/', views.leprechauns_detail, name='detail'),
    path('leprechauns/create/', views.LeprechaunCreate.as_view(), name='leprechauns_create'),
    path('leprechauns/<int:pk>/update/', views.LeprechaunUpdate.as_view(), name='leprechauns_update'),
    path('leprechauns/<int:pk>/delete/', views.LeprechaunDelete.as_view(), name='leprechauns_delete'),
    path('leprechauns/<int:leprechaun_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('weapons/', views.WeaponList.as_view(), name='weapons_index'),
    path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapons_detail'),
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapons_create'),
    path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapons_update'),
    path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapons_delete'),
    path('leprechauns/<int:leprechaun_id>/assoc_weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc_weapon')
]