from django.urls import path, include
from django.views.generic import TemplateView

from Accounting.views import dashboard as dashboard_views
from Accounting.views import general as general_views
from Accounting.views import auth as auth_views
from Accounting.views import item as item_views
from Accounting.views import group as group_views
from Accounting.views import tag as tag_views

urlpatterns = [
    # ******************** DEFAULT URLS ***************************************
    path('', general_views.index, name='index'),
    path('AboutUs/', TemplateView.as_view(template_name="Accounting/aboutus.html"), name='about_us'),
    path('ContactUs/', general_views.contactus, name='contact_us'),
    path('test/', general_views.test),
    path('captcha/', include('captcha.urls')),
    # ******************** ACCOUNTING URLS ************************************
    path('accounts/signin', auth_views.LoginView.as_view(), name='signin'),
    path('accounts/signout', auth_views.signout, name='signout'),
    path('accounts/join', auth_views.join, name='join'),
    path('accounts/signup', general_views.signup, name='signup'),

    # ******************** DASHBOARD URLS *************************************
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('dashboard/import-csv', dashboard_views.DashboardImportCSV.as_view(),
         name="dashboard_import_csv"),
    path('dashboard/profile', dashboard_views.dashboard_profile,
         name="dashboard_profile"),

    # ******************** ITEM URLS ******************************************
    path('dashboard/items', item_views.ItemFilteredSingleTableView.as_view(),
         name="dashboard_items"),
    path('dashboard/items/new', item_views.NewItemView.as_view(),
         name="dashboard_items_new"),
    path('dashboard/items/update/<int:pk>',
         item_views.ItemUpateView.as_view(), name="dashboard_item_update"),
    path('dashboard/items/delete/<int:pk>', item_views.ItemDeleteView.as_view(),
         name="dashboard_item_delete"),

    # ******************** GROUP URLS *****************************************
    path('dashboard/groups', group_views.GroupListView.as_view(),
         name="dashboard_groups"),
    path('dashboard/groups/new', group_views.GroupNewView.as_view(),
         name="dashboard_groups_new"),
    path('dashboard/groups/<int:pk>/update',
         group_views.GroupUpdateView.as_view(), name='dashboard_groups_update'),
    path('dashboard/groups/<int:pk>/delete',
         group_views.GroupDeleteView.as_view(), name='dashboard_groups_delete'),

    # ******************** TAG URLS *******************************************
    path('dashboard/tags', tag_views.TagListView.as_view(), name="dashboard_tags"),
    path('dashboard/tags/new', tag_views.TagNewView.as_view(),
         name="dashboard_tags_new"),
    path('dashboard/tags/<int:pk>/update', tag_views.TagUpdateView.as_view(),
         name="dashboard_tag_update"),
    path('dashboard/tags/<int:pk>/delete',
         tag_views.TagDeleteView.as_view(), name="dashboard_tag_delete"),
    # ******************** OTHER URLS *****************************************

]
