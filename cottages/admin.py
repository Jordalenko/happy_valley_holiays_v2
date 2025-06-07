from django.contrib import admin
from .models import Cottage, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Cottage)
class CottageAdmin(SummernoteModelAdmin):
    list_display = ('cottage_id', 'slug')
    search_fields = ['cottage_id', 'description']
    prepopulated_fields = {'slug': ('cottage_id',)}
    summernote_fields = ('description',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'cottage', 'rating', 'created_on')
    list_filter = ('rating', 'created_on')
    search_fields = ('cottage__cottage_id', 'author__username', 'body')
