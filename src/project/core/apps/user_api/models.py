from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class MainUser(models.Model):
    DISCOUNT_VALUES = (
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


class ManagerUser(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="manager_user")

    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name="manager_users")


class StoreKeeperUser(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name="store_user")

    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name="store_users")
    manager_user = models.ForeignKey(to=ManagerUser, on_delete=models.CASCADE, related_name="store_users")
