from django.db import models
from  accounts.models import Member
# Create your models here.


#التصنيف 

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
##المؤلف
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    def __str__(self):
        return self.author_name
# دار النشر
class Publishing_house(models.Model):
    publish_name = models.CharField(max_length=200)
    def __str__(self):
        return self.publish_name
#المحقق 
class Questioner(models.Model):
    questioner_name = models.CharField(max_length=200)
    def __str__(self):
        return self.questioner_name

class Position(models.Model):
    position = models.CharField(max_length=200)
    def __str__(self):
        return self.position
#الكتاب
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_pages = models.PositiveIntegerField(default=0)
    book_folders = models.PositiveIntegerField(default=0)
    print_number = models.PositiveIntegerField(default=0)
    print_year = models.IntegerField(null=True)
    book_price = models.DecimalField(max_digits=11,decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    book_image =  models.ImageField(default='o.jpg', upload_to='books_images',null=True,blank=True)
    observations = models.TextField(null=True)
    available = models.BooleanField(default=True)
    no_of_copis = models.IntegerField(default=1)
    publish_house = models.ForeignKey(Publishing_house,on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    questioner = models.ForeignKey(Questioner,on_delete=models.CASCADE,null=True)
    book_postion= models.ForeignKey(Position,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    link =  models.CharField(max_length=900,null=True)
    book_owner = models.CharField(max_length=200,null=True)
    folder_number = models.IntegerField(default=0)

 
    def __str__(self):
        return self.book_name

    


class Book_order(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE,null=True,blank=True)
    accepted = models.BooleanField(default=False)
    duration = models.IntegerField(null=True)


class Borrowed_book(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)

