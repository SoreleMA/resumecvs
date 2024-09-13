from django.contrib import admin
from .models import Curriculum, Education, Experience

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'created_date')
    search_fields = ('name', 'last_name', 'email', 'phone')
    inlines = [EducationInline, ExperienceInline]


admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Education)
admin.site.register(Experience)