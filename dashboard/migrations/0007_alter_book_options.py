# Generated by Django 3.2.5 on 2021-11-29 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['authors_info']},
        ),
    ]