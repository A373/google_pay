from django.contrib import admin
from .models import Airtel, Jio, Idea, Bsnl, Operator, User


# Register your models here.


class AirtelAdmin(admin.ModelAdmin):
    list_display = ['plan', 'plan1', 'plan2', 'plan3']


admin.site.register(Airtel, AirtelAdmin)


class JioAdmin(admin.ModelAdmin):
    list_display = ['plan', 'plan1', 'plan2', 'plan3']


admin.site.register(Jio, JioAdmin)


class IdeaAdmin(admin.ModelAdmin):
    list_display = ['plan', 'plan1', 'plan2', 'plan3']


admin.site.register(Idea, IdeaAdmin)


class BsnlAdmin(admin.ModelAdmin):
    list_display = ['plan', 'plan1', 'plan2', 'plan3']


admin.site.register(Bsnl, BsnlAdmin)


class OperatorAdmin(admin.ModelAdmin):
    list_display = ['airtel', 'jio', 'idea', 'bsnl']


admin.site.register(Operator.OperatorAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['airtel', 'jio', 'idea', 'bsnl']


admin.site.register(User.UserAdmin)
