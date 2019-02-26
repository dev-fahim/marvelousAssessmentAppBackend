from project.core.apps.user_api.models import (MainUser, AdminUser, ManagerUser, StoreKeeperUser, UserType)


def get_main_user_model(request):
    user_type = UserType.objects.get(user_id=request.user.id)
    if user_type.is_main_user:
        return MainUser.client.get_client_model(request)
    if user_type.is_admin_user:
        return AdminUser.client.get_admin_main_user_model(request)
    if user_type.is_manager_user:
        return ManagerUser.client.get_manager_main_user_model(request)
    if user_type.is_store_keeper_user:
        return StoreKeeperUser.client.get_store_keeper_main_user_model(request)
