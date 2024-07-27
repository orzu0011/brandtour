from django.contrib import admin
from .models import Contact, BannerImg


# Register your models here.


admin.site.register([Contact, BannerImg])

