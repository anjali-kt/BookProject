# Generated by Django 3.2.13 on 2022-07-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default='abcd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
