from django.urls import path
from project.core.apps.auth_api.views import Login

app_name = "core"

urlpatterns = [
    path('login/', Login.as_view(), name="login")
]