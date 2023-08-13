from django.contrib import admin
from .models import HeroInfo, BookInfo


class BookAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date', 'bread', 'bcomment', 'isDeleted']

class HeroAdmin(admin.ModelAdmin):
    list_display = ('hname','hgender','hcomment','hbook','isDeleted')

# Register your models here.
admin.site.register(BookInfo,BookAdmin)
admin.site.register(HeroInfo,HeroAdmin)
