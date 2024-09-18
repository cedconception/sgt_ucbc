from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('create/', views.create_account, name='create'),
    path('profile/change/', views.change_profile, name='change-profile'),

]
