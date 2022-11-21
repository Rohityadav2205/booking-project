from django.contrib import admin
from .models import BookingModel
from.models import VisitModel
# Register your models here.
admin.site.register(BookingModel)
admin.site.register(VisitModel)