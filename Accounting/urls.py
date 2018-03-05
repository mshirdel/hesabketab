from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin', views.signin, name='signin'),
    path('accounts/signout', views.signout, name='signout'),
    path('accounts/join', views.join, name='join'),
    path('AboutUs/', views.about_us, name='about_us'),
    path('ContactUs/', views.index, name='contact_us'),
    path('blog/', views.index, name='blog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/items', views.dashboard_items, name="dashboard_items"),
    path('dashboard/groups', views.dashboard_groups, name="dashboard_groups"),
    path('dashboard/tags', views.dashboard_tags, name="dashboard_tags"),
    path('dashboard/import-csv', views.dashboard_import_from_csv, name="dashboard_import_csv"),
    path('dashboard/profile', views.dashboard_profile, name="dashboard_profile")
]
