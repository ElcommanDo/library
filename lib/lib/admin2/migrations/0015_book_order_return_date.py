# Generated by Django 3.0.4 on 2020-03-13 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0014_borrowed_book_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_order',
            name='return_date',
            field=models.DateField(null=True),
        ),
    ]
