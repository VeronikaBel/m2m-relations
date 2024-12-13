from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = sum([form.cleaned_data.get('is_main') for form in self.forms])
        
        if not any(form.has_changed() for form in self.forms):
            return super().clean()
        
        if main_count != 1:
            raise ValidationError("Может быть только один основной раздел!")
        
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    # formset = ScopeInlineFormset 

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'image']
    search_fields = ['title', 'text']
    inlines = [ScopeInline]
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass