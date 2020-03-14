from django.shortcuts import render, redirect,HttpResponse
from .models import Author, Book,Book_order,Borrowed_book, Position,Publishing_house,Questioner,Category
from django.contrib import messages
from accounts.models import Member
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic.base import TemplateView
import xlwt
from django.contrib.auth.decorators import user_passes_test

class CSVPageView(TemplateView):
    template_name = "existing_books.html"


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Book Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['اسم الكتاب', 'عدد الصفحات', 'عدد المجلدات','سعر الكتاب','رقم الطباعه','عدد النسخ','دار النشر','المحقق','التصنيف','الموقع']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    
    rows =  Book.objects.filter(available=True).values_list('book_name', 'book_pages', 'book_folders', 'book_price','print_number','no_of_copis','publish_house__publish_name','questioner__questioner_name','category__category_name','book_postion__position')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Book Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['اسم الكتاب', 'عدد الصفحات', 'عدد المجلدات','سعر الكتاب','رقم الطباعه','عدد النسخ','دار النشر','المحقق','التصنيف','الموقع']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    
    rows =  Book.objects.all().values_list('book_name', 'book_pages', 'book_folders', 'book_price','print_number','no_of_copis','publish_house__publish_name','questioner__questioner_name','category__category_name','book_postion__position')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

def export_borrowed_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Book Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['اسم الكتاب', 'اسم المستعير']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    
    rows =  Borrowed_book.objects.all().values_list('book__book_name', 'member__user__username')
    for row in rows:
        
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
from django.contrib.auth.decorators import login_required
login_required(login_url='login')
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    auths = Author.objects.all()
    pubs = Publishing_house.objects.all()
    poses = Position.objects.all()
    cats = Category.objects.all()
    ques = Questioner.objects.all()
    books = Book.objects.all()
    members = Member.objects.all()
    context = {
        'books':books,
        'members':members,
        'categories':cats,
                'publishes':pubs,
                'positions':poses,
                'authors':auths,
                'quest':ques
                }
    return render(request,'admin/home.html', context)

def add_author(request):
    if request.method=="POST":
        if Author.objects.filter(author_name=request.POST['author']):
             messages.warning(request,'هذا المؤلف موجود بالفعل')
             return redirect('home')

         
        Author.objects.create(author_name=request.POST['author'])
        messages.success(request,'تم اضافه المؤلف بنجاح')
        return redirect('home')    
    
def add_category(request):
    if request.method=="POST":
        if Category.objects.filter(category_name=request.POST['category']):
             messages.warning(request,'هذا التصنيف مضاف من قبل')
             return redirect('home')
        Category.objects.create(category_name=request.POST['category'])
        
    messages.success(request,'تم اضافه التصنيف بنجاح')
    return redirect('home')


def add_questioner(request):
    if request.method=="POST":
        if Questioner.objects.filter(questioner_name=request.POST['questioner']):
             messages.warning(request,'هذا المحقق مضاف من قبل')
             return redirect('home')
        Questioner.objects.create(questioner_name=request.POST['questioner'])
        
    messages.success(request,'تم اضافه المحقق بنجاح')
    return redirect('home')

def add_position(request):
    if request.method=="POST":
        if Position.objects.filter(position=request.POST['position']):
             messages.warning(request,'هذا الموقع مضاف من قبل')
             return redirect('home')
        Position.objects.create(position=request.POST['position'])
        
    messages.success(request,'تم اضافه الموقع بنجاح بنجاح')
    return redirect('home')

def add_publish(request):
    if request.method=="POST":
        if Publishing_house.objects.filter(publish_name=request.POST['publish']):
             messages.warning(request,'هذه الدار مضافه من قبل ')
             return redirect('home')
    Publishing_house.objects.create(publish_name=request.POST['publish'])
        
    messages.success(request,'تم اضافه الدار بنجاح')
    return redirect('home')

