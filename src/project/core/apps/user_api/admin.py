from django.contrib import admin
from project.core.apps.user_api.models import UserType, MainUser, ManagerUser, AdminUser, StoreKeeperUser
# Register your models here.


admin.site.register(UserType)
admin.site.register(MainUser)
admin.site.register(ManagerUser)
admin.site.register(AdminUser)
admin.site.register(StoreKeeperUser)

