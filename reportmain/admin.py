from django.contrib import admin
from reportmain.models import Base , DailyReport , Person , Machine
from adminViews import DailyReportAdmin , PersonAdmin , BaseAdmin ,MachineAdmin

# Register your models here.
admin.site.register(Base , BaseAdmin)
admin.site.register(DailyReport , DailyReportAdmin)
admin.site.register(Person , PersonAdmin)
admin.site.register(Machine , MachineAdmin)