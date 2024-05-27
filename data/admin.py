from django.contrib import admin
from data.models import MendeleyData


@admin.register(MendeleyData)
class MendeleyDataAdmin(admin.ModelAdmin):
    list_display = ('time', 'aeration_rate', 'agitator_rpm')
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]
