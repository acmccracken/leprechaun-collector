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
]