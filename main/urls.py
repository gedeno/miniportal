from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home, ),
    path('teach', views.teach),
    path('teach2',views.teach2),
    path('disp',views.display)
    
]