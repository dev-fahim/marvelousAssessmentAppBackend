from django.urls import path
from apps.accounts.views import login_view, logout_view

app_name = "auth"

urlpatterns = [
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view")
]
