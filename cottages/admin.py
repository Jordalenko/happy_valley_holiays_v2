from django.contrib import admin
from .models import Cottage, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('review_id', 'cottage', 'guest', 'status', 'created_at')
    search_fields = ['cottage__cottage_id', 'guest__username', 'comment']
    list_filter = ('status', 'created_at')
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('comment',)


# Register your models here.
admin.site.register(Cottage)
