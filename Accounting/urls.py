from django.urls import path, include

from . import views

urlpatterns = [
    path('test/', views.test),
    path('', views.index, name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin', views.SignIn.as_view(), name='signin'),
    path('accounts/signout', views.signout, name='signout'),
    path('accounts/join', views.join, name='join'),
    path('AboutUs/', views.about_us, name='about_us'),
    path('ContactUs/', views.index, name='contact_us'),
    path('blog/', views.index, name='blog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/items', views.DashboardItemView.as_view(), name="dashboard_items"),
    path('dashboard/items/new', views.DashboardItemNewView.as_view(), name="dashboard_items_new"),
    path('dashboard/groups', views.dashboard_groups, name="dashboard_groups"),
    path('dashboard/tags', views.dashboard_tags, name="dashboard_tags"),
    path('dashboard/import-csv', views.dashboard_import_from_csv,
         name="dashboard_import_csv"),
    path('dashboard/profile', views.dashboard_profile, name="dashboard_profile"),
]
