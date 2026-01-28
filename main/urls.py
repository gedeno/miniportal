from django.urls import path
from .  import views

urlpatterns = [
    path('home/', views.home, ),
    path('teach/', views.teach),
    path('subject/<int:id>/',views.Subject),
    path('teach2/<int:id>/',views.teach2),
    #path('disp/',views.display),
    #path('display2/<str:id_no>/',views.display2),
    
    
]