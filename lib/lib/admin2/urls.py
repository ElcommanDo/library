from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add-category/',views.add_category,name='add_category'),
    path('add-publish-house/',views.add_publish,name='add_publish'),
    path('add-position/',views.add_position,name='add_position'),
    path('add-author/',views.add_author,name='add_author'),
    path('add-questioner/',views.add_questioner,name='add_questioner'),
    path('add_book/',views.add_book,name='add_book'),
    path('books/',views.books,name='books'),
    path('update_book/<int:id>',views.update_book,name='update_book'),
    path('delete_book/<int:id>/',views.delete_book,name='delete_book'),
    path('book-details/<int:id>/',views.book_details,name='book_details'),
    path('borrow_books/',views.borrow_books,name='borrow_books'),
    path('borrow_process/<int:id>/',views.borrow_process,name='borrow_process'),
    path('orders/',views.orders,name='orders'),
    path('accept_order/<int:id>', views.accept_order,name='accept_order'),
    path('delete_order/<int:id>', views.delete_order,name='delete_order'),
    path('book_back/',views.book_back,name='book_back'),
    path('borrowed_books/',views.borrowed_books,name='borrowed_books'),
    path('existing_books/',views.existing_books,name='existing_books'),
    path('csv-exist-bbok',views.export_users_xls,name='export-exist'),
    path('csv-bbok',views.export_xls,name='export-all'),
    path('export_borrowed_users_xls',views.export_borrowed_users_xls,name='export_borrowed_users_xls'),
]
