from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import ThriftUserManager


class ThriftUser(AbstractBaseUser, PermissionsMixin):
    class Address(models.TextChoices):
        BHAKTAPUR = "bhaktapur", "Bhaktapur"
        BHARATPUR = "bharatpur", "Bharatpur"
        BIRATNAGAR = "biratnagar", "Biratnagar"
        BIRGUNJ = "birgunj", "Birgunj"
        BUTWAL = "butwal", "Butwal"
        DHANGADHI = "dhangadhi", "Dhangadhi"
        DHARAN = "dharan", "Dharan"
        HETAUDA = "hetauda", "Hetauda"
        ILAM = "ilam", "Ilam"
        ITAHARI = "itahari", "Itahari"
        JANAKPUR = "janakpur", "Janakpur"
        JHAPA = "jhapa", "Jhapa"
        KATHMANDU = "kathmandu", "Kathmandu"
        LALITPUR = "lalitpur", "Lalitpur"
        NEPALGUNJ = "nepagunj", "Nepalgunj"
        POKHARA = "pokhara", "Pokhara"

    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    address = models.CharField(
        max_length=100,
        choices=Address.choices,
        default=Address.KATHMANDU,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['address', 'phone_no', ]

    objects = ThriftUserManager()

    def __str__(self):
        return self.email
    
    def get_fullname(self):
        return self.first_name + self.last_name
