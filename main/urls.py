from django.urls import path
from .  import views

urlpatterns = [
    path('home/', views.home, ),
    path('teach/', views.teach),
    path('teach2/<int:id>/',views.teach2),
    path('disp/',views.display)
    
]