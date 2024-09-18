from django.urls import path
from . import  views

urlpatterns =[
    path('', views.MenuList.as_view(), name="home")

]
""",
  path('', views.MenuItemDetail.as_view(), name="home")"""