from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('account/details/', views.AccountDetailView.as_view(), name='account-detail'),
    # path('account/details/<int:pk>/', views.AccountDetailView.as_view(), name='account-detail'),
]
