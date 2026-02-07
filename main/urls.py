from django.urls import path
from .  import views

urlpatterns = [
    path('home/', views.home, ),
    path('teach/', views.teach),
    path('subject/<int:id>/',views.Subject),
    path('teach2/<int:id>/',views.teach2),
    path('disp/',views.display),
    path('subjects1/<int:id>/',views.subjects1),
    path('display2/<int:id>/',views.display2),
    
]