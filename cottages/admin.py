from django.contrib import admin
from .models import Cottage, Review, CottageImage
from django_summernote.admin import SummernoteModelAdmin


class CottageImageInline(admin.TabularInline):
    model = CottageImage
    extra = 1


@admin.register(Cottage)
class CottageAdmin(SummernoteModelAdmin):
    list_display = ('cottage_id', 'slug')
    search_fields = ['cottage_id', 'description']
    prepopulated_fields = {'slug': ('cottage_id',)}
    summernote_fields = ('description',)
    inlines = [CottageImageInline]  # ✅ Add inlines here


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'cottage', 'rating', 'created_on')
    list_filter = ('rating', 'created_on')
    search_fields = ('cottage__cottage_id', 'guest__username', 'body')


admin.site.register(CottageImage)
