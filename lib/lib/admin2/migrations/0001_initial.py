# Generated by Django 3.0.4 on 2020-03-07 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publishing_house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Questioner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questioner_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('book_pages', models.PositiveIntegerField(default=0)),
                ('book_folders', models.PositiveIntegerField(default=0)),
                ('print_number', models.PositiveIntegerField(default=0)),
                ('print_year', models.DateField(null=True)),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('created_at', models.DateField()),
                ('book_image', models.ImageField(null=True, upload_to='books_images')),
                ('observations', models.TextField(null=True)),
                ('available', models.BooleanField(default=True)),
                ('no_of_copis', models.IntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin2.Author')),
                ('book_postion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin2.Position')),
                ('publish_house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin2.Publishing_house')),
                ('questioner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin2.Questioner')),
            ],
        ),
    ]