def add_book(request):
    if request.method=="POST":
        data = request.POST
        if Book.objects.filter(book_name=data['book_name']):
            messages.warning(request,'هذا الكتاب مضاف من قبل')
            return redirect('home')
        else:
            book = Book()
            book.book_name = data['book_name']
            book.book_pages = data['pages']
            book.book_price = data['price']
            print(request.FILES.get('image'))
            if request.FILES.get('image') != '':
                book.book_image = request.FILES.get('image')

            if data['folders'] !='':

                book.book_folders = data['folders']
            if data['print_number'] !='':
                book.print_number = data['print_number']
            if data['print_year'] !='':
                book.print_year = data['print_year']
            if data['link'] !='':
                book.link = data['link']
            if data['copies'] !='':
                book.no_of_copis = data['copies']
            book.book_owner = data['owner']
            book.folder_number = data['folder_number']
            book.observations = data['obs']
            if Position.objects.get(position = data.get('position')):
                book.book_postion = Position.objects.get(position = data.get('position'))
            if Author.objects.filter(author_name=data['author']):
                book.author = Author.objects.get(author_name=data['author'])
                
            else:
                obj =Author(author_name=data['author'])
                obj.save()
                book.author = obj
            if Questioner.objects.filter(questioner_name=data['questioner']):
                book.questioner = Questioner.objects.get(questioner_name=data['questioner'])
            else:
                obj =Questioner(questioner_name = data['questioner'])
                obj.save()
                book.questioner = obj
            if Publishing_house.objects.filter(publish_name=data['publish']):
                book.publish_house=Publishing_house.objects.get(publish_name=data['publish'])
            else:
                obj=Publishing_house(publish_name = data['publish'])
                obj.save()
                book.publish_house = obj
            if Category.objects.filter(category_name=data['category']):
                book.category = Category.objects.get(category_name=data['category'])
            else:
                obj=Category(category_name = data['category'])
                obj.save()
                book.category = obj

            book.save()
        messages.success(request,'تم اضافه الكتاب بنجاح')
        return redirect('home')

