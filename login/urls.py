from django.urls import path
from .views import (
    CustomLoginView,
    role_based_dashboard_redirect,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # ✅ keep this
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', role_based_dashboard_redirect, name='dashboard_redirect'),
]
