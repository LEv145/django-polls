from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    verbose_name_plural = "Выборы"


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, dict(fields=["question_text"])),
        ("Информация о дате", dict(fields=["published_date"], classes=["collapse"])),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "published_date", "was_published_recently")
    list_filter = ("published_date",)
    search_fields = ("question_text",)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
