from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class UserType(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name='user_type')

    is_main_user = models.BooleanField()
    is_admin_user = models.BooleanField()
    is_manager_user = models.BooleanField()
    is_store_keeper_user = models.BooleanField()

    objects = models.Manager()

    def __str__(self):
        return self.user.__str__()


class MainUserManager(models.Manager):

    def get_client_model(self, request):
        return super().get_queryset().get(user_id=request.user.id)


class MainUser(models.Model):
    DISCOUNT_VALUES = (
        (0, '0%'),
        (5, '5%'),
        (7, '7%'),
        (12, '12%'),
        (30, '30%'),
        (50, '50%'),
        (70, '70%')
    )
    PLAN_VALUES = (
        (1, 'Plan 1'),
        (2, 'Plan 2'),
        (3, 'Plan 3')
    )

    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="main_user")

    discount = models.PositiveSmallIntegerField(choices=DISCOUNT_VALUES)
    plan = models.PositiveSmallIntegerField(choices=PLAN_VALUES)

    is_trial = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_limited = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)

    expire_date = models.DateField(auto_now_add=True)

    objects = models.Manager()
    client = MainUserManager()

    def __str__(self):
        return self.user.__str__()


class AdminUserManager(models.Manager):

    def get_admin_main_user_model(self, request):
        return super().get_queryset().get(user_id=request.user.id).main_user

    def get_client_model(self, request):
        return super().get_queryset().get(user_id=request.user.id)


class AdminUser(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="admin_user")

    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name="admin_users")

    objects = models.Manager()
    client = AdminUserManager()

    def __str__(self):
        return self.user.__str__()


class ManagerUserManager(models.Manager):

    def get_manager_main_user_model(self, request):
        return super().get_queryset().get(user_id=request.user.id).main_user

    def get_client_model(self, request):
        return super().get_queryset().get(user_id=request.user.id)


class ManagerUser(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="manager_user")

    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name="manager_users")
    admin_user = models.ForeignKey(to=AdminUser, on_delete=models.CASCADE, related_name="manager_users")

    objects = models.Manager()
    client = ManagerUserManager()

    def __str__(self):
        return self.user.__str__()


class StoreKeeperUserManager(models.Manager):

    def get_store_keeper_main_user_model(self, request):
        return super().get_queryset().get(user_id=request.user.id).main_user

    def get_client_model(self, request):
        return super().get_queryset().get(user_id=request.user.id)


class StoreKeeperUser(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="store_user")

    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name="store_users")
    admin_user = models.ForeignKey(to=AdminUser, on_delete=models.CASCADE, related_name="store_users")
    manager_user = models.ForeignKey(to=ManagerUser, on_delete=models.CASCADE, related_name="store_users")

    objects = models.Manager()
    client = StoreKeeperUserManager()

    def __str__(self):
        return self.user.__str__()
