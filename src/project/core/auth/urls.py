from django.urls import path
from project.core.auth.views import Login

app_name = "core"

urlpatterns = [
    path('login/', Login.as_view(), name="login")
]