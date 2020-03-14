from django.contrib import admin
from .models import Book,Author,Category,Position,Publishing_house,Borrowed_book,Book_order, Questioner
from import_export.admin import ImportExportModelAdmin
    
# Register your models here.
@admin.register(Book,Category,Publishing_house,Position,Questioner,Author,Borrowed_book ,Book_order)
class ViewAdmin(ImportExportModelAdmin):
    pass
