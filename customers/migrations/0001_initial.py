# Generated by Django 5.2.3 on 2025-07-01 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0005_rename_book_id_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, unique=True)),
                ('additional_info', models.TextField(blank=True)),
                ('rating', models.PositiveSmallIntegerField(default=50)),
                ('book_count', models.PositiveSmallIntegerField(default=0, help_text='Number of currently rented books')),
                ('books', models.ManyToManyField(blank=True, to='books.book')),
            ],
        ),
    ]
