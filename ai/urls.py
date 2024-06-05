from django.urls import path

from . import views



urlpatterns=[

    path('',views.index,name='index'),
    path('complaint/', views.create_complaint, name='complaint'),
    path('check',views.check,name='check'),
    path('success', views.success_page, name='success_page'),
    path('status/',views.status, name='status'),
    path('update_status/', views.update_status, name='update_status'),
    

]