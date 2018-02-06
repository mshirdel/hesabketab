from django.urls import path, include

from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/join', views.signup, name='sign_up'),
    path('AboutUs/', views.index, name='about_us'),
    path('ContactUs/', views.index, name='contact_us'),
    path('blog/', views.index, name='blog'),
]