# Generated by Django 3.0.4 on 2020-03-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0012_borrowed_book_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_owner',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='folder_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='print_year',
            field=models.IntegerField(null=True),
        ),
    ]
