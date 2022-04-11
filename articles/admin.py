from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopeship, Tag


class ScopeshipInlineFormset(BaseInlineFormSet):

    def clean(self):
        is_main_count = 0
        for form in self.forms:
            is_main_count += 1 if form.cleaned_data.get('is_main') else 0
        if is_main_count == 0:
            raise ValidationError('Укажите основной раздел')
        elif is_main_count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeshipInline(admin.TabularInline):

    model = Scopeship
    formset = ScopeshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    inlines = [ScopeshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    pass
