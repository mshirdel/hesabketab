from django.urls import path, include
from django.views.generic import TemplateView

from Accounting import views

urlpatterns = [
    # ******************** DEFAULT URLS ***************************************
    path('', views.index, name='index'),
    path('AboutUs/', TemplateView.as_view(template_name="Accounting/aboutus.html"), name='about_us'),
    path('ContactUs/', views.contactus, name='contact_us'),
    # ******************** ACCOUNTING URLS ************************************
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin', views.SignIn.as_view(), name='signin'),
    path('accounts/signout', views.signout, name='signout'),
    path('accounts/join', views.join, name='join'),

    # ******************** DASHBOARD URLS *************************************
    path('dashboard/', views.dashboard, name='dashboard'),

    # ******************** ITEM URLS ******************************************
    path('dashboard/items', views.DashboardItemView.as_view(),
         name="dashboard_items"),
    path('dashboard/items/new', views.NewItemView.as_view(),
         name="dashboard_items_new"),
    path('dashboard/items/<int:pk>/update',
         views.ItemUpateView.as_view(), name="dashboard_item_update"),

    # ******************** GROUP URLS *****************************************
    path('dashboard/groups', views.DashboardGroupView.as_view(),
         name="dashboard_groups"),
    path('dashboard/groups/new', views.DashboardGroupNewView.as_view(),
         name="dashboard_groups_new"),
    path('dashboard/groups/<int:pk>/update',
         views.GroupUpdateView.as_view(), name='dashboard_groups_update'),
    path('dashboard/groups/<int:pk>/delete',
         views.GroupDeleteView.as_view(), name='dashboard_groups_delete'),
    path('dashboard/groups/update',
         views.DashboardGroupUpdateVew.as_view(), name='dashboard_group_edit'),

    # ******************** TAG URLS *******************************************
    path('dashboard/tags', views.DashboardTagView.as_view(), name="dashboard_tags"),
    path('dashboard/tags/new', views.DashboardTagNewView.as_view(),
         name="dashboard_tags_new"),

    # ******************** OTHER URLS *****************************************
    path('dashboard/import-csv', views.DashboardImportCSV.as_view(),
         name="dashboard_import_csv"),
    path('dashboard/profile', views.dashboard_profile, name="dashboard_profile"),
]
