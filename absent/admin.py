from django.contrib import admin

from .models import Absent, PreReview, Review

# Register your models here.
admin.site.register(Absent)
admin.site.register(PreReview)
admin.site.register(Review)
