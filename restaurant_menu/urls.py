from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.MenuList.as_view(), name="home"),
    path('about/', views.about, name="about"),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