def books(request):
    
    auths = Author.objects.all()
    pubs = Publishing_house.objects.all()
    poses = Position.objects.all()
    cats = Category.objects.all()
    ques = Questioner.objects.all()
    context = {
        'categories':cats,
                'publishes':pubs,
                'positions':poses,
                'authors':auths,
                'quest':ques
                }
    
    if request.method=="POST":
        books = Book.objects.filter(book_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/books.html',context)
        books = Book.objects.filter(category__category_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/books.html',context)
        books = Book.objects.filter(publish_house__publish_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/books.html',context)
        books = Book.objects.filter(author__author_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/books.html',context)
        books = Book.objects.filter(questioner__questioner_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/books.html',context)

    else:
        books = Book.objects.all()
        context['books']=books

    return render(request,'admin/books.html',context)

@user_passes_test(lambda u: u.is_superuser)
def update_book(request,id):
    if request.method=="POST":
            book = Book.objects.get(id=id)
            data = request.POST
            book.book_name = data['book_name']
            book.book_pages = data['pages']
            book.book_price = data['price']
            if data['folders'] !='':

                book.book_folders = data['folders']
            if data['print_number'] !='':
                book.print_number = data['print_number']
            if data['print_year'] !='':
                book.print_year = data['print_year']
            if data['link'] !='':
                book.link = data['link']
            if data['copies'] !='':
                book.no_of_copis = data['copies']
            
            if request.FILES.get('img'):
                book.book_image = request.FILES.get('img')
            if data.get('available')=='on':
                book.available = True
            else:
                 book.available = False
            book.link = data['link']
            book.no_of_copis = data['copies']
            book.observations = data['obs']
            book.book_owner = data['owner']
            book.folder_number = data['folders_num']
            if Position.objects.get(position = data.get('position')):
                book.book_postion = Position.objects.get(position = data.get('position'))
            if Author.objects.filter(author_name=data['author']):
                book.author = Author.objects.get(author_name=data['author'])
            else:
                obj =Author(author_name=data['author'])
                obj.save()
                book.author = obj
            if Questioner.objects.filter(questioner_name=data['questioner']):
                book.questioner = Questioner.objects.get(questioner_name=data['questioner'])
            else:
                obj =Questioner(questioner_name = data['questioner'])
                obj.save()
                book.questioner = obj
            if Publishing_house.objects.filter(publish_name=data['publish']):
                book.publish_house=Publishing_house.objects.get(publish_name=data['publish'])
            else:
                obj=Publishing_house(publish_name = data['publish'])
                obj.save()
                book.publish_house = obj
            if Category.objects.filter(category_name=data['category']):
                book.category = Category.objects.get(category_name=data['category'])
            else:
                obj=Category(category_name = data['category'])
                obj.save()
                book.category = obj

            book.save()
            messages.success(request,'تم تعديل الكتاب بنجاح')
            return redirect('books')

@user_passes_test(lambda u: u.is_superuser)
def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,'تم حذف الكتاب بنجاح')
    return redirect('books')



def book_details(request,id):
    book = Book.objects.get(id=id)
    return render(request,'admin/book_details.html',{'book':book})




def borrow_books(request):
    context = {}
    if request.method=="POST":
        books = Book.objects.filter(book_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/borrow_books.html',context)
        books = Book.objects.filter(category__category_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/borrow_books.html',context)
        books = Book.objects.filter(author__author_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/borrow_books.html',context)
        books = Book.objects.filter(publish_house__publish_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/borrow_books.html',context)
        books = Book.objects.filter(questioner__questioner_name__contains=request.POST['book_name'])
        if books:
            context['books'] = books
            return render(request,'admin/borrow_books.html',context)
            
    books = Book.objects.all()    
    return render(request,'admin/borrow_books.html',{'books':books})


from datetime import date, timedelta
def borrow_process(request,id):
    if request.method=="POST":
        book = Book.objects.get(id=id)
        if book.available == False or book.no_of_copis == 0 :
            messages.warning(request,'عذرا هذا الكتاب غير متاح فى الوقت الحالى')
            return redirect('borrow_books')
        else:
            order = Book_order()
            order.book = book
            order.member = Member.objects.get(user=request.user)
            order.duration = request.POST['duration']
            
            order.save()
            messages.success(request,'تم ارسال طلب الاستعاره بنجاح')
            return redirect('borrow_books')


def orders(request):

    orders = Book_order.objects.filter(accepted=False)
    context = {'orders':orders}
    return render(request,'admin/book_orders.html',context)

from datetime import datetime
@user_passes_test(lambda u: u.is_superuser)
def accept_order(request,id):
    
    order = Book_order.objects.get(id=id)
    order.accepted = True
    if order.book.no_of_copis-1 <=0:
        order.book.available = False
    else:
        order.book.no_of_copis-=1    
    order.book.save()
    order.save()
    borrowed = Borrowed_book(book=order.book,member=order.member)
    borrowed.return_date =  datetime.now() + timedelta(days=order.duration)
    borrowed.save()
    if order.member.user.email:
         send_mail(
        'تم قبول طلب الاستعاره',
        'تم قبول طلب الاستعاره يرجى الذهاب لاستلام الكتاب',
        'abubadr9811@gmail.com',[order.member.user.email,]
        )
    messages.success(request,'تم قبول الطلب  وارسال رساله جيميل للعضو بنجاح')
    return redirect('orders')
@user_passes_test(lambda u: u.is_superuser)
def delete_order(request,id):
    order = Book_order.objects.get(id=id)
    send_mail(
        'عذرا بخصوص طلب الاستعاره',
        'نأسف لابلاغكم انه تم رفض  طلب الاستعاره يرجى التواصل مع مسئول لمكتبه لمعرفه السبب',
        'abubadr9811@gmail.com',[order.member.user.email,]
        )
    order.delete()
    messages.success(request,'تم حذف الطلب  وارسال رساله جيميل للعضو بنجاح')
    return redirect('orders')
@user_passes_test(lambda u: u.is_superuser)
def book_back(request):
    if request.method=="POST":
        book = Book.objects.get(book_name=request.POST['book_name'])
        book.no_of_copis+=1
        book.save()
        obj = Borrowed_book.objects.filter(book=book)[0]
        if obj:
            obj.delete()
        
        user = User.objects.get(username=request.POST['member'])
        member = Member.objects.get(user=user)
        order = Book_order.objects.filter(member=member,book=book)
        order.delete()
        messages.success(request,'تم استرجاع الكتاب بنجاح')
        return redirect('home')


def borrowed_books(request):

    books = Borrowed_book.objects.all()
    context = {'books':books}
    return render(request,'admin/borrowed_books.html',context)




def existing_books(request):
    bor = Borrowed_book.objects.all()
    books = Book.objects.filter(available=True)
    return render(request,'admin/existing_books.html',{'books':books})