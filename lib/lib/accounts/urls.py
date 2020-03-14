from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.login_admin,name='login'),
    path('logout/',views.logout_admin,name='logout'),
    path('create_admin/',views.create_admin,name='create_admin'),
    path('create_superAdmin/',views.create_super_admin,name='create_super_admin'),
    path('super-admin-dashboard/',views.admin_dash,name='admin'),
    path('create-member/',views.create_member,name='create_member'),
    path('show-members/',views.show_members,name='show_members'),
    path('show-users/',views.show_users,name='show_users'),
    path('update-member/<int:id>/',views.update_member,name='update_member'),
    path('update-admin/<int:id>/',views.update_admin,name='update_admin'),
    path('delete-member/<int:id>/',views.delete_member,name='delete_member'),
    path('delete-admin/<int:id>/',views.delete_admin,name='delete_user'),
    
]
