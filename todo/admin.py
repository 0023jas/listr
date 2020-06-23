from django.contrib import admin
from .models import TodoItem
from .models import CurrentlyWorkingItem
from .models import FinishedItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(CurrentlyWorkingItem)
admin.site.register(FinishedItem)