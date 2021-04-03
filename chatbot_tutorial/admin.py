from django.contrib import admin
from chatbot_tutorial.models import AllCalls, GetUser


class AllCallsAdmin(admin.ModelAdmin):
    model = AllCalls

class GetUserAdmin(admin.ModelAdmin):
    model = GetUser


admin.site.register(AllCalls, AllCallsAdmin)
admin.site.register(GetUser, GetUserAdmin)